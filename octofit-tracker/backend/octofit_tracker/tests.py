from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name="Test Team")
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="pass", team=self.team)
        self.workout = Workout.objects.create(name="Cardio", description="Run 5km", suggested_for_team=self.team)
        self.activity = Activity.objects.create(user=self.user, type="run", duration=30, distance=5.0)
        self.leaderboard = Leaderboard.objects.create(user=self.user, points=100)

    def test_team_str(self):
        self.assertEqual(str(self.team), "Test Team")

    def test_user_team(self):
        self.assertEqual(self.user.team, self.team)

    def test_activity_user(self):
        self.assertEqual(self.activity.user, self.user)

    def test_workout_team(self):
        self.assertEqual(self.workout.suggested_for_team, self.team)

    def test_leaderboard_points(self):
        self.assertEqual(self.leaderboard.points, 100)
