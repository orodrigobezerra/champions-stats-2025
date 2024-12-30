from django.shortcuts import render
from django.core.paginator import Paginator
from champions_stats.models import Players, Teams

# Create your views here.


def home(request):
    # Todos os teams e players
    all_teams = Teams.objects.all()
    all_players = Players.objects.all()

    # Dados para o template
    return render(
        request,
        'champions_stats/home.html',
        {'teams': all_teams, 'players': all_players}
    )


def players(request):
    # Filtro de teams
    club_filter = request.GET.get('club', None)

    all_players = Players.objects.all().order_by('id_team__team')
    if club_filter and club_filter != 'all':
        filtered_players = all_players.filter(id_team__team__iexact=club_filter)
    else:
        filtered_players = all_players

    paginator = Paginator(filtered_players, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Lista de teams para o filtro
    clubs = Players.objects.values_list(
        'id_team__team', flat=True).distinct().order_by('id_team__team')

    return render(request, 'champions_stats/players.html', {
        'page_obj': page_obj,
        'clubs': clubs,
    })


def teams(request):
    country_filter = request.GET.get('country', None)

    all_teams = Teams.objects.all().order_by('country')
    if country_filter and country_filter != 'all':
        filtered_teams = all_teams.filter(country__iexact=country_filter)
    else:
        filtered_teams = all_teams

    paginator = Paginator(filtered_teams, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    # Lista de países únicos
    countries_list = Teams.objects.values_list(
        'country',
        flat=True).distinct().order_by('country')

    return render(request, 'champions_stats/teams.html', {
        'page_obj': page_obj,
        'countries': countries_list,
    })
