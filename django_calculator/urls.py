from django.conf.urls import url, include
from django.contrib import admin
from calculator_app.views import calculator_view, UserCreateView, ProfileView, ProfileUpdateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', calculator_view, name='calculator_view'),
    url(r'^create_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^accounts/profile/$', ProfileView.as_view(), name='profile_view'),
    url(r'^accounts/profile/(?P<pk>\d+)/$', ProfileUpdateView.as_view(), name='profile_update_view'),
]
