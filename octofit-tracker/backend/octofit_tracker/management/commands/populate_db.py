from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create Users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Thor', email='thor@marvel.com', team=marvel),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date='2026-03-04')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=400, date='2026-03-03')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, calories=500, date='2026-03-02')
        Activity.objects.create(user=users[3], type='Yoga', duration=40, calories=200, date='2026-03-01')
        Activity.objects.create(user=users[4], type='Boxing', duration=50, calories=450, date='2026-02-28')
        Activity.objects.create(user=users[5], type='Pilates', duration=35, calories=250, date='2026-02-28')

        # Create Workouts
        Workout.objects.create(name='Push Ups', description='Upper body workout', suggested_for='All')
        Workout.objects.create(name='Squats', description='Lower body workout', suggested_for='All')
        Workout.objects.create(name='Plank', description='Core workout', suggested_for='All')

        # Create Leaderboard
        Leaderboard.objects.create(team=marvel, points=1200)
        Leaderboard.objects.create(team=dc, points=1100)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully!'))
