from django.shortcuts import render
from django.views.generic.list import ListView
from .models import NewsPiece
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class HomepageView(LoginRequiredMixin, ListView):
    model = NewsPiece
    context_object_name = 'newspieces'
    template_name = 'home.html'
    login_url = 'login'

    def get_queryset(self):
        return NewsPiece.objects.order_by('-publish_date')


def test2(request):
    return render(request, 'reddit_feed.html',)
