from crispy_forms.helper import FormHelper
from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3


class DaisyUiTextArea(forms.Textarea):
    pass


class DaisyUiTextInput(forms.TextInput):
    pass


class DaisyUiEmailInput(forms.EmailInput):
    pass


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label="Il tuo nome",
        error_messages={
            "required": "Per favore, digita il tuo nome",
            "max_length": "Nome troppo lungo (max 100 caratteri)",
        },
        widget=DaisyUiTextInput(attrs={"class": "input input-bordered w-full"}),
    )
    email = forms.EmailField(
        label="Il tuo indirizzo email",
        error_messages={"required": "Per favore, digita il tuo indirizzo email"},
        widget=DaisyUiEmailInput(attrs={"class": "input input-bordered w-full"}),
    )
    message = forms.CharField(
        label="Il tuo messaggio",
        max_length=1000,
        error_messages={
            "required": "Per favore, digita il tuo messaggio",
            "max_length": "Messaggio troppo lungo (max 1000 caratteri)",
        },
        widget=DaisyUiTextArea(attrs={"class": "textarea textarea-bordered w-full"}),
    )
    captcha = ReCaptchaField(
        label=False,
        widget=ReCaptchaV3(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.disable_csrf = True
        self.helper.label_class = "block text-base-content text-sm font-semibold mb-2"
