from django.shortcuts import render
from django.core.paginator import Paginator
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


def players(request):
    # Filtro de clube
    club_filter = request.GET.get('club', None)

    players = Players.objects.all()
    if club_filter and club_filter != 'all':
        players = players.filter(id_team__team__iexact=club_filter)

    paginator = Paginator(players, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Lista de clubes para o filtro
    clubs = Players.objects.values_list(
        'id_team__team', flat=True).distinct().order_by('id_team__team')

    return render(request, 'champions_stats/players.html', {
        'page_obj': page_obj,
        'clubs': clubs,
    })


def teams(request):
    country_filter = request.GET.get('country', None)

    teams = Teams.objects.all()
    if country_filter and country_filter != 'all':
        teams = teams.filter(country__iexact=country_filter)

    paginator = Paginator(teams, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Pegue uma lista de países únicos
    countries = Teams.objects.values_list(
        'country',
        flat=True).distinct().order_by('country')

    return render(request, 'champions_stats/teams.html', {
        'page_obj': page_obj,
        'countries': countries,
    })
