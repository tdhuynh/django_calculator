from django.conf.urls import url, include
from django.contrib import admin
from calculator_app.views import UserCreateView, ProfileUpdateView, ProfileDetailView, CalculatorView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', CalculatorView.as_view(), name='calculator_view'),
    url(r'^create_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^accounts/profile/(?P<pk>\d+)/$', ProfileDetailView.as_view(), name='profile_detail_view'),
    url(r'^accounts/profile/(?P<pk>\d+)/update/$', ProfileUpdateView.as_view(), name='profile_update_view'),
]
