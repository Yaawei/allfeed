from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from newsfeed.models import UserFeedChoices, RssUrl


class SignUpForm(UserCreationForm):
    email = forms.CharField(
        max_length=254,
        required=True,
        widget=forms.EmailInput()
    )

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )


class FeedSubscriptionsForm(ModelForm):
    class Meta:
        model = UserFeedChoices
        fields = ['rss_url']
        # checkbox widget doesnt work like it should
        widgets = {
            'rss_url': forms.CheckboxSelectMultiple
        }

