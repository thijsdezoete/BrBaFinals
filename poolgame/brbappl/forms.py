from django.forms import ModelForm
from brbappl.models import Contestant, Result


class ContestantForm(ModelForm):
     class Meta:
         model = Contestant
         fields = ['name']

class TestQuestion(ModelForm):
    class Meta:
        model = Result
        fields = ['is_survivor', 'killed_by']
