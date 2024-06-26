from django.contrib import admin
from .models import Post,BlogPost,Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# class PostAdmin(admin.ModelAdmin):
#     list_display=('title','slug','status','created_on')
#     list_filter=('status',)
#     search_fields=['title','content']
#     prepopulated_fields={'slug':('title',)}
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
class CommentAdmin(admin.ModelAdmin):
    list_display=('name','body','post','created_on','active')
    list_filter=('active','created_on')
    search_fields=('name','email','body')
    actions=['approve_comments']

    def approve_comments(self,request,queryset):
        queryset.update(active=True)
admin.site.register(Post,PostAdmin)
admin.site.register(BlogPost)
admin.site.register(Comment,CommentAdmin)
