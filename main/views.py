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