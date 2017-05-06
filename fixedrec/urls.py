
from django import views
from django.conf.urls import url, include
from django.contrib import admin

from locations import views as locations_views
from activities import views as activity_views
from core import views as core_views
from authentication import views as authentication_views


urlpatterns = [

    #debug part
    url(r'^admin/', admin.site.urls),
    url(r'^$', core_views.home, name='home'),
    url(r'^locations/tracks/$', locations_views.track_list),
    url(r'^locations/new_tracks/$', locations_views.new_track_list),
    url(r'^locations/new_tracks/(?P<last_update>[0-9]+)/$', locations_views.new_track_list),
    url(r'^locations/new_tracks1/(?P<last_update_iso>(\d{4})-(\d{2})-(\d{2})T(\d{2})\:(\d{2})\:(\d{2})[+-](\d{2})\:(\d{2})+)/$', locations_views.last_update_iso),
    url(r'^locations/users/$', locations_views.UserList.as_view()),
    url(r'^locations/tracks/(?P<uuid>[0-9a-z-]+)/$',  locations_views.track_detail),
    # url(r'^locations/', locations_views.index),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),

    url(r'^', include('snippets.urls')),

    #core part
    url(r'^global_map/', core_views.global_map, name='global_map'),

    url(r'^messaging/', core_views.messaging, name='messaging'),
    url(r'^feed/', core_views.feed, name='feed'),


    #profiles part
    url(r'^signup/$', authentication_views.signup, name='signup'),
    url(r'^signin/$', authentication_views.signin, name='signin'),
    url(r'^signout/$', authentication_views.signout, name='signout'),
    url(r'^reset/$', authentication_views.reset, name='reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', authentication_views.reset_confirm, name='password_reset_confirm'),
    url(r'^success/$', authentication_views.success, name='success'),

    url(r'^tracks/(?P<username>[^/]+)$', core_views.tracks, name='tracks'),
    url(r'^tracks/', core_views.tracks, name='tracks'),




    url(r'^(?P<username>[^/]+)/$', core_views.profile, name='profile'),
    url(r'^(?P<username>[^/]+)/following/$', activity_views.following, name='following'),
    url(r'^(?P<username>[^/]+)/followers/$', activity_views.followers, name='followers'),


]
