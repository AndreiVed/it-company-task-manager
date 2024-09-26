from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.models import Position, Team, Project


class ModelTests(TestCase):
    def setUp(self):
        self.position = Position.objects.create(
            name="test_position",
        )

        self.team = Team.objects.create(
            name="test_team",
        )

        self.worker = get_user_model().objects.create_user(
            username="user",
            password="test123",
            first_name="user_first_name",
            last_name="user_last_name",
            position=self.position,
            team=self.team
        )

    def test_worker_str(self):
        self.assertEqual(
            str(self.worker),
            f"{self.worker.username} "
            f"({self.worker.first_name} {self.worker.last_name}) "
            f"- position: {self.worker.position} - team: {self.worker.team}"
        )
