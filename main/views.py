from django.shortcuts import render, redirect
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


def testimonals(request):
	testimonals = Testimonial.objects.all().order_by('-date_posted')

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if not request.user.is_authenticated:
		    next_page = request.path
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