from django.urls import path
from . import views

urlpatterns = [
    # Productos
    path('', views.producto_list, name='producto_list'),
    path('producto/nuevo/', views.producto_create, name='producto_create'),
    path('producto/<int:pk>/editar/', views.producto_edit, name='producto_edit'),
    path('producto/<int:pk>/eliminar/', views.producto_delete, name='producto_delete'),
    # Proveedores
    path('proveedores/', views.proveedor_list, name='proveedor_list'),
    path('proveedor/nuevo/', views.proveedor_create, name='proveedor_create'),
    path('proveedor/<int:pk>/editar/', views.proveedor_edit, name='proveedor_edit'),
    path('proveedor/<int:pk>/eliminar/', views.proveedor_delete, name='proveedor_delete'),
]