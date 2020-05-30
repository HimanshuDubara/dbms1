from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

from . import views

app_name = "teams"


urlpatterns = (
                  # /teams/
                  url(r'^$', views.index, name='index'),

                  # /teams/teamID
                  url(r'^(?P<teamID>[0-9]+)/$', views.details, name='details'),

                  # /teams/TeamID/Player
                  url(r'^(?P<teamID>[0-9]+)/players$', views.players, name='players'),
                  # /teams/add/
                  url(r'^add/$', views.TeamCreate.as_view(), name='Team-Add'),

                  # /teams/teamID/update/
                  url(r'^(?P<pk>[0-9]+)/update/$', views.TeamUpdate.as_view(), name='Team-Update'),

                  # /teams/teamID/delete/
                  url(r'^(?P<teamID>[0-9]+)/delete/$', views.teamdelete, name='Team-Delete'),

                  # /teams/add_player/
                  url(r'^add_player/$', views.PlayerCreate.as_view(), name='Player-Add'),

                  #/teams/players/pid/update/
                  url(r'^players/(?P<pk>[0-9]+)/update/$', views.PlayerUpdate.as_view(), name='Player-Update'),

                  #/teams/players/pid/delete/
                  url(r'^/players/(?P<pid>[0-9]+)/delete/$', views.playerdelete, name='Player-Delete'),


)

