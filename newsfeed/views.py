from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import NewsPiece, UserFeedChoices, RssUrl

from django.contrib.auth.mixins import LoginRequiredMixin


class HomepageView(TemplateView):
    template_name = 'home.html'


class GenericFilteredView(LoginRequiredMixin, ListView):
    model = NewsPiece
    context_object_name = 'newspieces'
    template_name = 'feed.html'
    login_url = 'login'
    filter_kwargs = {}

    def get_queryset(self):
        try:
            rss_urls_of_user_subs = RssUrl.objects.filter(userfeedchoices__user=self.request.user)
            return NewsPiece.objects.filter(
                **self.filter_kwargs,
                rss_source__in=rss_urls_of_user_subs
            ).order_by('-publish_date')
        except TypeError:
            return NewsPiece.objects.order_by('-publish_date')
