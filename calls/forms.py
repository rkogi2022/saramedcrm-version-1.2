
from django import forms
from . models import support
from .models import courtesy
from .models import director


#custom date widget
class DateInput(forms.DateInput):
    input_type = 'date'

class AddSupportCallForm(forms.ModelForm):
    logdate=forms.DateTimeField(label='Date',widget=DateInput)
    completiondate=forms.DateTimeField(label='Date',widget=DateInput,required=False)
    problem=forms.CharField(widget=forms.Textarea(attrs={'class': 'feedback-textarea'}))
    solution=forms.CharField(widget=forms.Textarea(attrs={'class': 'feedback-textarea'}))
    class Meta:
        model=support
        fields=('__all__')

class UpdateSupportCallForm(forms.ModelForm):
    logdate=forms.DateTimeField(label='Date',widget=DateInput)
    class Meta:
        model=support
        fields=('facility','logdate','module','problem','status')

class AddCourtesyCallForm(forms.ModelForm):
    logdate=forms.DateTimeField(label='Date',widget=DateInput)
    feedback=forms.CharField(widget=forms.Textarea(attrs={'class': 'feedback-textarea'}))
    class Meta:
        model=courtesy
        fields=('__all__')

class AddDirectorCallForm(forms.ModelForm):
    feedback_given=forms.CharField(widget=forms.Textarea(attrs={'class': 'feedback-textarea'}))
    logdate=forms.DateTimeField(label='Date',widget=DateInput)
    class Meta:
        model=director
        fields=('__all__')