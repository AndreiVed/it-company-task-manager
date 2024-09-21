from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.test import TestCase

from task_manager.forms import WorkerCreateForm, WorkerSearchForm, ProjectSearchForm, TaskSearchForm, TaskForm
from task_manager.models import Position, Team, Worker, Project, Task, TaskType


class WorkerFormTests(TestCase):
    def test_driver_creation_form(self):
        position = Position.objects.create(
            name="developer"
        )
        team = Team.objects.create(
            name="team1"
        )
        form_data = {
            "username": "username",
            "password1": "user12test",
            "password2": "user12test",
            "first_name": "user_first_name",
            "last_name": "user_last_name",
            "email": "test@email.com",
            "set_usable_password": True,
            "position": position,
            "team": team,
        }

        form = WorkerCreateForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class WorkerSearchFormTest(TestCase):
    def setUp(self):
        self.worker1 = get_user_model().objects.create_user(
            username="johnsmith",
        )
        self.worker2 = get_user_model().objects.create_user(
            username="tylerderden",
        )
        self.worker3 = get_user_model().objects.create_user(
            username="tyleranderson",
        )

    def test_worker_search_form_single(self):
        form_data = {"username": "john"}
        form = WorkerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        filtered_data = Worker.objects.filter(
            username__icontains=form.cleaned_data["username"]
        )
        self.assertEqual(filtered_data.count(), 1)
        self.assertEqual(filtered_data.first(), self.worker1)

    def test_worker_search_form_two(self):
        form_data = {"username": "tyler"}
        form = WorkerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        filtered_data = Worker.objects.filter(
            username__icontains=form.cleaned_data["username"]
        )
        self.assertEqual(filtered_data.count(), 2)
        self.assertNotIn(self.worker1, filtered_data)
        self.assertIn(self.worker2, filtered_data)
        self.assertIn(self.worker3, filtered_data)

    def test_worker_search_form_not_exist(self):
        form_data = {"username": "nobody"}
        form = WorkerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        filtered_data = Worker.objects.filter(
            username__icontains=form.cleaned_data["username"]
        )
        self.assertEqual(filtered_data.count(), 0)

    def test_worker_search_form_empty(self):
        form_data = {"username": ""}
        form = WorkerSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        filtered_data = Worker.objects.filter(
            username__icontains=form.cleaned_data["username"]
        )
        self.assertEqual(filtered_data.count(), 3)


class ProjectSearchFormTest(TestCase):
    def setUp(self):
        self.project1 = Project.objects.create(
            name="project 1",
        )
        self.project2 = Project.objects.create(
            name="project 2",
        )
        self.project3 = Project.objects.create(
            name="project 13",
        )

    def test_worker_search_form_single(self):
        form_data = {"name": "2"}
        form = ProjectSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        filtered_data = Project.objects.filter(
            name__icontains=form.cleaned_data["name"]
        )
        self.assertEqual(filtered_data.count(), 1)
        self.assertEqual(filtered_data.first(), self.project2)

    def test_worker_search_form_two(self):
        form_data = {"name": "1"}
        form = ProjectSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        filtered_data = Project.objects.filter(
            name__icontains=form.cleaned_data["name"]
        )
        self.assertEqual(filtered_data.count(), 2)
        self.assertNotIn(self.project2, filtered_data)
        self.assertIn(self.project1, filtered_data)
        self.assertIn(self.project3, filtered_data)

    def test_worker_search_form_not_exist(self):
        form_data = {"name": "0"}
        form = ProjectSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        filtered_data = Project.objects.filter(
            name__icontains=form.cleaned_data["name"]
        )
        self.assertEqual(filtered_data.count(), 0)

    def test_worker_search_form_empty(self):
        form_data = {"name": ""}
        form = ProjectSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        filtered_data = Project.objects.filter(
            name__icontains=form.cleaned_data["name"]
        )
        self.assertEqual(filtered_data.count(), 3)


class TaskSearchFormTest(TestCase):
    def setUp(self):
        self.task_type=TaskType.objects.create(
            name="QA"
        )

        self.project = Project.objects.create(
            name="test_project"
        )
        self.task1 = Task.objects.create(
            name="task 1",
            deadline=datetime.now() + timedelta(days=2),
            is_completed=False,
            priority="high",
            task_type=self.task_type,
            project=self.project,
        )
        self.task2 = Task.objects.create(
            name="task 2",
            deadline=datetime.now() + timedelta(days=2),
            is_completed=False,
            priority="high",
            task_type=self.task_type,
            project=self.project,
        )
        self.task3 = Task.objects.create(
            name="task 13",
            deadline=datetime.now() + timedelta(days=2),
            is_completed=False,
            priority="high",
            task_type=self.task_type,
            project=self.project,
        )

    def test_worker_search_form_single(self):
        form_data = {"name": "2"}
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        filtered_data = Task.objects.filter(
            name__icontains=form.cleaned_data["name"]
        )
        self.assertEqual(filtered_data.count(), 1)
        self.assertEqual(filtered_data.first(), self.task2)

    def test_worker_search_form_two(self):
        form_data = {"name": "1"}
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        filtered_data = Task.objects.filter(
            name__icontains=form.cleaned_data["name"]
        )
        self.assertEqual(filtered_data.count(), 2)
        self.assertNotIn(self.task2, filtered_data)
        self.assertIn(self.task1, filtered_data)
        self.assertIn(self.task3, filtered_data)

    def test_worker_search_form_not_exist(self):
        form_data = {"name": "0"}
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        filtered_data = Task.objects.filter(
            name__icontains=form.cleaned_data["name"]
        )
        self.assertEqual(filtered_data.count(), 0)

    def test_worker_search_form_empty(self):
        form_data = {"name": ""}
        form = TaskSearchForm(data=form_data)
        self.assertTrue(form.is_valid())
        filtered_data = Task.objects.filter(
            name__icontains=form.cleaned_data["name"]
        )
        self.assertEqual(filtered_data.count(), 3)


class TaskDeadlineValidationTest(TestCase):
    def test_deadline_in_past(self):
        form_data = {"deadline": datetime.now() - timedelta(days=2)}
        error_message = "The deadline must be a date in the future."
        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["deadline"], [error_message])
