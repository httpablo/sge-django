from rest_framework import serializers
from products.models import Product
from categories.models import Category
from brands.models import Brand
from brands.serializers import BrandSerializer
from categories.serializers import CategorySerializer


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
    )
    brand = serializers.PrimaryKeyRelatedField(
        queryset=Brand.objects.all(),
    )
    description = serializers.CharField()
    serie_number = serializers.CharField()
    cost_price = serializers.DecimalField(max_digits=20, decimal_places=2)
    selling_price = serializers.DecimalField(max_digits=20, decimal_places=2)
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    update_at = serializers.DateTimeField()


class ProductModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class ProductListDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    brand = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'serie_number', 'cost_price', 'selling_price', 'quantity', 'created_at', 'update_at', 'category', 'brand']
    
    def get_category(self, obj):
        return obj.category.name

    def get_brand(self, obj):
        return obj.brand.name
