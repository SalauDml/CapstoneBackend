from rest_framework import serializers
from .models import Blogs


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields= '__all__'
        

    def validate(self, attrs):
        errors = {}
        images = attrs.get('images')
        title= attrs.get('title')
        mini_description = attrs.get('mini_description')
        readingTime = attrs.get('readingTime')
        content= attrs.get('content')

        if self.partial!=True:
            if not images:
                errors['Images'] = ['Image is a required field']
            if not title:
                errors['Title'] = ['Title is a required field']
            if not mini_description:
                errors['description'] = ['Description is a required field']
            if not readingTime:
                errors['readingTime'] = ['Reading time is a required field']
            if not content:
                errors['content'] = ['Content is a required field']

        if errors:
            raise serializers.ValidationError(errors)
        return attrs

    
    def create(self, validated_data):
        return Blogs.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.images = validated_data.get('images',instance.images)
        instance.title = validated_data.get('title',instance.title)
        instance.mini_description = validated_data.get('mini_description',instance.mini_description)
        instance.readingTime = validated_data.get("readingTime",instance.readingTime)
        instance.content = validated_data.get('content',instance.content)
        instance.save()
        # blog = 
        return instance

