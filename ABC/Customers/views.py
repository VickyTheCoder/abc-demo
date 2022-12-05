from django.shortcuts import render
from django.http import JsonResponse
from .models import Customer
# Create your views here.
def new_customer(request):
    return render(request, 'customers/add.html')

def insert_customer_in_db(request):
    name = request.POST.get('name')
    mobile = request.POST.get('mobile')
    email = request.POST.get('email')
    company_name = request.POST.get('company_name')
    tax_number = request.POST.get('tax_number')
    customer_address = request.POST.get('customer_address')
    Customer.objects.create(
        name=name, mobile=mobile, email=email,
        company_name=company_name, tax_number=tax_number,
        customer_address=customer_address
    )
    resp = {'status': f"User('{name}') added2"}
    print(resp, 77777777777777777)
    return JsonResponse(resp)