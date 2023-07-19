from django.shortcuts import render


def home(request):
	return render(request, 'main/home.html', {'title': 'EXCSERPRO: Excellent Service Provider'})


def about(request):
	return render(request, 'main/about.html', {'title': 'EXCSERPRO: About Us'})


def services(request):
	return render(request, 'main/services.html', {'title': 'EXCSERPRO: Our Services'})


def gallery(request):
	return render(request, 'main/gallery.html', {'title': 'EXCSERPRO: Gallery'})


def testimonals(request):
	return render(request, 'main/testimonals.html', {'title': 'EXCSERPRO: Testimonals'})


def contact(request):
	return render(request, 'main/contact.html', {'title': 'EXCSERPRO: Contact Us'})