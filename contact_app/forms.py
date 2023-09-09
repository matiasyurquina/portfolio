from django import forms
from contact_app.models import contact_model

from captcha.fields import ReCaptchaField
from django import forms

class contact_form(forms.ModelForm):
    captcha = ReCaptchaField()
    mail = forms.EmailField()
    class Meta:
        model = contact_model
        fields = ['name', 'mail', 'subject', 'message', 'captcha']