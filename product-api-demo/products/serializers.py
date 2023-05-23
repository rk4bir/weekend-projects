from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Size, Color, Price, Product


class ProductListSerializer(HyperlinkedModelSerializer):
    """Serializer class for Product list view"""
    # detail view is click-able field that leads to product-detail view
    detail_view = serializers.HyperlinkedIdentityField(view_name='product-detail',
                                                       lookup_field='slug',
                                                       lookup_url_kwarg='slug',
                                                       format='html')

    class Meta:
        model = Product
        fields = ['detail_view', 'slug', 'pid', 'title', 'stock_status']


class ProductDetailSerializer(ModelSerializer):
    """Serializer class for product detail view"""
    add_size = serializers.HyperlinkedIdentityField(view_name='set-size', lookup_field='slug', format='html')
    add_color = serializers.HyperlinkedIdentityField(view_name='set-color', lookup_field='slug', format='html')
    add_price = serializers.HyperlinkedIdentityField(view_name='set-price', lookup_field='slug', format='html')

    class Meta:
        model = Product
        # names, product code, slug, status, stocks
        fields = ['add_size', 'add_color', 'add_price',
                  'title', 'pid', 'slug', 'stock_status', 'stocks',
                  'price_ranges', 'available_sizes', 'available_colors']


class SizeCreateSerializer(ModelSerializer):
    """Serializer class to create a Size instance and add it to its product=>contenttype"""
    class Meta:
        model = Size
        fields = ['title', 'description']


class ColorCreateSerializer(ModelSerializer):
    """Serializer class to create a Color instance and add it to its product=>contenttype"""
    class Meta:
        model = Color
        fields = ['title', 'color_code']


class PriceCreateSerializer(ModelSerializer):
    """Serializer class to create a Price instance and add it to its product=>contenttype"""
    class Meta:
        model = Price
        fields = ['price', 'start_date', 'end_date']
