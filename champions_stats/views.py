from django.shortcuts import render

from champions_stats.models import Players, Teams

# Create your views here.


def home(request):
    # Buscando os times e jogadores
    teams = Teams.objects.all()  # Obtendo todos os times
    players = Players.objects.all()  # Obtendo todos os jogadores

    # Passando os dados para o template
    return render(
        request,
        'champions_stats/home.html',
        {'teams': teams, 'players': players}
    )


def teams(request):
    # Buscando os times
    teams = Teams.objects.all()  # Obtendo todos os times

    # Passando os dados para o template
    return render(
        request,
        'champions_stats/teams.html',
        {'teams': teams}
    )


def players(request):
    # Buscando os jogadores
    players = Players.objects.all()  # Obtendo todos os jogadores

    # Passando os dados para o template
    return render(
        request,
        'champions_stats/players.html',
        {'players': players}
    )
