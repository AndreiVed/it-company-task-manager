from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task_manager.forms import (
    WorkerCreateForm,
    WorkerUpdateForm,
    WorkerSearchForm, ProjectSearchForm,
)

from task_manager.models import (
    Worker,
    Task,
    Project,
    Team,
    Position,
    TaskType,
)


# Create your views here.
@login_required
def index(request):
    """View function for the home page of the site."""

    num_workers = Worker.objects.count()
    num_tasks = Task.objects.count()
    num_projects = Project.objects.count()
    num_teams = Team.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_workers": num_workers,
        "num_tasks": num_tasks,
        "num_projects": num_projects,
        "num_teams": num_teams,
        "num_visits": num_visits + 1,
    }

    return render(request, "task_manager/index.html", context=context)


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    paginate = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(WorkerListView, self).get_context_data(**kwargs)
        username = self.request.GET.get("username", )
        context["search_form"] = WorkerSearchForm(
            initial={"username": username}
        )
        return context

    def get_queryset(self):
        queryset = Worker.objects.select_related("position")
        form = WorkerSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(username__icontains=form.cleaned_data["username"])
        return queryset


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    queryset = Worker.objects.all().prefetch_related("tasks")


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreateForm
    success_url = reverse_lazy("task_manager:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdateForm
    success_url = reverse_lazy("task_manager:worker-list")


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker
    success_url = reverse_lazy("task_manager:worker-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    paginate = 5


class TaskDetailView(LoginRequiredMixin, generic.ListView):
    pass


class PositionListView(LoginRequiredMixin, generic.ListView):
    model = Position
    paginate = 5


class PositionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:position-list")


class PositionUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("task_manager:position-list")


class PositionDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Position
    success_url = reverse_lazy("task_manager:position-list")


class TaskTypeListView(LoginRequiredMixin, generic.ListView):
    model = TaskType
    template_name = "task_manager/task_type_list.html"
    context_object_name = "task_type_list"
    paginate = 5


class TaskTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = TaskType
    fields = "__all__"
    template_name = "task_manager/task_type_form.html"
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskTypeUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TaskType
    fields = "__all__"
    template_name = "task_manager/task_type_form.html"
    success_url = reverse_lazy("task_manager:task-type-list")


class TaskTypeDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TaskType
    template_name = "task_manager/task_type_confirm_delete.html"
    success_url = reverse_lazy("task_manager:task-type-list")


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    paginate = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProjectListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", )
        context["search_form"] = ProjectSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Project.objects.all()
        form = ProjectSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project
    queryset = Project.objects.all()


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("task_manager:project-list")


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("task_manager:project-list")


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("task_manager:project-list")


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team
    paginate = 5


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team
    queryset = Team.objects.all()


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("task_manager:team-list")


class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team
    fields = "__all__"
    success_url = reverse_lazy("task_manager:team-list")


class TeamDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Team
    success_url = reverse_lazy("task_manager:team-list")