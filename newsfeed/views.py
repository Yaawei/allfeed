from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.views.generic.list import MultipleObjectMixin
from .models import NewsPiece, RssUrl
from accounts.models import LikedEntry
from accounts.forms import BookmarkForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect


class HomepageView(TemplateView):
    template_name = 'home.html'


class NewspieceListView(ListView, LoginRequiredMixin):
    filter_kwargs = {}
    paginate_by = 30
    context_object_name = 'newspieces'
    template_name = 'feed.html'

    def get_queryset(self):
        rss_urls_of_user_subscriptions = RssUrl.objects.filter(
            userfeedchoice__user=self.request.user
        )
        return NewsPiece.objects.filter(
            **self.filter_kwargs,
            rss_source__in=rss_urls_of_user_subscriptions
        ).order_by('-publish_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BookmarkForm
        return context


class NewspieceBookmark(MultipleObjectMixin, FormView, LoginRequiredMixin):
    template_name = 'feed.html'
    filter_kwargs = {}
    paginate_by = 30
    form_class = BookmarkForm

    def get_queryset(self):
        rss_urls_of_user_subscriptions = RssUrl.objects.filter(
            userfeedchoice__user=self.request.user
        )
        return NewsPiece.objects.filter(
            **self.filter_kwargs,
            rss_source__in=rss_urls_of_user_subscriptions
        ).order_by('-publish_date')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            news_piece = self.get_queryset().filter(
                id=form.cleaned_data['bookmarked_obj']
            )
            LikedEntry.objects.get_or_create(
                user=self.request.user,
                liked_entry=news_piece.get()
            )
        current_url = request.get_full_path()
        return redirect(current_url)


class NewspieceView(View, LoginRequiredMixin):
    filter_kwargs = {}

    def get(self, request, *args, **kwargs):
        view = NewspieceListView.as_view(filter_kwargs=self.filter_kwargs)
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = NewspieceBookmark.as_view(filter_kwargs=self.filter_kwargs)
        return view(request, *args, **kwargs)
