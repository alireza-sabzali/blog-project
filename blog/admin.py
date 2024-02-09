from django.contrib import admin
from blog.models import Post, Comments, Entry

admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Entry)
