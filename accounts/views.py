from django.contrib.auth import login
from .forms import SignUpForm, FeedSubscriptionsForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from newsfeed.models import UserFeedChoices
from django.contrib.auth.models import User


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

#todo formularz do subskrypcji

class SubscriptionView(LoginRequiredMixin, FormView):
    form_class = FeedSubscriptionsForm
    template_name = 'subscription_form.html'
    success_url = 'abcd'
    model = UserFeedChoices
    user = User.objects.first()

    def form_invalid(self, form):
        print(form._errors)
        return super(SubscriptionView, self).form_invalid(form)


    def form_valid(self, form):
        print(form.fields)
        subscription = form.save(commit=False)
        subscription.user = self.user
        subscription.save()
        return super(SubscriptionView, self).form_valid(form)



