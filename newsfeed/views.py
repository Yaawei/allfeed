from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import NewsPiece, RssUrl
from django.contrib.auth.mixins import LoginRequiredMixin


class HomepageView(TemplateView):
    template_name = 'home.html'


class GenericFilteredView(LoginRequiredMixin, ListView):
    model = NewsPiece
    context_object_name = 'newspieces'
    template_name = 'feed.html'
    login_url = 'login'
    filter_kwargs = {}
    paginate_by = 30

    def get_queryset(self):
        rss_urls_of_user_subscriptions = RssUrl.objects.filter(
            userfeedchoice__user=self.request.user
        )

        return NewsPiece.objects.filter(
            **self.filter_kwargs,
            rss_source__in=rss_urls_of_user_subscriptions
        ).order_by('-publish_date')


