from django.contrib import admin
from app import models

admin.site.register(
    [
        models.Category,
        models.Product,
        models.ProductAttribute,
        models.ProductMemoryPrice,
        models.ProductImage,
        models.Memory,
        models.PromoCode,
        models.Order,
        models.OrderProduct,
        models.ProductSet,
        models.OrderProductSet,
        models.Client,
        models.RepairService,
        models.DeviceRepair,
        models.Accessory,
        models.AttributeType
    ]
)
