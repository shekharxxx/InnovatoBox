from django.contrib import admin
from .models import Comment, Video_up,like

# Register your models here.
admin.site.register(Comment)
admin.site.register(Video_up)
admin.site.register(like)