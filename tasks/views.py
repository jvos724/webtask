from django.shortcuts import render


def main_view(request):
    context = {}
    return render(request, "tasks/main_template.html", context)
