from app import views
from django.urls import path

urlpatterns = [
    path('category/', views.CategoryAPIView.as_view(), name='categories'),
    path('product/', views.ProductListAPIView.as_view(), name='product-list'),
    path('product/<int:pk>/detail/', views.ProductDetailAPIView.as_view(), name='product-detail'),
    path('product_attribute/', views.ProductAttributeAPIView.as_view(), name='product-attribute'),

    path('accessory/', views.AccessoryAPIView.as_view(), name='accessories'),

    path('productset/', views.ProductSetAPIView.as_view(), name='product-set'),

    path('service_category/', views.ServiceCategoryAPIView.as_view(), name='service_category'),
    path('service_product/', views.ServiceProductAPIView.as_view(), name='service_product'),
    path('service_repair/', views.RepairServiceAPIView.as_view(), name='repair'),
    path('device_repair/', views.DeviceRepairAPIView.as_view(), name='device_repair'),
    path('client/', views.ClientAPIView.as_view(), name='clients'),

    path('order/', views.OrderCreateAPIView.as_view(), name='order'),
    path('promo_code/', views.PromoCodeAPIView.as_view(), name='promo-code'),
]
