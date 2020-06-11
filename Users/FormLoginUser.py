from django import forms


class FormLoginUser(forms.Form):
    username = forms.CharField(required=True, label="INGRESE SU USUARIOS",
                               min_length=4, max_length=15,
                               widget=forms.TextInput(attrs={
                                   'class': 'form-control',
                                   'id': 'username',
                                   'type': 'text',
                                   'name': 'username',
                                   'placeholder': 'Admin'
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
