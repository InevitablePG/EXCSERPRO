from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Testimonial, Gallery
from .forms import CommentForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


def home(request):
	return render(request, 'main/home.html', {'title': 'EXCSERPRO: Excellent Service Provider'})


def about(request):
	return render(request, 'main/about.html', {'title': 'EXCSERPRO: About Us'})


def services(request):
	return render(request, 'main/services.html', {'title': 'EXCSERPRO: Our Services'})


class GalleryListView(ListView):
	model = Gallery
	template_name = 'main/gallery.html'  # <app>/<model>_<viewtype>.html
	ordering = ['-date_posted']

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['title'] = 'EXCSERPRO: Gallery'
	    return context


class GalleryCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	model = Gallery
	fields = ['image']
	template_name = 'blog/new_post.html'
	success_url = '/gallery'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
	    return self.request.user.is_staff


class GalleryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Gallery
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/gallery'

    def test_func(self):
        return self.request.user.is_staff


def testimonals(request):
	testimonals = Testimonial.objects.all().order_by('-date_posted')

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if not request.user.is_authenticated:
		    next_page = request.path
		    messages.info(request, f'Please login first, or register if you dont have an account.')
		    return redirect(f'/login/?next={next_page}')

		if form.is_valid():
		    testimonial = form.save(commit=False)
		    testimonial.author = request.user  # Assuming you are using the built-in authentication system
		    testimonial.save()
		    messages.success(request, f'Your comment has been posted!')
		    return redirect('Testimonals')
	else:
	    form = CommentForm()

	return render(request, 'main/testimonals.html', {'form': form, 'testimonals': testimonals})


def contact(request):
	return render(request, 'main/contact.html', {'title': 'EXCSERPRO: Contact Us'})