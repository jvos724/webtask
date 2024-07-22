from django.shortcuts import render

from .models import Project


def main_view(request):
    projects = Project.objects.all().prefetch_related("tasks__tags")
    context = {"projects": projects}
    return render(request, "tasks/main_template.html", context)
