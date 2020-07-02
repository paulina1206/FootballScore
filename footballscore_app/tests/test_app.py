import pytest

@pytest.mark.django_db
def test_index(client):
    response = client.get('/footballscore/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_league(client, user, league):
    client.login(username='paulina', password='ad')
    response = client.get('/footballscore/league/')
    assert response.status_code == 200
    assert len(response.context['objects']) == 3
    for i in range(len(league)):
        assert league[i] in response.context['objects']


@pytest.mark.django_db
def test_team(client, user, team):
    client.login(username='paulina', password='ad')
    response = client.get('/footballscore/teams/')
    assert response.status_code == 200
    assert len(response.context['objects']) == 2
    for i in range(len(team)):
        assert team[i] in response.context['objects']


@pytest.mark.django_db
def test_season_create(client, user, season):
    client.login(username='paulina', password='ad')
    response = client.get('/footballscore/add_season/')
    assert response.status_code == 200
    assert season.season == "2019/2020"
    assert season.league.name == 'La Liga'


@pytest.mark.django_db
def test_search_league(client):
    response = client.get('/footballscore/search_league/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_detail_league(client, league):
    response = client.get(f'/footballscore/detail_league/{league[0].pk}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_search_teams(client):
    response = client.get('/footballscore/search_teams/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_detail_team(client, team):
    response = client.get(f'/footballscore/detail_team/{team[0].pk}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_search_match(client):
    response = client.get('/footballscore/search_match/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_league(client, user):
    client.login(username='paulina', password='ad')
    response = client.get('/footballscore/add_league/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_league(client, user, league):
    client.login(username='paulina', password='ad')
    response = client.get(f'/footballscore/edit_league/{league[0].pk}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_league(client, user, league):
    client.login(username='paulina', password='ad')
    response = client.get(f'/footballscore/delete_league/{league[0].pk}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_team(client, user):
    client.login(username='paulina', password='ad')
    response = client.get('/footballscore/add_team/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_team(client, user, team):
    client.login(username='paulina', password='ad')
    response = client.get(f'/footballscore/edit_team/{team[0].pk}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_team(client, user, team):
    client.login(username='paulina', password='ad')
    response = client.get(f'/footballscore/delete_team/{team[0].pk}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_match(client, user):
    client.login(username='paulina', password='ad')
    response = client.get('/footballscore/add_match/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_match(client, user, match):
    client.login(username='paulina', password='ad')
    response = client.get(f'/footballscore/edit_match/{match.pk}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_match(client, user, match):
    client.login(username='paulina', password='ad')
    response = client.get(f'/footballscore/delete_match/{match.pk}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_edit_season(client, user, season):
    client.login(username='paulina', password='ad')
    response = client.get(f'/footballscore/edit_season/{season.pk}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_season(client, user, season):
    client.login(username='paulina', password='ad')
    response = client.get(f'/footballscore/delete_season/{season.pk}/')
    assert response.status_code == 200
