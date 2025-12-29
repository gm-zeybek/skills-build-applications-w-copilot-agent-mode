from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete all data
        User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Create Teams
        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create_user(username='tony', email='tony@stark.com', password='ironman', first_name='Tony', last_name='Stark', team=marvel)
        steve = User.objects.create_user(username='steve', email='steve@rogers.com', password='captain', first_name='Steve', last_name='Rogers', team=marvel)
        bruce = User.objects.create_user(username='bruce', email='bruce@wayne.com', password='batman', first_name='Bruce', last_name='Wayne', team=dc)
        clark = User.objects.create_user(username='clark', email='clark@kent.com', password='superman', first_name='Clark', last_name='Kent', team=dc)

        # Create Activities
        octo_models.Activity.objects.create(user=tony, type='Run', duration=30, distance=5)
        octo_models.Activity.objects.create(user=steve, type='Swim', duration=45, distance=2)
        octo_models.Activity.objects.create(user=bruce, type='Cycle', duration=60, distance=20)
        octo_models.Activity.objects.create(user=clark, type='Run', duration=50, distance=10)

        # Create Workouts
        octo_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', suggested_for_team=marvel)
        octo_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes', suggested_for_team=dc)

        # Create Leaderboard
        octo_models.Leaderboard.objects.create(user=tony, points=100)
        octo_models.Leaderboard.objects.create(user=steve, points=90)
        octo_models.Leaderboard.objects.create(user=bruce, points=95)
        octo_models.Leaderboard.objects.create(user=clark, points=98)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
