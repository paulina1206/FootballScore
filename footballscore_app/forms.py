from django import forms
from footballscore_app.models import Match, Team, League

class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = "__all__"


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = "__all__"


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"
        widgets = {
            'season': forms.CheckboxSelectMultiple
        }

class SearchForm(forms.Form):
    query = forms.CharField(required=False)