from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']




class CustomContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    # You can add custom validation for specific fields
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name.isalpha():
            raise forms.ValidationError("Name should only contain alphabetic characters.")
        return name
