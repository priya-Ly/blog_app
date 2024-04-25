from django.shortcuts import render
from .models import Post,BlogPost
from django.http import HttpResponse
from .forms import BlogPostForm
from django.views import generic
# Create your views here.
class PostList(generic.ListView):
    queryset=Post.objects.filter(status=1).order_by('-created_on')
    template_name='index.html'
class PostDetail(generic.DetailView):
    model=Post
    template_name='post_detail.html'

# def create_blog_post(request):
#     if request.method == 'POST':
#         form=BlogPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('New blog successfully added')
#         else:
#             form=BlogPostForm()
#             context={
#                 "form":form
#             }
#         return render(request,'home.html',context)

# def blog_list(request):
#     blog_list=BlogPost.objects.all()
#     return render(request,'blog_list.html',{'blogs':blog_list})
# def blog_view(request,blog_id):
#     blog_view=BlogPost.objects.filter(id=blog_id)
#     return render(request,'blog_view.html',{'blog':blog_view})

class CreateBlogPost(generic.CreateView):
    model=BlogPost
    form_class = BlogPostForm
    template_name = 'home.html'
    success_url= '/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class BlogListView(generic.ListView):
    model=BlogPost
    template_name='blog_list.html'
    context_object_name='blogs'

class BlogDetailView(generic.DetailView):
    model=BlogPost
    template_name='blog_view.html'
    context_object_name='blog'
