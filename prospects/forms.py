from django import forms

# import models
from . models import business_prospect
from .models import conversion_tracker


#create custom date widget
class DateInput(forms.DateInput):
    input_type = 'date'

class AddBussinessProspectForm(forms.ModelForm):
    created_date=forms.DateTimeField(label='Date',widget=DateInput(attrs={'class':'form-control'}),required=True)
    comment=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),required=True)
    class Meta:
        model=business_prospect
        fields=('facility_name','county','town','email','contact_person','phone_no','comment','created_date')

        widgets = {
            'facility_name': forms.TextInput(attrs={'class': 'form-control'}),
            'county': forms.TextInput(attrs={'class': 'form-control'}),
            'town': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control'}),
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


class FeedbackForm(forms.Form):
    feedback = forms.CharField(widget=forms.Textarea(attrs={'class': 'feedback-textarea'}))


class ConversionTrackerForm(forms.ModelForm):
    demodate=forms.DateTimeField(label='Demo Date',widget=DateInput(attrs={'class':'form-control'}),required=False)
    assessmentdate=forms.DateTimeField(label='Assessment Date',widget=DateInput(attrs={'class':'form-control'}),required=False)
    reportdate=forms.DateTimeField(label='Report Dissemination Date',widget=DateInput(attrs={'class':'form-control'}),required=False)
    class Meta:
        model = conversion_tracker
        fields = '__all__'
        exclude = ['created_by']  # If you want to exclude a specific field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['demostatus'].widget.attrs.update({'class': 'form-control'})  # Add CSS class to the field
        self.fields['Attendees'].widget.attrs.update({'class': 'form-control', 'rows': 3})  # Add CSS class and specify the number of rows for the field
        self.fields['meeting'].widget.attrs.update({'class': 'form-control'})  # Add CSS class to the field
        self.fields['feedback'].widget.attrs.update({'class': 'form-control', 'rows': 3})  # Add CSS class and specify the number of rows for the field      self.fields['report'].widget.attrs.update({'class': 'form-control-file'})  # Add CSS class to the field
        self.fields['facility_license'].widget.attrs.update({'class': 'form-control-file'})  # Add CSS class to the field
        self.fields['krapin'].widget.attrs.update({'class': 'form-control-file'})  # Add CSS class to the field
