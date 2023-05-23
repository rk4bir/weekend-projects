from django.contrib import admin
from django.urls import path
from products.views import (
    ProductAPIView, ProductDetailAPIView,
    SizeCreateAPIView, ColorCreateAPIView, PriceCreateAPIView
)


urlpatterns = [
    # products list
    path('products/', ProductAPIView.as_view(), name='product-list'),

    # attribute -> size create view
    path('products/<slug:slug>/size/', SizeCreateAPIView.as_view(), name='set-size'),

    # attribute -> color create view
    path('products/<slug:slug>/color/', ColorCreateAPIView.as_view(), name='set-color'),

    # attribute -> price create view
    path('products/<slug:slug>/price/', PriceCreateAPIView.as_view(), name='set-price'),

    # product detail
    path('products/<slug:slug>/', ProductDetailAPIView.as_view(), name='product-detail'),

    # Django admin
    path('admin/', admin.site.urls),
]
