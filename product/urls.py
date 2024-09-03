from django.urls import path

from product.views import ProductListCreateView, MaterialListCreateView, ProductMaterialListCreateView, \
    WarehouseListCreateView, WarehouseView


urlpatterns = [
    path('', WarehouseView.as_view(), name=''),
    path('product/', ProductListCreateView.as_view(), name='product_list_create'),
    path('material/', MaterialListCreateView.as_view(), name='material_list_create'),
    path('product/<int:pk>/', ProductMaterialListCreateView.as_view(), name='product_detail'),
    path('warehouse/', WarehouseListCreateView.as_view(), name='warehouse_list_create'),
]

