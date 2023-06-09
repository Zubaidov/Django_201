from django.views.generic import ListView, DetailView
from .models import Post

class HomePageView(ListView):
    http_method_names = ["get"]
    template_name = "index.html"
    model = Post
    context_object_name = "posts"
    queryset = Post.objects.all().order_by('id')[0:30]

class PostDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "detail.html"
    model = Post
    context_object_name = "post {{ post }}"

