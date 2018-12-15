from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=196)
    message = models.TextField()

    def __str__(self):
        return self.email


class Topic(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Photo(models.Model):
    description = models.CharField(max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mysite/static/gallery')

    def get_source(self):
        directory = self.image.name.split('/static/')
        return directory[1]

    def get_name(self):
        directory = self.image.name.split('/')
        return directory[-1]

    def __str__(self):
        return self.get_name()


class Project(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Description(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=1500)
    image = models.ImageField(upload_to='mysite/static/gallery')

    def get_source(self):
        directory = self.image.name.split('/static/')
        return directory[1]

    def get_name(self):
        directory = self.image.name.split('/')
        return directory[-1]

    def __str__(self):
        return self.get_name()


