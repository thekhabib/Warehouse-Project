from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from product.models import Product, ProductMaterial, Warehouse, Material
from product.serializer import ProductSerializer, ProductMaterialSerializer, \
    WarehouseSerializer, MaterialSerializer


class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MaterialListCreateView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class ProductMaterialListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductMaterialSerializer

    def get_queryset(self):
        product_id = self.kwargs['pk']
        return ProductMaterial.objects.filter(product__id=product_id)


class WarehouseListCreateView(generics.ListCreateAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class WarehouseView(APIView):

    def post(self, request):
        product = get_object_or_404(Product, code=request.data['product_code'])
        quantity = request.data['quantity']
        product_materials = product.materials.all()
        materials_data = []
        for mat in product_materials:
            total_qty = mat.quantity * quantity
            warehouses = Warehouse.objects.filter(material=mat.material).order_by('id')
            for warehouse in warehouses:
                if total_qty <= 0:
                    break
                get_qty = min(total_qty, warehouse.remainder)
                materials_data.append(
                    {
                        "warehouse_id": warehouse.id,
                        "material_name": warehouse.material.name,
                        "qty": get_qty,
                        "price": warehouse.price,
                    },
                )
                total_qty -= get_qty
            if total_qty > 0:
                materials_data.append(
                    {
                        "warehouse_id": None,
                        "material_name": mat.material.name,
                        "qty": total_qty,
                        "price": None,
                    },
                )
        return Response(
            {
                'result': {
                    'product_name': product.name,
                    'product_qty': quantity,
                    'product_materials': materials_data,
                }
            }
        )


