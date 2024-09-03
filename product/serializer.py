from rest_framework import serializers

from product.models import Product, ProductMaterial, Warehouse, Material


class ProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'code',
        ]


class MaterialSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Material
        fields = [
            'id',
            'name',
        ]


class ProductMaterialSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), required=False)
    material = serializers.PrimaryKeyRelatedField(queryset=Material.objects.all(), required=False)

    class Meta:
        model = ProductMaterial
        fields = [
            'id',
            'product',
            'material',
            'quantity',
        ]


class WarehouseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    material = serializers.PrimaryKeyRelatedField(queryset=Material.objects.all(), required=False)

    class Meta:
        model = Warehouse
        fields = [
            'id',
            'material',
            'remainder',
            'price',
        ]


