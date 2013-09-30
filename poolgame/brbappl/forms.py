from django.forms import ModelForm, Select, HiddenInput
from brbappl.models import Contestant, People, Result

ALL_CHOICES = [x for x in People.objects.all().values_list('id', 'name')]


class ContestantForm(ModelForm):
     class Meta:
         model = Contestant
         fields = ['name']

class TestQuestion(ModelForm):
    class Meta:
        model = Result
        fields = ['is_survivor', 'killed_by']
        # exclude=('name',)
        # widgets = {
            # 'killed_by': Select(
                # choices=ALL_CHOICES),
            # 'name': HiddenInput()
        # }
