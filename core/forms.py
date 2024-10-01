from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(
        label="Il tuo indirizzo email",
        error_messages={"required": "Per favore, digita il tuo indirizzo email"},
    )
    content = forms.CharField(
        label="Il tuo messaggio",
        max_length=1000,
        error_messages={"required": "Per favore, digita il tuo messaggio"},
        widget=forms.Textarea,
    )
