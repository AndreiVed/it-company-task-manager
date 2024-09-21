from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from task_manager.models import Position, Team


class AdminSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="testadmin"
        )
        self.client.force_login(self.admin_user)
        self.position = Position.objects.create(
            name="test_position",
        )

        self.team = Team.objects.create(
            name="test_team",
        )
        self.worker = get_user_model().objects.create_user(
            username="user",
            password="testuser",
            position=self.position,
            team=self.team
        )

    def test_worker_position_and_team_listed(self):
        url = reverse("admin:task_manager_worker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)
        self.assertContains(res, self.worker.team)

    def test_worker_detail_license_number_listed(self):
        url = reverse("admin:task_manager_worker_change", args=[self.worker.id])
        res = self.client.get(url)
        self.assertContains(res, self.worker.position)
        self.assertContains(res, self.worker.team)
