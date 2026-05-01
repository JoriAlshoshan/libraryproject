from django import forms
from .models import Book
from .models import StudentCard
from .models import Student, Address
from .models import Student2


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']


class StudentCardForm(forms.ModelForm):
    class Meta:
        model = StudentCard
        fields = ['student_name', 'card_title', 'image']


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']


class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple
        }