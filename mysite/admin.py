from django.contrib import admin
from .models import Student, Contact
from .views import Photo, Topic, Project, Description

# Register your models here.


class PhotoInline(admin.TabularInline):
    fieldsets = [
        ('Basic Info', {'fields': ['description']}),
        ('Upload Image', {'fields': ['image']})
    ]
    model = Photo
    extra = 3


class TopicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [PhotoInline]


class ProjectDescriptionInline(admin.TabularInline):
    fieldsets = [
        ('Basic Info', {'fields': ['description']}),
        ('Upload Image', {'fields': ['image']})
    ]
    model = Description
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
    ]
    inlines = [ProjectDescriptionInline]


admin.site.register(Topic, TopicAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Student)
admin.site.register(Contact)