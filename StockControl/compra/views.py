
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DeleteView

from .forms import ProductoForm, ProveedorForm
from .models import Producto, Proveedor

"""
    Cuando se utilizan vistas basadas en clases, el funcionamiento es el siguiente:
    1- dispatch(): valida la petición y selecciona el método HTTP (GET, POST, PUT) que se utilizó para la solicitud.
    2- http_method_not_allowed(): arroja un error si el método HTTP utilizado por la petición no está definido o no es soportado.
"""

"""
    Cuado se crea una clase que hereda de una TemplateView, su definición interna es la siguiente:
    class Inicio(TemplateView):
        tempate_name = ''
        
        def get(self, request, *args, **kwargs):
            return render(request, template_name)
"""


# Create your views here.
# Vista basada en funciones:
def inicio(request):
    return render(request, 'index.html')


# Vista basada en clases:
class Inicio(TemplateView):
    template_name = 'index.html'


# Vista basada en funciones:
def listarProductos(request):
    productos = Producto.objects.all()
    return render(request, template_name='productos/listado.html', context={'productos': productos})


# Vista basada en clases:
class ListadoProductos(ListView):
    model = Producto
    template_name = 'productos/listado.html'
    context_object_name = 'productos'
    queryset = Producto.objects.all()


# En caso de no utilizar el formulario personalizado ProductoForm definido en forms.py:
#ProductoForm = modelform_factory(Producto, exclude=[])

# Vista basada en funciones:
def agregarProducto(request):
    proveedor_form = ProveedorForm(request.POST)
    if request.POST:
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('compra:index')
        if proveedor_form.is_valid():
            proveedor_form.save()
    else:
        producto_form = ProductoForm()
        proveedor_form = ProveedorForm()
    context = {
        'form_1': producto_form,
        'form_2': proveedor_form
    }
    return render(request, 'productos/nuevo.html', context)

# Vista basada en funciones:
def modificarProducto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    # Especificar la instancia permite indicar cuál es el id del producto que queremos modificar
    # en la base de datos, por lo que los campos del formulario se autocompletarán con los datos
    # de la instancia pasada por parámetro.
    if request.POST:
        producto_form = ProductoForm(request.POST, instance=producto, use_required_attribute=False)
        if producto_form.is_valid():
            # Debido a que se especificó la instancia, django identificará el id de la instancia y al
            # llamar el método save() guardará los datos de la misma instancia en lugar de crear una nueva.
            producto_form.save()
            return redirect('index')
    else:
        producto_form = ProductoForm(instance=producto)
        # Enviamos el objeto producto_form que contiene el formulario con la información obtenida de la base de datos
    return render(request, 'productos/editar.html', {'form': producto_form})


# Vista basada en funciones:
def eliminarProducto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if producto:
        producto.delete()
    return redirect('compra:productos')


# Vista basada en clases:
class EliminarProducto(DeleteView):
    model = Producto
    template_name = 'productos/eliminar.html/'
    success_url = reverse_lazy('compra:productos')

    # Si se desea hacer la eliminación lógica (no se elimina de la base de datos)
    # se puede redefinir el método post de esta manera:
    # def post(self, request, pk, *args, **kwargs):
    #     object = Producto.objects.get(id=pk)
    #     object.estado = False
    #     object.save()
    #     return redirect('compra:productos')
    # Recordar eliminar el atributo succes_url para que no se produzca un error al redireccionar.


# Vista basada en funciones:
def detalleProducto(request, id):
    producto = Producto.objects.get(pk=id)
    return render(request, 'productos/detalle.html', {'producto': producto})


def agregarProveedor(request):
    if request.POST:
        proveedor_form = ProveedorForm(request.POST)
        if proveedor_form.is_valid():
            proveedor_form.save()
            return redirect('compra:proveedores')
    else:
        proveedor_form = ProveedorForm()
    return render(request, 'proveedores/nuevo.html', {'form': proveedor_form})


def modificarProveedor(request, id):
    proveedor = get_object_or_404(Proveedor, pk=id)
    if request.POST:
        proveedor_form = ProveedorForm(request.POST, instance=proveedor)
        if proveedor_form.is_valid():
            proveedor_form.save()
            return redirect('compra:proveedores')
    else:
        proveedor_form = ProveedorForm(instance=proveedor)
    return render(request, 'proveedores/editar.html', {'form': proveedor_form})


def detalleProveedor(request, id):
    proveedor = Proveedor.objects.get(pk=id)
    return render(request, 'proveedores/detalle.html', {'proveedor': proveedor})


def listarProveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, template_name='proveedores/listado.html', context={'proveedores': proveedores})


class EliminarProveedor(DeleteView):
    model = Proveedor
    template_name = 'proveedores/eliminar.html/'
    success_url = reverse_lazy('compra:proveedores')