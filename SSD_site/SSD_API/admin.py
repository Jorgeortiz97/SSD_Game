from django.contrib import admin

# Register your models here.
from .models import User, Submission

admin.site.register(User)
admin.site.register(Submission)