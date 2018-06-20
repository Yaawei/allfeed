from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from datetime import datetime, timedelta
from newsfeed import views
from accounts import views as accounts_views
from api import views as api_views


urlpatterns = [
    url(r'^$', views.HomepageView.as_view(), name='home'),
    url(r'^my-allfeed/today/$', views.NewspieceView.as_view(
        filter_kwargs={'publish_date__gte': datetime.utcnow()-timedelta(days=1)}
    ), name='today'),
    url(r'^my-allfeed/this-week/$', views.NewspieceView.as_view(
        filter_kwargs={'publish_date__gte': datetime.utcnow() - timedelta(days=7)}
    ), name='this week'),
    url(r'^my-allfeed/subscriptions/$', accounts_views.subscribe,
        name='subscriptions'),
    url(r'^api/liked/(?P<username>\w+)/$', api_views.LikedEntryView.as_view(), name='liked'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^admin/', admin.site.urls),
]
