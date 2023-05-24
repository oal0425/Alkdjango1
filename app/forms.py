from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

"""en fields se puede mandar una lista y especificar los campos que queremos utilizar"""
# fields = ['firstname','lastname', 'birth']