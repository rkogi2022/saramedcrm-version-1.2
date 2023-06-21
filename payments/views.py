from django.shortcuts import render,redirect,get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.contrib import messages
from django.db.models import Sum, F
from django.contrib.auth.decorators import login_required

# import models
from prospects.models import business_prospect
from .models import invoice
from .models import receipt
from .models import implementation

# import forms
from .forms import CreateInvoiceForm
from .forms import CreateReceiptForm
from .forms import AddImplementationDetails
#create your views here

# displaying list of invoices
def invoice_details(request):
    invoicedetails=invoice.objects.all().order_by('-created_date')
    page=Paginator(invoicedetails,10)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        }
    template='payments/invoice.html'
    return render(request,template,context)

# creatin a new invoice
@login_required(login_url='auth_app:login')
def create_invoice(request):
    template='payments/create invoice.html'
    if request.method == 'POST':
        form=CreateInvoiceForm(request.POST)
        if form.is_valid():            
            form.save()
            messages.success(request, f'The invoice was created successfully')
            return redirect('payments:invoicedetails')
    else:
            form=CreateInvoiceForm()

    return render(request, template,{'form':form})

# delete an invoice
@login_required(login_url='auth_app:login')
def delete_invoice(request,id):
    id = int(id)
    try:
         invoicedetails=invoice.objects.get(id=id)
    except:
        return redirect('payments:invoicedetails')
    invoicedetails.delete()
    return redirect('payments:invoicedetails')

# display receipts
def receipts_details(request):
    paid_amount= receipt.objects.aggregate(total_amount=Sum('amt_paid'))
    receiptsdetails=receipt.objects.all().order_by('-created_date')
    page=Paginator(receiptsdetails,10)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        'paid_amount':paid_amount,
    }
    template='payments/receipts.html'
    return render(request,template,context)


# creatin a new invoice
@login_required(login_url='auth_app:login')
def create_receipt(request):
    template='payments/create receipt.html'
    if request.method == 'POST':
        form=CreateReceiptForm(request.POST)
        if form.is_valid():            
            form.save()
            messages.success(request, f'The Receipt was added successfully')
            return redirect('payments:receiptsdetails')
    else:
            form=CreateReceiptForm()
    return render(request, template,{'form':form})

@login_required(login_url='auth_app:login')
def update_receipt(request,id):
    receiptdetails=get_object_or_404(receipt, id=id)
    if request.method == 'POST':
        form=CreateReceiptForm(request.POST, instance=receiptdetails)
        if form.is_valid():
            form.save()
            messages.success(request, f'Receipt updated successfully')
            return redirect('payments:receiptsdetails')
    else:
        form=CreateReceiptForm(instance=receiptdetails)
    context={
        'form':form,
        }
    template='payments/update receipt.html'
    return render(request,template,context)

#delete a receipt
@login_required(login_url='auth_app:login')
def delete_receipt(request,id):
    id = int(id)
    try:
        receiptdetails=receipt.objects.get(id=id)
    except:
        messages.error(request, f'The receipt was deleted successfully')
        return redirect('payments:receiptsdetails')
    receiptdetails.delete()
    return redirect('payments:receiptsdetails')

# transactional reports view
def transactional_report(request):
    template='payments/transactional reports.html'
    moneyreports=business_prospect.objects.annotate(
        total_amount_paid=Sum('receipt__amt_paid'),
        total_invoices=Sum('invoice__total_cost'),
        ).annotate(balance=F('total_invoices') - F('total_amount_paid'))
    page=Paginator(moneyreports,10)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
    }
    return render(request,template, context)

# view clients licence expiry
def acc_details(request):
    implementationdetails=implementation.objects.all()
    page=Paginator(implementationdetails,10)
    page_list=request.GET.get('page')
    page = page.get_page(page_list)
    context={
        'page':page,
        }
    template='payments/account.html'
    return render(request, template, context)

# Display implementation dates
def implementation_dates(request, id):
    details=implementation.objects.filter(id=id)
    context={
        'details':details
        }
    template='payments/implementation.html'
    return render(request, template,context )

# add implementation dates
@login_required(login_url='auth_app:login')
def create_implementation(request):
    template='payments/add implementation.html'
    if request.method == 'POST':
        form=AddImplementationDetails(request.POST,request.FILES)
        if form.is_valid():    
            uploaded_file = request.FILES['implementation_report']        
            form.save()
            messages.success(request, f'The dates were added successfully')
            return redirect('payments:clients-details')
    else:
            form=AddImplementationDetails()
    return render(request, template,{'form':form})

@login_required(login_url='auth_app:login')
def update_implementation(request,id):
    implementationdetails=get_object_or_404(implementation, id=id)
    if request.method == 'POST':
        form=AddImplementationDetails(request.POST, instance=implementationdetails)
        if form.is_valid():
            form.save()
            messages.success(request, f'Implementation dates updated successfully')
            return redirect('payments:clients-details')
    else:
        form=AddImplementationDetails(instance=implementationdetails)
    context={
        'form':form,
        }
    template='payments/update implementation.html'
    return render(request,template,context)

#delete a receipt
@login_required(login_url='auth_app:login')
def delete_implementation(request,id):
    id = int(id)
    try:
        implementationdetails=implementation.objects.get(id=id)
    except:
        messages.error(request, f'The client details were deleted successfully')
        return redirect('payments:clients-details')
    implementationdetails.delete()
    return redirect('payments:clients-details')