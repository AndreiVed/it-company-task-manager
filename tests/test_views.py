from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from task_manager.models import Worker, Task, TaskType, Project

WORKER_URL = reverse("task_manager:worker-list")
TASK_URL = reverse("task_manager:task-list")


class PublicWorkerTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Test",
            password="test123",
        )

    def test_login_required_for_worker_list(self):
        res = self.client.get(WORKER_URL)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_for_driver_detail(self):
        res = self.client.get(reverse(
            "task_manager:worker-detail",
            args=[self.user.id])
        )
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_for_worker_update(self):
        res = self.client.get(reverse(
            "task_manager:worker-update",
            args=[self.user.id])
        )
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_for_driver_delete(self):
        res = self.client.get(reverse(
            "task_manager:worker-delete",
            args=[self.user.id])
        )
        self.assertNotEqual(res.status_code, 200)


class PrivateWorkerTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Test",
            password="test123",
        )
        self.client.force_login(self.user)

    def test_retrieve_workers(self):
        get_user_model().objects.create_user(
            username="Test1",
            password="test1231",
        )
        get_user_model().objects.create_user(
            username="Test2",
            password="test1232",
        )
        response = self.client.get(WORKER_URL)
        self.assertEqual(response.status_code, 200)
        worker_list = Worker.objects.all()
        self.assertEqual(
            list(response.context["worker_list"]),
            list(worker_list),
        )
        self.assertTemplateUsed(response, "task_manager/worker_list.html")


class TaskTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Test",
            password="test123",
        )
        self.client.force_login(self.user)
        self.task_type = TaskType.objects.create(
            name="QA"
        )

        self.project = Project.objects.create(
            name="test_project"
        )

        self.task_high_priority = Task.objects.create(
            name="task1",
            description="some description",
            deadline=datetime.now() + timedelta(days=2),
            is_completed=False,
            priority="high",
            task_type=self.task_type,
            project=self.project,
        )

        self.task_medium_priority = Task.objects.create(
            name="task2",
            description="some description",
            deadline=datetime.now() + timedelta(days=2),
            is_completed=False,
            priority="medium",
            task_type=self.task_type,
            project=self.project,
        )

        self.task_low_priority = Task.objects.create(
            name="task3",
            description="some description",
            deadline=datetime.now() + timedelta(days=2),
            is_completed=False,
            priority="low",
            task_type=self.task_type,
            project=self.project,
        )

        self.task_completed = Task.objects.create(
            name="task4",
            description="some description",
            deadline=datetime.now() + timedelta(days=2),
            is_completed=True,
            priority="low",
            task_type=self.task_type,
            project=self.project,
        )

        self.task_failed = Task.objects.create(
            name="task5",
            description="some description",
            deadline=datetime.now() - timedelta(days=2),
            is_completed=False,
            priority="low",
            task_type=self.task_type,
            project=self.project,
        )

    def handle_test_task_sorting(self, response):
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["high_priority"]),
            [self.task_high_priority],
        )
        self.assertEqual(
            list(response.context["medium_priority"]),
            [self.task_medium_priority],
        )
        self.assertEqual(
            list(response.context["low_priority"]),
            [self.task_low_priority],
        )
        self.assertEqual(
            list(response.context["completed"]),
            [self.task_completed],
        )
        self.assertEqual(
            list(response.context["failed"]),
            [self.task_failed],
        )

    def test_task_list_sorting(self):
        response = self.client.get(reverse("task_manager:task-list"))
        self.handle_test_task_sorting(response)

    def test_project_detail_task_sorting(self):
        response = self.client.get(
            reverse(
                "task_manager:project-detail",
                kwargs={"pk": self.project.id}
            )
        )
        self.handle_test_task_sorting(response)

    def test_task_completed_view(self):
        self.assertFalse(self.task_high_priority.is_completed)

        self.client.post(
            reverse(
                "task_manager:task-completed",
                args=[self.task_high_priority.id]
            )
        )
        self.task_high_priority.refresh_from_db()
        self.assertTrue(self.task_high_priority.is_completed)
