from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from checkapp.models import Computer
from checkapp.forms import CheckoutForm

def index(request):
    return render(request, 'checkapp/index.html', {})

def checkout(request):
    computers = Computer.objects.filter(is_available = True)
    context_dict = {'computers': computers}
    return render(request, 'checkapp/checkout.html', context_dict)

def checkin(request):
    computers = Computer.objects.filter(is_available = False)
    context_dict = {'computers': computers}
    return render(request, 'checkapp/checkin.html', context_dict)

def computer_detail(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    return render(request, 'checkapp/computer_detail.html', {'computer': computer})

def computer_checkin_detail(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    return render(request, 'checkapp/computer_checkin_detail.html', {'computer': computer})

def computer_checkout(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    computer.checkout()
    return redirect('index')

def computer_checkin(request, pk):
    computer = get_object_or_404(Computer, pk=pk)
    computer.checkin()
    return redirect('index')

def asset_new(request):
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            computer = form.save(commit=False)
            computer.added_by = request.user
            computer.added_date = timezone.now()
            computer.save()
            return redirect('index')
    else:
        form = CheckoutForm()
    return render(request, 'checkapp/asset_new.html', {'form': form})
