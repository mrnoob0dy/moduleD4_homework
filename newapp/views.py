from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import PostFilter
from .forms import NewsForm



class PostsList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-id')
    paginate_by = 10


class PostList(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


class Search(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'filter'
    queryset = Post.objects.order_by('-id')
    paginate_by = 1


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context
    

class PostsCreateView(CreateView):
    template_name = 'posts_create.html'
    form_class = NewsForm


class PostsUpdateView(UpdateView):
    template_name = 'posts_create.html'
    form_class = NewsForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
    


class PostsDeleteView(DeleteView):
    template_name = 'posts_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'
