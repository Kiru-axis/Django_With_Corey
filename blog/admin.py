from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ("title","date_posted","author",)
admin.site.register(Post,PostAdmin)
