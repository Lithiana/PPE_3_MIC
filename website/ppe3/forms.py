from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

class ClientForm(forms.Form):
    civilite = forms.ChoiceField(choices=(('M', 'M'), ('Mme', 'Mme')))
    nom = forms.CharField(required=True)
    prenom = forms.CharField(required=True)
    tel = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    adresse = forms.CharField(required=True)
    code_postal = forms.CharField(required=True)
    ville = forms.CharField(required=True)
    pays = forms.CharField(required=True)