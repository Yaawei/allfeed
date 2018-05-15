from django.shortcuts import render
from django.views.generic.list import ListView
from .models import NewsPiece
from django.http import HttpResponse


class HomepageView(ListView):
    model = NewsPiece
    context_object_name = 'newspieces'
    template_name = 'home.html'


def test2(request):
    return render(request, 'reddit_feed.html',)