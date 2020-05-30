from django.shortcuts import render
from .models import Teams, Player
from django.http import Http404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    context = {'all_teams': Teams.objects.all()}
    return render(request, 'teams/index.html', context)


def details(request, teamID):
    try:
        team: object = Teams.objects.get(pk=teamID)
    except Teams.DoesNotExist:
        raise Http404("Team is not registered")
    return render(request, 'teams/details.html', {'team': team})


def players(request, teamID):
    try:
        pl: object = Player.objects.filter(TeamID_id=teamID)
    except Player.DoesNotExist:
        raise Http404("No Registered Players in the Team")
    return render(request, 'teams/retplayers.html', {'pl': pl})


def home(request):
    return render(request, 'teams/home.html', {})


class TeamCreate(CreateView):
    model = Teams
    fields = ['TeamID', 'TeamName', 'TeamRank', ]


class TeamUpdate(UpdateView):
    model = Teams
    fields = ['TeamID', 'TeamName', 'TeamRank',]


def teamdelete(request, teamID):
    try:
        t: object = Teams.objects.filter(TeamID=teamID)
    except Player.DoesNotExist:
        raise Http404("Please Select a valid team to remove")
    deleted = t.delete()
    if deleted:
        return render(request, 'teams/delete_team__confirm.html', )
    else:
        raise Http404(" Sorry, we could not delete the given team")


class PlayerCreate(CreateView):
    model = Player
    fields = ['PID','TeamID', 'PName', 'PAge', 'PType', ]


class PlayerUpdate(UpdateView):
    model = Player
    fields = ['PID','TeamID', 'PName', 'PAge', 'PType', ]



def playerdelete(request, pid):
    try:
        t: object = Player.objects.filter(PID=pid)
    except Player.DoesNotExist:
        raise Http404("Please Select a valid player to remove")
    deleted = t.delete()
    if deleted:
        return render(request, 'teams/player_confirm_delete.html', )
    else:
        raise Http404(" Sorry, we could not delete the given team")

class Playerdelete(DeleteView):
    model = Player
    reverse_lazy('/teams/')




