from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Product  # Make sure Product is imported
from django.contrib.auth.decorators import login_required
from .models import Product, Batch  # Assuming you’ve added Batch model
from datetime import datetime
from .models import ManufacturingAndProduction

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard
        else:
            error_message = 'Invalid username or password'
            return render(request, 'core/login.html', {'error_message': error_message})

    return render(request, 'core/login.html')


# Product Report View
@login_required
def product_report_view(request):
    products = Product.objects.all()
    return render(request, 'core/product_report.html', {'products': products})

def production_report(request):
    batches = Batch.objects.select_related('product').order_by('-manufacture_date')
    context = {
        'batches': batches,
        'report_date': datetime.now()
    }
    return render(request, 'report.html', context)

def production_report(request):
    productions = ManufacturingAndProduction.objects.all().order_by('-production_date')
    return render(request, 'core/production_report.html', {'productions': productions})

def dashboard_view(request):
    products = Product.objects.all()  # Fetch all products
    return render(request, 'core/dashboard.html', {'products': products})