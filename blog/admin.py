from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin): 
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author') 
    search_fields = ('title', 'body') 
    prepopulated_fields = {'slug': ('title',)} 
    raw_id_fields = ('author',) 
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
    
#The list_display attribute allows you to set the fields of your model that you want to display in the admin object list page. 
#The @admin.register() decorator performs the same function as the admin.site.register() function we have replaced, registering the ModelAdmin class that it decorates.