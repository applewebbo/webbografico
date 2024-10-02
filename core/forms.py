from crispy_forms.helper import FormHelper
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Il tuo nome",
        error_messages={
            "required": "Per favore, digita il tuo nome",
            "max_length": "Nome troppo lungo (max 100 caratteri)",
        },
    )
    email = forms.EmailField(
        label="Il tuo indirizzo email",
        error_messages={"required": "Per favore, digita il tuo indirizzo email"},
    )
    message = forms.CharField(
        label="Il tuo messaggio",
        max_length=1000,
        error_messages={
            "required": "Per favore, digita il tuo messaggio",
            "max_length": "Messaggio troppo lungo (max 1000 caratteri)",
        },
        widget=forms.Textarea,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
