from django import forms
from django.contrib.auth.models import User
from Alumns.models import Alumn


class RegisterUser(forms.Form):
    username = forms.CharField(required=True, label="INGRESE SU USUARIO",
                                min_length=4, max_length=15,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'username',
                                    'type': 'text',
                                    'name': 'username',
                                    'placeholder': 'Admin'
                                }))
    email = forms.EmailField(required=True, label="INGRESE SU CORREO",
                                  min_length=4, max_length=25,
                                  widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'email',
                                    'type': 'email',
                                    'name': 'email',
                                    'placeholder': 'correo@ejemplo.com'
                                  }))
    password = forms.CharField(required=True, label="INGRESE SU CONTRASEÑA",
                                         min_length=4, max_length=25,
                                         widget=forms.TextInput(attrs={
                                             'class': 'form-control',
                                             'id': 'password',
                                             'type': 'password',
                                             'name': 'password',
                                             'placeholder': 'Contraseña'
                                         }))
    password2 = forms.CharField(required=True, label="INGRESE NUEVAMENTE SU CONTRASEÑA",
                               min_length=4, max_length=25,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'id': 'password2',
                                   'type': 'password',
                                   'name': 'password2',
                                   'placeholder': 'Contraseña'
                               }))

    def veriry_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El usuario ya se encuentra registrado')
        return username
    def verify_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El correo ya se encuentra registrado')
        return email
    def verify_password(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', " La contraseña no coincide")
    def save(self):
        return User.objects.create_superuser(
            self.cleaned_data.get('username'),
            self.cleaned_data.get('email'),
            self.cleaned_data.get('password')
        )
