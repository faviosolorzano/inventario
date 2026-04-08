from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Proveedor
from .forms import ProductoForm, ProveedorForm

# ---- PRODUCTOS ----
def producto_list(request):
    productos = Producto.objects.select_related('proveedor').all()
    return render(request, 'productos/producto_list.html', {'productos': productos})

def producto_create(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('producto_list')
    return render(request, 'productos/producto_form.html', {'form': form, 'titulo': 'Nuevo Producto'})

def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    form = ProductoForm(request.POST or None, instance=producto)
    if form.is_valid():
        form.save()
        return redirect('producto_list')
    return render(request, 'productos/producto_form.html', {'form': form, 'titulo': 'Editar Producto'})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('producto_list')
    return render(request, 'productos/producto_confirm_delete.html', {'objeto': producto, 'tipo': 'Producto'})

# ---- PROVEEDORES ----
def proveedor_list(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'productos/proveedor_list.html', {'proveedores': proveedores})

def proveedor_create(request):
    form = ProveedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('proveedor_list')
    return render(request, 'productos/producto_form.html', {'form': form, 'titulo': 'Nuevo Proveedor'})

def proveedor_edit(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    form = ProveedorForm(request.POST or None, instance=proveedor)
    if form.is_valid():
        form.save()
        return redirect('proveedor_list')
    return render(request, 'productos/producto_form.html', {'form': form, 'titulo': 'Editar Proveedor'})

def proveedor_delete(request, pk):
    proveedor = get_object_or_404(Proveedor, pk=pk)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('proveedor_list')
    return render(request, 'productos/producto_confirm_delete.html', {'objeto': proveedor, 'tipo': 'Proveedor'})