from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = '__all__'
        labels = {
            'BookTitle': 'Book Title',
            'NumberOfPages': 'Number of Pages'
            }
    
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['Author'].empty_label = "(Select an Author)"

class AuthorForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = '__all__'
        labels = {
            'FirstName': 'First Name',
            'LastName': 'Last Name',
            'CountryOfOrigin': 'Country of Origin'
            }
