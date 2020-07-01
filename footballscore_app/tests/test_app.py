import pytest

@pytest.mark.django_db
def test_index(client, user):
    client.login(username = 'paulina', password = 'ad')
    response = client.get('/footballscore/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_league(client, user, league):
    client.login(username = 'paulina', password = 'ad')
    response = client.get('/footballscore/league/')
    assert response.status_code == 200
    assert len(response.context['objects']) == 3
    for i in range(len(league)):
        assert league[i] in response.context['objects']

@pytest.mark.django_db
def test_team(client, user, team):
    client.login(username = 'paulina', password = 'ad')
    response = client.get('/footballscore/teams/')
    assert response.status_code == 200
    assert len(response.context['objects']) == 2
    for i in range(len(team)):
        assert team[i] in response.context['objects']