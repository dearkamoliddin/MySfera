from rest_framework import generics
from rest_framework.views import APIView, Response
from rest_framework import status
from django.utils import timezone

from app import models
from app import serializers


class CategoryAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductListSerializer


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer


class ProductAttributeAPIView(generics.ListAPIView):
    queryset = models.ProductAttribute.objects.all()
    serializer_class = serializers.ProductAttributeSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        attribute_type = self.request.query_params.get('type_id')
        if attribute_type:
            attribute_type = int(attribute_type)
            queryset = queryset.filter(attribute_type__id=attribute_type)
        return queryset


class AccessoryAPIView(generics.ListAPIView):
    queryset = models.Accessory.objects.all()
    serializer_class = serializers.AccessorySerializer


class ProductSetAPIView(generics.ListAPIView):
    queryset = models.ProductSet.objects.all()
    serializer_class = serializers.ProductSetSerializer


class ClientAPIView(generics.ListAPIView):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        client_type = self.request.query_params.get('type')
        if client_type:
            queryset = queryset.filter(type=client_type)
        return queryset


class RepairServiceAPIView(generics.ListAPIView):
    queryset = models.RepairService.objects.all()
    serializer_class = serializers.RepairServiceSerializer

    def get_queryset(self):
        product_id = self.request.query_params.get('product_id')
        if product_id:
            return self.queryset.filter(product__id=product_id)
        return super().get_queryset()


class ServiceCategoryAPIView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.ServiceCategorySerializer


class ServiceProductAPIView(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ServiceProductSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id')
        if category_id:
            return self.queryset.filter(category__id=category_id)
        return super().get_queryset()


class DeviceRepairAPIView(generics.CreateAPIView):
    queryset = models.DeviceRepair.objects.all()
    serializer_class = serializers.DeviceRepairSerializer


class OrderCreateAPIView(generics.CreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderCreateSerializer


class PromoCodeAPIView(APIView):
    def post(self, request):
        serializer = serializers.PromoCodeCheckSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        amount = serializer.validated_data.get('amount')
        promo_code = serializer.validated_data.get('promo_code')

        base_promo_code = models.PromoCode.objects.filter(name=promo_code).first()
        if not base_promo_code:
            return Response(
                data={"message": "Promo-kod mavjud emas."},
                status=status.HTTP_400_BAD_REQUEST
            )
        if amount < base_promo_code.min_amount:
            return Response(
                {"message": f"Bu promo-kod ishashi uchun minimal summa: {base_promo_code.min_amount} so'm."},
                status=status.HTTP_400_BAD_REQUEST
            )
        timezone_date = timezone.datetime.now().date()
        promo_code_date = base_promo_code.expiry_date
        if promo_code_date < timezone_date:
            return Response(
                {"message": "Bu promo-kod muddati tugagan."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response({
            'promo_code': base_promo_code.id,
            'amount': base_promo_code.amount
        })
