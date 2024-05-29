from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin # text editor
from newspaper.models import (
    Category, 
    Contact, 
    Newsletter, 
    Post, 
    Tag, 
    UserProfile, 
    Comment,
)

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Newsletter)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    date_hierarchy = 'published_at'
    list_display = ['title', 'published_at', 'author']

admin.site.register(Post, PostAdmin)
