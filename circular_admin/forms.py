from django.forms import ModelForm, ModelChoiceField, ChoiceField
from .models import NewCircular, Memorandum, JobPost

class MemorandumForm(ModelForm):
  class Meta():
    model = Memorandum
    fields = '__all__'


class JobPostForm(ModelForm):
  class Meta():
    model = JobPost
    fields = '__all__'


class NewCircularForm(ModelForm):
  memorandum_with_date = ModelChoiceField(
    # widget=ChoiceField,
    queryset=Memorandum.objects.all(),
  )


  post = ModelChoiceField(
    # widget=ChoiceField,
    queryset=JobPost.objects.all(),
  )


  class Meta():
    model = NewCircular
    exclude = ['user', ]