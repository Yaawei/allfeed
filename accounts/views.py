from django.contrib.auth import login
from .forms import SignUpForm, FeedSubscriptionsForm
from django.shortcuts import render, redirect
from newsfeed.models import UserFeedChoice, RssUrl


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
    initial_qs = RssUrl.objects.filter(userfeedchoice__user=user)
    if request.method == 'POST':
        form = FeedSubscriptionsForm(request.POST)
        if form.is_valid():
            subscriptions = form.cleaned_data.get('subscription')
            queries_to_delete = UserFeedChoice.objects.filter(
                user=user,
                rss_url__in=initial_qs.difference(subscriptions).values('id')
            )
            queries_to_add = subscriptions.difference(initial_qs)
            for query in queries_to_add:
                UserFeedChoice.objects.create(user=user, rss_url=query)
            queries_to_delete.delete()
            return redirect('subscriptions')
    elif request.method == 'GET':
        form = FeedSubscriptionsForm(
            initial={'subscription': initial_qs}
        )
    return render(request, 'subscription_form.html', {'form': form})

