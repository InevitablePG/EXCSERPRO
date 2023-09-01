from django import forms
from .models import Testimonial
from captcha.fields import ReCaptchaField


class BookingForm(forms.Form):
    ISSUE_CHOICES = [
        ('', ''),
        ('Starter Repair', 'Starter Repair'),
        ('Alternator Repairs', 'Alternator Repairs'),
        ('Wiring & Rewinding', 'Wiring & Rewinding'),
        ('Auto Electrical Spares', 'Auto Electrical Spares'),
        ('Battery Testing & Charging', 'Battery Testing & Charging'),
        ('Car Service (Minor/Major)', 'Car Service (Minor/Major)'),
        ('Engine Overhaul', 'Engine Overhaul'),
        ('Gearbox Repairs', 'Gearbox Repairs'),
        ('Clutch Repairs', 'Clutch Repairs'),
        ('Suspension Repairs', 'Suspension Repairs'),
        ('Car Diagnosis', 'Car Diagnosis')
    ]
    
    full_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'First and Last Name'}))
    email = forms.EmailField(max_length=100, required=False, widget=forms.EmailInput(attrs={'placeholder': 'example@example.com'}))
    phone_number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    issues = forms.ChoiceField(choices=ISSUE_CHOICES, required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message here', 'rows': 4}))
    captcha = ReCaptchaField()



class CommentForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['city', 'text']