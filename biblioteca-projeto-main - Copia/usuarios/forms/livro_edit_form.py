from django import forms
from bibliotech.models import Book
from utils.django_forms import add_attr

class AuthorLivroForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        
    class Meta:
        model = Book
        fields = 'title', 'description', 'cover', 'quantidade', 'emprestado', 'category', 'author'
        widgets = {
            'cover': forms.FileInput(
                attrs= {
                    'class': 'span-2'
                }
            )
        }
