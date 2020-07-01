import tempfile
from random import choice
from faker import Faker

from footballscore_app.models import Team, Match


faker = Faker("pl_PL")


def get_test_image_file():
    from django.core.files.images import ImageFile
    file = tempfile.NamedTemporaryFile(suffix='.png')
    return ImageFile(file, name=file.name)


def random_Team():
    """Return a random Team object from db."""
    team = Team.objects.all()
    return choice(team)


def fake_match_data():
    """Generate a dict of match data

    """
    match_data = {
        "team_home": random_Team().name,
        "team_away": random_Team().name,
        "date": (faker.date()),
        "score_home": int(faker.randint(1, 100)),
        "score_away": int(faker.randint(1, 100))
    }
    return match_data


def find_team_by_name(name):
    """Return the first `Team` object that matches `name`."""
    return Team.objects.filter(name=name).first()


def create_fake_match():
    """Generate new fake match and save to database."""
    match_data = fake_match_data()
    Match.objects.create(**match_data)


