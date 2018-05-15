from django.contrib import admin
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from newsfeed import views
from accounts import views as accounts_views

urlpatterns = [
    url(r'^$', views.HomepageView.as_view(), name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^reddit/$', views.test2, name='reddit'),
    url(r'^admin/', admin.site.urls),
]
