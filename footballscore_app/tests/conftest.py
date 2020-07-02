import pytest
from django.contrib.contenttypes.models import ContentType
from django.test import Client, override_settings
from footballscore_app.models import League, Team, Match, Country, Season, TeamSeason
from django.contrib.auth.models import User, Permission
from django.core.files import File


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def user():
    user = User(username='paulina')
    user.set_password('ad')
    user.save()
    contenttype = ContentType.objects.get(model='league')
    permissions1 = Permission.objects.filter(content_type=contenttype)
    contenttype = ContentType.objects.get_for_model(Season)
    permissions2 = Permission.objects.filter(content_type=contenttype)
    contenttype = ContentType.objects.get(model='team')
    permissions3 = Permission.objects.filter(content_type=contenttype)
    contenttype = ContentType.objects.get(model='match')
    permissions4 = Permission.objects.filter(content_type=contenttype)
    user.user_permissions.set(permissions1|permissions2|permissions3|permissions4)
    return user


@pytest.fixture
def league():
    s = Country.objects.create(name='Spain', flag='/uploads/flags/Spain.gif')
    e = Country.objects.create(name='England', flag='/uploads/flags/England.png')
    ge = Country.objects.create(name='Germany', flag='/uploads/flags/Germany.png')
    g = [League.objects.create(pk = 1, name='La Liga', description='Liga hiszpańska', hierarchy='1', country=s)]
    g.append(League.objects.create(pk = 2, name='Premier League', description='Liga angielska', hierarchy='1', country=e))
    g.append(League.objects.create(pk = 3, name='Bundesliga', description='Liga niemiecka', hierarchy='1', country=ge))
    return g


@pytest.fixture
def team():
    a = [Team.objects.create(pk=1, name='Bayern', description='Niemiecka liga', coach='JJ',
                             arms='/uploads/uploads/FC_Barcelona.png',
                             address='Bayern, Germany')]
    a.append(
        Team.objects.create(pk=2, name='Liverpool', description='Angielska Liga', arms='/uploads/uploads/FC_Barcelona.png',
                            coach='JJ', address='Liverpool, England'))
    return a

@pytest.fixture
def season():
    s = Country.objects.create(name='Spain', flag=File(file=b""))
    league = League.objects.create(name='La Liga', description='Liga hiszpańska', hierarchy='1', country=s)
    season = Season.objects.create(
        pk = 1,
        season="2019/2020",
        league=league, )
    return season

@pytest.fixture
def match():
    country = Country.objects.create(name='Spain', flag=File(file=b""))
    league = League.objects.create(name='La Liga', description='Liga hiszpańska', hierarchy='1', country=country)
    season = Season.objects.create(
        season="2019/2020",
        league=league)
    team1 = Team.objects.create(name='Bayern', description='Niemiecka liga', coach='JJ',
                        arms='/uploads/uploads/FC_Barcelona.png',
                        address='Bayern, Germany')
    team2 = Team.objects.create(name='Bayern', description='Niemiecka liga', coach='JJ',
                                arms='/uploads/uploads/FC_Barcelona.png',
                                address='Bayern, Germany')
    th = TeamSeason.objects.create(team=team1, season=season)
    ta = TeamSeason.objects.create(team=team2, season=season)
    match = Match.objects.create(pk=1, team_home=th, team_away=ta, date='2020-07-01')
    return match