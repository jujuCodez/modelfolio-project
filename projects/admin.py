from django.contrib import admin

# Register your models here.
from .models import Project, About

admin.site.register(Project)
admin.site.register(About)