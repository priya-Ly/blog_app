from .import views
from django.urls import path


urlpatterns=[
    path('',views.PostList.as_view(),name='home'),
    path('blogs/',views.BlogListView.as_view(),name='blog_list'),
    path('create/',views.CreateBlogPost.as_view(),name='create_blog_post'),
    path('blogs/<int:pk>',views.BlogDetailView.as_view(),name='blog_view'),
    path('<slug:slug>/',views.PostDetail.as_view(),name='post_detail'),

]