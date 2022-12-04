from django import forms


class ContactForm(forms.Form):
    """
    Contact form
    """
    name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)
    content = forms.CharField(widget=forms.Textarea)
