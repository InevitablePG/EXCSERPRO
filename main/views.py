from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Testimonial
from .forms import CommentForm


def home(request):
	return render(request, 'main/home.html', {'title': 'EXCSERPRO: Excellent Service Provider'})


def about(request):
	return render(request, 'main/about.html', {'title': 'EXCSERPRO: About Us'})


def services(request):
	return render(request, 'main/services.html', {'title': 'EXCSERPRO: Our Services'})


def gallery(request):
	return render(request, 'main/gallery.html', {'title': 'EXCSERPRO: Gallery'})


def testimonals(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Your Review has been posted!')
			return redirect('Testimonals')
	else:
		form = CommentForm(request.POST)
	context = {
	    'title': 'EXCSERPRO: Testimonals',
	    'form': form,
	    'testimonals': Testimonial.objects.all()
	}
	return render(request, 'main/testimonals.html', context)


def contact(request):
	return render(request, 'main/contact.html', {'title': 'EXCSERPRO: Contact Us'})