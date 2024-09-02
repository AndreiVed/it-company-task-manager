from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from task_manager.models import Position, Worker, Team, TaskType, Task, Project


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]


@admin.register(Worker)
class WorkerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("position", "team", )
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("position", "team",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "position",
                        "team",
                    )
                },
            ),
        )

    search_fields = ["username",]
    list_filter = UserAdmin.list_filter + ("position", "team",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["name", "task_type", "description", "deadline", "is_completed",]
    search_fields = ["name", ]
    list_filter = ["name","task_type", "created_date", "is_completed"]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]
