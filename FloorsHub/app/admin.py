from django.contrib import admin
from .models import Advertisement, AdvertisementImage, Category, Subcategory
# Register your models here.


admin.site.register(Advertisement)
admin.site.register(AdvertisementImage)
admin.site.register(Category)
admin.site.register(Subcategory)