from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .models import Testimonial, Gallery
from .forms import CommentForm, BookingForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def new_booking(context) -> None:
    subject = f"New Booking From {context['full_name']}"
    from_email = 'fullstack.python.dev@gmail.com'
    recipient_list = ['fullstack.python.dev@gmail.com']
    
    html_content = render_to_string('emails/book.html', context)
    
    text_content = strip_tags(html_content)
    
    email = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)

    email.attach_alternative(html_content, "text/html")

    email.send()



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
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            issues = form.cleaned_data['issues']
            message = form.cleaned_data['message']

            temp_context = {
                'full_name': full_name,
                'email': email,
                'phone_number': phone_number,
                'issues': issues,
                'message': message
            }
            new_booking(temp_context)
            messages.success(request, f'Thank you {full_name} for your booking request, we will get in touch with you shortly.')
            return redirect('Home')

        else:
            messages.info(request, 'Please fill in all the fields with \'*\' including the Capcha!')

    else:
        form = BookingForm()
        
    context = {
        'form': form,
        'title': 'EXCSERPRO: Contact Us'
    }
    return render(request, 'main/contact.html', context)