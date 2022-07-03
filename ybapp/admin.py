from django.contrib import admin
from .models import Year, Student, TextMemories

# Register your models here.

admin.site.register(Year)
admin.site.register(Student)
admin.site.register(TextMemories)