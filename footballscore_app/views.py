import operator

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from footballscore_app.forms import LeagueForm, TeamForm, MatchForm, SearchForm, SeasonForm
from footballscore_app.models import Match, League, Team, Season
from datetime import date


# Create your views here.
class BaseView(View):
    def get(self, request):
        matches = Match.objects.filter(date=date.today())
        leaguess = League.objects.all()
        leagues = []
        for league in leaguess:
            for match in matches:
                if match.team_home.season.league.name == league.name and league not in leagues:
                    leagues.append(league)
        return render(request, "index.html", {'matches': matches, 'leagues': leagues})


class LeagueView(View):
    def get(self, request):
        leagues = League.objects.all()
        return render(request, "league.html", {'objects': leagues})

class SearchLeagueView(View):
    def get(self, request):
        leagues, search_form = self.search_match(request)
        return render(request, "search_league.html",
                      {'search_form': search_form, 'objects': leagues})

    def search_match(self, request):
        search_form = SearchForm(request.GET)
        search_form.is_valid()
        name = search_form.cleaned_data.get('query', '')
        q = Q(name__icontains=name)
        country = search_form.cleaned_data.get('query', '')
        q1 = Q(country__name__icontains=country)
        leagues = League.objects.filter(q | q1)
        return leagues, search_form

class AddLeagueView(PermissionRequiredMixin, CreateView):
    permission_required = 'footballscore_app.add_league'
    form_class = LeagueForm
    template_name = 'add_league.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': League.objects.all()})
        return context


class EditLeagueView(PermissionRequiredMixin, UpdateView):
    permission_required = 'footballscore_app.change_league'
    model = League
    fields = ['name', 'description', 'hierarchy', 'country']
    template_name = 'edit_league.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': League.objects.all()})
        return context


class DeleteLeagueView(PermissionRequiredMixin, DeleteView):
    permission_required = 'footballscore_app.delete_league'
    model = League
    template_name = 'delete_league.html'
    success_url = reverse_lazy('league')


class DetailLeagueView(View):
    def get(self, request, id):
        league = League.objects.get(pk=id)
        season = league.season_set.order_by("-season")
        paginator = Paginator(season, 1)
        page = request.GET.get('page')
        seasons = paginator.get_page(page)
        teamss = Team.objects.filter(played_in_season__league=league).order_by('-teamseason__points')
        teams = []
        for team in teamss:
            if team not in teams:
                teams.append(team)
        return render(request, "detail_league.html", {'league': league, 'teams': teams, 'seasons': seasons})


class TeamView(View):
    def get(self, request):
        teams = Team.objects.all()
        return render(request, "team.html", {'objects': teams})

class SearchTeamsView(View):
    def get(self, request):
        teams, search_form = self.search_team(request)
        teams_filtered = []
        for team in teams:
            if team not in teams_filtered:
                teams_filtered.append(team)
        return render(request, "search_team.html",
                      {'search_form': search_form, 'objects': teams_filtered})

    def search_team(self, request):
        search_form = SearchForm(request.GET)
        search_form.is_valid()
        name = search_form.cleaned_data.get('query', '')
        q = Q(name__icontains=name)
        league = search_form.cleaned_data.get('query', '')
        q1 = Q(played_in_season__league__name__icontains=league)
        teams = Team.objects.filter(q | q1)
        return teams, search_form

class AddTeamView(PermissionRequiredMixin, View):
    permission_required = 'footballscore_app.add_team'

    def get(self, request):
        form = TeamForm
        return render(request, "add_team.html", {'form': form})

    def post(self, request):
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teams')
        return render(request, "add_team.html", {'form': form})


class EditTeamView(PermissionRequiredMixin, View):
    permission_required = 'footballscore_app.change_team'

    def get(self, request, id):
        team = Team.objects.get(pk=id)
        form = TeamForm(instance=team)
        return render(request, "edit_team.html", {'form': form})

    def post(self, request, id):
        team = Team.objects.get(pk=id)
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect(f'/footballscore/teams/')
        return render(request, "edit_team.html", {'form': form})


class DeleteTeamView(PermissionRequiredMixin, DeleteView):
    permission_required = 'footballscore_app.delete_team'
    model = Team
    template_name = 'delete_team.html'
    success_url = reverse_lazy('teams')


class DetailTeamView(View):
    def get(self, request, id):
        team = Team.objects.get(pk=id)
        season = team.played_in_season.order_by('-season')
        paginator = Paginator(season, 1)
        page = request.GET.get('page')
        seasons = paginator.get_page(page)
        matchess = Match.objects.all()
        matches = []
        for match in matchess:
            if match.team_home.team.name == team.name or match.team_away.team.name == team.name:
                matches.append(match)
        return render(request, "detail_team.html", {'team': team, 'matches': matches, 'seasons': seasons})


class AddMatchView(PermissionRequiredMixin, View):
    permission_required = 'footballscore_app.add_match'

    def get(self, request):
        form = MatchForm
        return render(request, "add_match.html", {'form': form})

    def post(self, request):
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, "add_match.html", {'form': form})


class SearchMatchView(View):
    def get(self, request):
        matches, search_form = self.search_match(request)
        leaguess = League.objects.all()
        leagues = []
        for league in leaguess:
            for match in matches:
                if match.team_home.season.league.name == league.name and league not in leagues:
                    leagues.append(league)
        return render(request, "search_match.html",
                      {'search_form': search_form, 'matches': matches, 'leagues': leagues})

    def search_match(self, request):
        search_form = SearchForm(request.GET)
        search_form.is_valid()
        team_home = search_form.cleaned_data.get('query', '')
        q = Q(team_home__team__name__icontains=team_home)
        team_away = search_form.cleaned_data.get('query', '')
        q1 = Q(team_away__team__name__icontains=team_away)
        matches = Match.objects.filter(q | q1)
        return matches, search_form


class DeleteMatchView(PermissionRequiredMixin, DeleteView):
    permission_required = 'footballscore_app.delete_match'
    model = Match
    template_name = 'delete_match.html'
    success_url = reverse_lazy('search_match')


class EditMatchView(PermissionRequiredMixin, UpdateView):
    permission_required = 'footballscore_app.change_match'
    model = Match
    fields = "__all__"
    template_name = 'edit_match.html'
    success_url = reverse_lazy('search_match')


class AddSeasonView(PermissionRequiredMixin, CreateView):
    permission_required = 'footballscore_app.add_season'
    form_class = SeasonForm
    template_name = 'add_season.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': Season.objects.all()})
        return context


class EditSeasonView(PermissionRequiredMixin, UpdateView):
    permission_required = 'footballscore_app.change_season'
    model = Season
    fields = "__all__"
    template_name = 'edit_season.html'
    success_url = reverse_lazy('add_season')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': Season.objects.all()})
        return context

class DeleteSeasonView(PermissionRequiredMixin, DeleteView):
    permission_required = 'footballscore_app.delete_season'
    model = Season
    template_name = 'delete_season.html'
    success_url = reverse_lazy('add_season')