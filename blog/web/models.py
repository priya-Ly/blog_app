from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
STATUS=(
    (0,'DRAFT'),
    (1,'PUBLISH')
)
class Post(models.Model):
    title=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')
    updated_on=models.DateTimeField(auto_now=True)
    content=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    status=models.IntegerField(choices=STATUS,default=0)
class Meta:
    ordering=['-created_on']
def __str__(self):
    return self.title

class BlogPost(models.Model):
    blog_title=models.CharField(max_length=200)
    blog_content=RichTextField()
    publish_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog_title