import pytest
from django.contrib.contenttypes.models import ContentType
from django.test import Client, override_settings
from footballscore_app.models import League, Team, Match, Country
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
    p = Permission.objects.get(codename='view_league')
    user.user_permissions.add(p)
    p = Permission.objects.get(codename='view_team')
    user.user_permissions.add(p)

    # contenttype = ContentType.objects.get(model='genre')
    # permissions = Permission.objects.filter(content_type=contenttype)
    # user.user_permissions.set(permissions)

    return user

@pytest.fixture
def league():
    s= Country.objects.create(name='Spain', flag=File(file=b""))
    e= Country.objects.create(name='England', flag=File(file=b""))
    ge= Country.objects.create(name='Germany', flag=File(file=b""))
    g = [League.objects.create(name='La Liga', description='Liga hiszpańska', hierarchy='1', country=s)]
    g.append(League.objects.create(name='Premier League', description='Liga angielska', hierarchy='1', country=e))
    g.append(League.objects.create(name='Bundesliga', description='Liga niemiecka', hierarchy='1', country=ge))
    return g


@pytest.fixture
def team():
    a=[Team.objects.create(name='Bayern', description='Niemiecka liga', coach='JJ', arms='/uploads/uploads/FC_Barcelona.png',
                                 address='Bayern, Germany')]
    a.append(Team.objects.create(name='Liverpool', description='Angielska Liga', arms='/uploads/uploads/FC_Barcelona.png', coach='JJ', address='Liverpool, England'))
    return a

