from django.shortcuts import render, get_object_or_404
from .models import Contact, Photo, Topic, Project, Description


# put the column number here
topic_column_number = 3
image_column_number = 5
project_column_number = 3


def index(request):
    return render(request, 'mysite/index.html')


def portfolio(request):
    projects = Project.objects.all()
    list_of_projects = []
    j = 0
    entry = []
    for t in projects:
        j += 1
        entry.append(t)
        if (j % project_column_number) == 0:
            list_of_projects.append(entry)
            entry = []
            j = 0
    list_of_projects.append(entry)
    return render(request, 'mysite/portfolio.html', {'projects': projects, 'list_of_projects': list_of_projects})
    # return render(request, 'mysite/portfolio.html')


def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'mysite/thank.html')
    else:
        return render(request, 'mysite/contact.html')


def travel(request):
    topics = Topic.objects.all()
    list_of_topics = []
    j = 0
    entry = []
    for t in topics:
        j += 1
        entry.append(t)
        if (j % topic_column_number) == 0:
            list_of_topics.append(entry)
            entry = []
            j = 0
    list_of_topics.append(entry)
    return render(request, 'mysite/travel.html', {'topics': topics, 'list_of_topics': list_of_topics})


def travelgallery(request, topic_name):
    topic = Topic.objects.get(name=topic_name)
    images = Topic.objects.get(name=topic_name).photo_set.all()
    list_of_images = []
    j = 0
    entry = []
    for i in images:
        j += 1
        entry.append(i)
        if (j % image_column_number) == 0:
            list_of_images.append(entry)
            entry = []
            j = 0
    list_of_images.append(entry)
    return render(request, 'mysite/travelGallery.html', {'topic': topic, 'images': images, 'list_of_images': list_of_images})


def traveldetails(request, topic_name, photo_id):
    photo = get_object_or_404(Photo, topic__name=topic_name, id=photo_id)
    return render(request, 'mysite/travelDetails.html', {'photo': photo})


def projectdescription(request, project_name):
    project = Project.objects.get(name=project_name)
    descriptions = Project.objects.get(name=project_name).description_set.all()
    list_of_descriptions = []
    j = 0
    entry = []
    for i in descriptions:
        j += 1
        entry.append(i)
        if (j % image_column_number) == 0:
            list_of_descriptions.append(entry)
            entry = []
            j = 0
    list_of_descriptions.append(entry)
    return render(request, 'mysite/projectDescription.html', {'project': project, 'descriptions': descriptions, 'list_of_descriptions': list_of_descriptions})


def projectdetails(request, project_name, description_id):
    description = get_object_or_404(Description, topic__name=project_name, id=description_id)
    return render(request, 'mysite/projectDescription.html', {'description': description})


