from django.contrib import admin

from profiles.models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    exclude = ('created_time', 'last_modified')
    list_display = ('owner', 'created_time', 'last_modified', 'content')


admin.site.register(Post, PostAdmin)
