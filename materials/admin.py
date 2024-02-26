from django.contrib import admin

from materials.models import Course, Lesson
from users.models import User


admin.site.register(Course)

admin.site.register(Lesson)