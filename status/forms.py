from django.forms import ModelForm
from django import forms
from .models import Status, Statusreview

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['body']
        
    def __init__(self, *args, **kwargs):
        super(StatusForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})

class StatusReviewForm(ModelForm):
    class Meta:
        model = Statusreview
        fields = ['value']

    def __init__(self, *args, **kwargs):
        super(StatusReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class' : 'input'})


