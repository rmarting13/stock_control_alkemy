from django.urls import path
from .views import ListadoProductos, listarProductos, detalleProducto, DetalleProducto, modificarProducto, \
    ModificarProducto, Inicio, inicio, agregarProducto, eliminarProducto, EliminarProducto, \
    EliminarProveedor, listarProveedores, agregarProveedor, detalleProveedor, modificarProveedor

# el parámetro 'name=index' permite referirse a la url y su template desde el sistemas de templates de django
urlpatterns = [
    # path('', inicio, name='index'),  # Vista basada en funciónes.
    path('', Inicio.as_view(), name='index'),  # Vista basada en clases.
    path('detalle/<int:id>', detalleProducto, name='detalle_producto'),  # Vista basada en funciones.
    # path('detalle/<int:pk', DetalleProducto, name='detalle_producto'),  # Vista basada en clases.
    path('editar/<int:id>', modificarProducto, name='editar_producto'),  # Vista basada en funciones.
    # path('editar/<int:pk>', ModificarProducto, name='editar_producto'),  # Vista basada en clases.
    # path('productos/<int:id>', ListadoProductos, name='lista_productos'), #Vista basada en funciones.
    path('productos/', ListadoProductos.as_view(), name='productos'),  # Vista basada en clases.
    path('nuevo/', agregarProducto, name='nuevo_producto'), #Vista basada en funciones.
    # path('nuevo/', AgregarProducto.as_view(), name='nuevo_producto'),  # Vista basada en clases.
    # path('eliminar/<int:id>', eliminarProducto, name='eliminar_producto'),  # Vista basada en funciones.
    path('eliminar/<int:pk>', EliminarProducto.as_view(), name='eliminar_producto'),  # Vista basada en clases.

    path('proveedores/', listarProveedores, name='proveedores'),  # Vista basada en funciones.
    path('proveedor/nuevo', agregarProveedor, name='nuevo_proveedor'),  # Vista basada en funciones.
    path('proveedor/editar/<int:id>', modificarProveedor, name='editar_proveedor'),  # Vista basada en funciones.
    path('proveedor/detalle/<int:id>', detalleProveedor, name='detalle_proveedor'),  # Vista basada en funciones.
    path('proveedor/eliminar/<int:pk>', EliminarProveedor.as_view(), name='eliminar_proveedor')
]
