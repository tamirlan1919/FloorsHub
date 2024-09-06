from rest_framework import serializers
from .models import Category, Subcategory, Advertisement, AdvertisementImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class SubcategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Subcategory
        fields = ['id', 'name', 'category']

class AdvertisementImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvertisementImage
        fields = ['id', 'image']

class AdvertisementSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    subcategory = SubcategorySerializer(read_only=True)
    images = AdvertisementImageSerializer(many=True, read_only=True)

    class Meta:
        model = Advertisement
        fields = ['id', 'title', 'description', 'price', 'category', 'subcategory', 'is_active', 'created_at', 'images']
