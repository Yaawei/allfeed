from django.contrib.auth import login
from .forms import SignUpForm, FeedSubscriptionsForm
from django.shortcuts import render, redirect
from newsfeed.models import UserFeedChoices


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def subscribe(request):
    user = request.user
    if request.method == 'POST':
        form = FeedSubscriptionsForm(request.POST)
        if form.is_valid():
            subscriptions = form.cleaned_data.get('subscription')
            if subscriptions:
                for query in subscriptions:
                    UserFeedChoices.objects.get_or_create(user=user, rss_url=query)
                return redirect('today')
    else:
        form = FeedSubscriptionsForm()
    return render(request, 'subscription_form.html', {'form': form})
