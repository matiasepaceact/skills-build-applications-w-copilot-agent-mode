from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        marvel_members = ['Iron Man', 'Spider-Man', 'Captain America']
        dc_members = ['Superman', 'Batman', 'Wonder Woman']

        marvel_team = Team.objects.create(name='marvel', members=marvel_members)
        dc_team = Team.objects.create(name='dc', members=dc_members)

        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel'),
            User.objects.create(email='superman@dc.com', name='Superman', team='dc'),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc'),
        ]

        Activity.objects.create(user='Iron Man', type='run', duration=30, date='2026-02-26')
        Activity.objects.create(user='Spider-Man', type='cycle', duration=45, date='2026-02-25')
        Activity.objects.create(user='Superman', type='swim', duration=60, date='2026-02-24')
        Activity.objects.create(user='Batman', type='walk', duration=20, date='2026-02-23')

        Leaderboard.objects.create(team='marvel', points=150)
        Leaderboard.objects.create(team='dc', points=120)

        Workout.objects.create(user='Iron Man', suggestion='Push-ups', date='2026-02-26')
        Workout.objects.create(user='Batman', suggestion='Sit-ups', date='2026-02-26')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
