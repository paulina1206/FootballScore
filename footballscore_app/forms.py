from django import forms
from django.core.exceptions import NON_FIELD_ERRORS

from footballscore_app.models import Match, Team, League


class LeagueForm(forms.ModelForm):
    class Meta:
        model = League
        fields = "__all__"
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'})
        }
        help_texts = {
            'hierarchy': ('(Level of league in country)'),
        }
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': ("It can be one league in country at this level"),
            },
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"
        widgets = {
            'season': forms.CheckboxSelectMultiple
        }

class TeamSeasonForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"


class MatchForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        team_home = cleaned_data['team_home'].season.season
        team_away = cleaned_data['team_away'].season.season
        if team_home and team_away:
            if team_home != team_away:
                raise forms.ValidationError("Teams don't play at the same league.")
        return cleaned_data

    class Meta:
        model = Match
        fields = "__all__"


class SearchForm(forms.Form):
    query = forms.CharField(required=False)
