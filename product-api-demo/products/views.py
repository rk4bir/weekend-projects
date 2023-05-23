from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import Size, Color, Price, Product
from .serializers import (
    ProductListSerializer, ProductDetailSerializer,
    SizeCreateSerializer, ColorCreateSerializer, PriceCreateSerializer
)
from .utils import logger


class ProductAPIView(ListAPIView):
    """Product list api view, shows 20 products per page with product's
        title, slug, product id, stock status.
        Also a click-able link that leads to product's detail view.
    """
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailAPIView(RetrieveAPIView):
    """Product detail api view, shows product's
        title, slug, product id, stock status, stocks, available sizes and colors.
        Also three click-able links to add color, size and price.
    """
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    lookup_field = 'slug'


class SizeCreateAPIView(CreateAPIView):
    """Size create view: creates Size instance and linked to Product in Generic-fashion"""
    queryset = Size
    serializer_class = SizeCreateSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'size'

    # overriding to add contenttype object to the Size instance
    def perform_create(self, serializer):
        """Grabs slug from kwargs, retrieve respective Product instance and
            links it to the Serializer Model i.e. Size instance.
        """
        try:
            product = Product.objects.get(slug=self.kwargs.get('slug'))
            serializer.save(content_object=product)
            message = "New size was added to " + product.title + '.'
            level = 'INFO'
        except Exception as err:
            message = "Couldn't save size: " + str(err)
            level = 'ERROR'
            pass

        # log information
        logger(level=level, request_type=self.request.method,
               url=self.request.build_absolute_uri(), status_code=201, message=message)


class ColorCreateAPIView(CreateAPIView):
    """Color create view: creates Color instance and linked to Product in Generic-fashion"""
    queryset = Color
    serializer_class = ColorCreateSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'color'

    # overriding to add contenttype object to the Color instance
    def perform_create(self, serializer):
        """Grabs slug from kwargs, retrieve respective Product instance and
            links it to the Serializer Model i.e. Color instance.
        """
        try:
            product = Product.objects.get(slug=self.kwargs.get('slug'))
            serializer.save(content_object=product)
            message = "New color was added to " + product.title + '.'
            level = 'INFO'
        except Exception as err:
            message = "Couldn't save color: " + str(err)
            level = 'ERROR'
            pass

        # log information
        logger(level=level, request_type=self.request.method,
               url=self.request.build_absolute_uri(), status_code=201, message=message)


class PriceCreateAPIView(CreateAPIView):
    """Price create view: creates Price instance and linked to Product in Generic-fashion"""
    queryset = Price
    serializer_class = PriceCreateSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'price'

    # overriding to add contenttype object to the price instance
    def perform_create(self, serializer):
        """Grabs slug from kwargs, retrieve respective Product instance and
            links it to the Serializer Model i.e. Price instance.
        """
        try:
            product = Product.objects.get(slug=self.kwargs.get('slug'))
            serializer.save(content_object=product)
            message = "New price was added to " + product.title + '.'
            level = 'INFO'
        except Exception as err:
            message = "Couldn't save price: " + str(err)
            level = 'ERROR'
            pass

        # log action information
        logger(level=level, request_type=self.request.method,
               url=self.request.build_absolute_uri(), status_code=201, message=message)
