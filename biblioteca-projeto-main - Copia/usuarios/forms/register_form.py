
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from utils.django_forms import add_placeholder, senha_forte
    

class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Seu usuario')
        add_placeholder(self.fields['email'], 'Seu email')
        add_placeholder(self.fields['first_name'], 'Seu primeiro nome')
        add_placeholder(self.fields['last_name'], 'Seu ultimo nome')


    password = forms.CharField(
        required=True,
        widget = forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha'
        }),
        error_messages={
            'required': 'Senha não pode ser vazia'
        },
        help_text=(
            'Sua precisa precisa ter uma letra em maíscula, uma letra miníscula e um numero.'
            'É preciso conter 8 caracteres'
        ),
        validators=[senha_forte]
    )

    password2 = forms.CharField(
        required=True,
        widget = forms.PasswordInput(attrs={
            'placeholder': 'Repita sua senha'
        })
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

    labels = {
        'username': 'Digite seu usuarios',
        'first_name': 'Digite seu primeiro nome',
        'last_name': 'Digite seu segundo nome',
        'email': 'Digite seu email',
        'password': 'Digite sua senha',
    }
    help_texts = {
        'email': 'Digite um emial valido',
    }
    error_messages = {
        'username': {
            'required': 'Este campo nao pode ser vazio!',
            'max_leangth': 'Esse campo deve ter mais que 3 caracteres'
        }
    }
    widgets = {
        'username': forms.TextInput(attrs={
            'placeholder': 'Escreva seu usuario aqui',
             'class': 'input text-inhput outra classe'
            }),
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Escreva sua senha aqui'
            })
    }

    def clean_email(self):
        email = self.cleaned_data.get('email' , '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'Este email já existe, entre com outro',
                code='invalid',
            )

        return email


    # def clean_password(self):
    #     data = self.cleaned_data.get('password')

    #     if 'atenção' in data:
    #         raise ValidationError(
    #             'Não digite %(pipoca)s no campo de senha',
    #             code='invalid',
    #             params= {'pipoca': '"atenção"'}
    #         )
        
    #     return data

    # def clean_first_name(self):
    #     data = self.cleaned_data.get('first_name')

    #     if 'Eduardo' in data:
    #         raise ValidationError(
    #             'Não digite %(value)s no campo de nome',
    #             code = 'invalid',
    #             params= {'value': '"Eduardo"'}
    #         )
        
    #     return data
    

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2= cleaned_data.get('password2')

        if password != password2:
            password_error = 'Senha e senha2 devem ser iguais'

            raise ValidationError({
                'password': ValidationError(
                    password_error,
                    code='invalid'
                    ),
                'password2': [
                    password_error,
                    # ValidationError('Outro erro') ---> Para criar outro campo de erros
                ],
            })