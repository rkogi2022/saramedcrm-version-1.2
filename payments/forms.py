from django import forms

# import your models
from . models import invoice
from . models import receipt
from .models import implementation

#custom date widget
class DateInput(forms.DateInput):
    input_type = 'date'

class CreateInvoiceForm(forms.ModelForm):
    class Meta:
        model=invoice
        fields=('facilityname','project_cost',)

class CreateReceiptForm(forms.ModelForm):
    transaction_date=forms.DateField(label='Transaction Date',widget=DateInput)
    class Meta:
        model=receipt
        fields=('facilityname','amt_paid','payment_mode','transaction_date',)

class AddImplementationDetails(forms.ModelForm):
    town= forms.CharField(label='Town', required=False)
    county= forms.CharField(label='County',required=True)
    start_date=forms.DateTimeField(label='Start Date',widget=DateInput)
    golive_date=forms.DateField(label='Go-Live Date',widget=DateInput)
    end_date=forms.DateField(label='End Date',widget=DateInput)
    class Meta:
        model=implementation
        fields=('facility_name','town','county','start_date','golive_date','end_date','implementation_report')