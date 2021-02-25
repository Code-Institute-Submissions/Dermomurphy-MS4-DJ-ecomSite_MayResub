from django.contrib import admin
from .models import Posts
# Register your models here.
class PostsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'body',
        'image',
        'created_on',
        
    )
    
    ordering = ('created_on',)



admin.site.register(Posts, PostsAdmin)




