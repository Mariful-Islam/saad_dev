import os
from django.conf import settings
from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Service, Project, Client, Partnership, Myprofile, Skill, Experience, ProjectStatstics
from django.core.mail import send_mail
# Create your views here.


def home(request):
    services = Service.objects.all()[0:3]
    projects = Project.objects.all()[0:3]
    clients = Client.objects.all()

    context = {'services': services, 'projects': projects, 'clients': clients}
    return render(request, 'index.html', context)


def service(request):
    services = Service.objects.all()

    context = {'services': services}
    return render(request, 'service.html', context)


def single_service(request, service_name):
    service = Service.objects.get(name=service_name)

    context = {'service': service}
    return render(request, 'single-service.html', context)


def project(request):
    projects = Project.objects.all()
    project_statstics = ProjectStatstics.objects.all()

    context = {'projects': projects, 'project_statstics': project_statstics}
    return render(request, 'project.html', context)


def single_project(request, project_name):
    project = Project.objects.get(name=project_name)

    context = {'project': project}
    return render(request, 'single-project.html', context)


def client(request):
    clients = Client.objects.all()

    partnerships = Partnership.objects.all()

    context = {'clients': clients, 'partnerships': partnerships}
    return render(request, 'client.html', context)


def about(request):
    myprofile = Myprofile.objects.get(id=1)
    skills = Skill.objects.all()
    experiences = Experience.objects.all()

    context = {'myprofile': myprofile,
               'skills': skills, 'experiences': experiences}
    return render(request, 'about.html', context)


def contact(request):
    if request.method == "POST":
        username = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        send_mail(
            username,
            message,
            email,
            ['mariful.shad.53@gmail.com'],
        )

        return render(request, 'contact.html')

    else:
        return render(request, 'contact.html')


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="applicaation/adminupload")
            response['content-Disposition'] = 'inline;filename=' + \
                os.path.basename(file_path)
            return response

    raise Http404
