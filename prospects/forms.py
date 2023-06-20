from django import forms

# import models
from . models import business_prospect
from .models import conversion_tracker


#create custom date widget
class DateInput(forms.DateInput):
    input_type = 'date'

class AddBussinessProspectForm(forms.ModelForm):
    created_date=forms.DateTimeField(label='Date',widget=DateInput)
    class Meta:
        model=business_prospect
        fields=('facility_name','county','town','email','contact_person','phone_no','comment','created_date')

class FeedbackForm(forms.Form):
    feedback = forms.CharField(widget=forms.Textarea(attrs={'class': 'feedback-textarea'}))

class ConversionTrackerForm(forms.ModelForm):
    demodate=forms.DateTimeField(label='Demo Date',widget=DateInput,required=False)
    assessmentdate=forms.DateTimeField(label='Assessment Date',widget=DateInput,required=False)
    reportdate=forms.DateTimeField(label='Report Dissemination Date',widget=DateInput,required=False)
    class Meta:
        model=conversion_tracker
        fields=('demo_id','demostatus','demodate','Attendees','meeting',
                'feedback','assessmentdate','report','reportdate','expression',
                'facility_license','krapin')