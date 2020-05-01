from django.contrib import admin

from .models import Question
from .models import Post

admin.site.register(Question)
admin.site.register(Post)
# Register your models here.
