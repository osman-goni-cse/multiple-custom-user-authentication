from django.contrib import admin
from .models import NewCircular, JobPost, Memorandum

# Register your models here.

admin.site.register(NewCircular)
admin.site.register(Memorandum)
admin.site.register(JobPost)
