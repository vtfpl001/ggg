from django.shortcuts import render
from .models import Product
from .models import Certificate
from django.contrib.auth.decorators import login_required




def home(request):
    return render(request, 'vtapp/home.html')

def about(request):
    return render(request, 'vtapp/about.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'vtapp/products.html', {'products': products})

def certificates(request):
    certificates = Certificate.objects.all()
    return render(request, 'vtapp/certificates.html', {'certificates': certificates})


def contact(request):
    return render(request, 'vtapp/contact.html')




from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Certificate
from .forms import ProductForm, CertificateForm

# ... Your existing views ...

# Create a product
@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'vtapp/product_form.html', {'form': form})

# Detail view for a product
@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'vtapp/product_detail.html', {'product': product})

# Update a product
@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'vtapp/product_form.html', {'form': form})

# Delete a product
@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return render(request, 'vtapp/product_confirm_delete.html', {'product': product})

# Similarly, create views for Certificate CRUD operations.




# Create a certificate
@login_required
def certificate_create(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('certificates')
    else:
        form = CertificateForm()
    return render(request, 'vtapp/certificate_form.html', {'form': form})

# Detail view for a certificate
@login_required
def certificate_detail(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    return render(request, 'vtapp/certificate_detail.html', {'certificate': certificate})

# Update a certificate
@login_required
def certificate_update(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES, instance=certificate)
        if form.is_valid():
            form.save()
            return redirect('certificate_detail', pk=pk)
    else:
        form = CertificateForm(instance=certificate)
    return render(request, 'vtapp/certificate_form.html', {'form': form})

# Delete a certificate
@login_required
def certificate_delete(request, pk):
    certificate = get_object_or_404(Certificate, pk=pk)
    if request.method == 'POST':
        certificate.delete()
        return redirect('certificates')
    return render(request, 'vtapp/certificate_confirm_delete.html', {'certificate': certificate})
