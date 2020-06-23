from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView
from footballscore_app.forms import LeagueForm
from footballscore_app.models import Match, League
from datetime import date

# Create your views here.
class BaseView(View):
    def get(self, request):
        matches = Match.objects.filter(date=date.today())
        return render(request, "index.html", {'matches': matches})

class LeagueView(View):
    def get(self, request):
        leagues = League.objects.all()
        return render(request, "league.html", {'objects': leagues})

class AddLeagueView(CreateView):
    form_class = LeagueForm
    template_name = 'add_league.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'objects': League.objects.all()})
        return context

class EditLeagueView(UpdateView): #id w urls
    model = League
    fields = ['name', 'description', 'hierarchy', 'country']
    # form_class = ProductForm  #dlaczego to nie działa?
    template_name = 'add_league.html'
    success_url = reverse_lazy('index')

class DeleteLeagueView(DeleteView):
    model = League  # jaki model
    template_name = 'delete_league.html'
    success_url = reverse_lazy('index')