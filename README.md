# FootballScore

**Final project - Coders Lab Back-End Developer: Python course.**


**Solution:**
a browser application that allows:

-> displaying information about matches played on a given day,

-> adding, modifying and deleting leagues,

-> league search,

-> adding, modifying and removing teams,

-> team search,

-> adding a match and its result,

-> displaying completed matches of the given team,

-> displaying future matches of the given team,

-> displaying the current table in the league.

The project will also include:

- authentication and login (all display options will be publicly available, adding and modifying data after logging in).


**Technology:**
- Python
- Django
- HTML5 and CSS3
- Bootstrap
- PostgreSQL databases
- Pytest


**Data structure:**

Description of the meaning of individual tables and columns:

**country:** model containing countries

-id: primary key of the table,
  
-name: name of the country,

-flag: image flag of the country,

**league:** model containing information about leagues.

-id: primary key of the table,

-name: league name,

-description: league description,

-hierarchy: league hierarchy in a given country,

-country: ForeignKey(Country)

**season:** model containing information about season.

-id: primary key of the table,

-season: season (exp. 2019/2020),

-league: ForeignKey(League),

**team:** model containing teams

-id: primary key of the table,

-name: team name,

-description: team description,

-coach: trainer,

-arms: image of team crest

-address: stadium address

-played_in_match: ManyToMany(Season, through='TeamSeason')

**TeamSeason:** intermediate model 

-team: ForeignKey(Team)

-season: ForeignKey(Season)

-points: team points in season

-wins: team wins in season

-draws: team draws in season

-losses: team losses in season


**match:** model containing information about matches

-team_home: host team - ForeignKey(TeamSeason)

-team_away: guest team - ForeignKey(TeamSeason)

-score_home: home team goals

-score_away: away team goals

-date: date of the meeting

**Landing page**
![landing](https://drive.google.com/file/d/1N1enc19__fXZn3dyz1SxW8c4-Yxz3eng/view?usp=sharing)