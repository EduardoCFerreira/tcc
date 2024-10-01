from django import forms
from bibliotech.models import Book
from utils.django_forms import add_attr
from django.core.exceptions import ValidationError
from collections import defaultdict

class BookCreate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

    class Meta:
        model = Book
        fields = 'title', 'description', 'slug', 'cover', 'quantidade', 'category', 'author'

        def clean(self, *args, **kwargs):
            super_clean = super().clean(*args, **kwargs)
            cleaned_data = self.cleaned_data
            title = cleaned_data.get('title')
            quantidade = cleaned_data.get('quantidade')


            if len(title) == 0:
                self._my_errors['title'].append('O titulo não pode ficar vazio!')

            if quantidade == 0:
                self._my_errors['quantidade'].append('A quantidade não pode ficar vazia!')

                if self._my_errors:
                    raise ValidationError(self._my_errors)

            return super_clean
        
        def clean_title(self):
            title = self.cleaned_data.get('title')
            if len(title) == 0:
                self._my_errors['title'].append('O titulo não pode ficar vazio!')

            return title
        
        def clean_quantidade(self):
            quantidade = self.cleaned_data.get('quantidade')
            if quantidade == 0:
                self._my_errors['quantidade'].append('A quantidade não pode ficar vazia!')
                
            return quantidade