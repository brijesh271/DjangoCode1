from django.shortcuts import render, HttpResponseRedirect
from .forms import ProductRegistration
from .models import User
# Create your views here.
#This Function will add a new product and show all products
def add_show(request):

    if request.method == 'POST':
        fm = ProductRegistration(request.POST)
        if fm.is_valid():
            #pm = fm.cleaned_data['pid']
            nm = fm.cleaned_data['name']
            qm = fm.cleaned_data['quantity']
            prm = fm.cleaned_data['price']
            #reg = User(pid=pm, name=nm,quantity=qm, price=prm)
            reg = User(name=nm, quantity=qm, price=prm)
            reg.save()
            fm = ProductRegistration()
    else:
        fm = ProductRegistration()
    prod = User.objects.all()
    return render(request, 'enroll/addandshow.html',{'form':fm, 'pud':prod})

#This Function will update /edit
def update_data(request, pid):
    if request.method == 'POST':
        pi = User.objects.get(pk=pid)
        fm = ProductRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=pid)
        fm = ProductRegistration(instance=pi)
    return render(request, 'enroll/updateproduct.html', {'form' : fm})

# This function will delete product (pk=Primary Key )
def delete_data(request, pid):
    if request.method == 'POST':
        pi = User.objects.get(pk=pid)
        pi.delete()
        return HttpResponseRedirect('/')
