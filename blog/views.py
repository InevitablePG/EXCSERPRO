from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


class PostListView(ListView):
	model = Post
	template_name = 'blog/post_list.html'  # <app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']



class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Post
	fields = ['thumbnail', 'title', 'caption']
	template_name = 'blog/new_post.html'
	success_url = '/blog'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
	    return self.request.user.is_superuser


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['thumbnail', 'title', 'caption']
    template_name = 'blog/new_post.html'
    success_url = '/blog'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog'

    def test_func(self):
        return self.request.user.is_superuser