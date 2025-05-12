from rest_framework import serializers
from profiles.models import Profile, ProfileCategory, ProfileLanguage, Availability, Resource

class ProfileCategoryInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileCategory
        fields = ['category', 'years_of_experience']

class ProfileLanguageInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileLanguage
        fields = ['language', 'proficiency', 'is_native']

class AvailabilityInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = [
            'availability_type', 'repeat_on',
            'date_start', 'date_end', 'time_start', 'time_end'
        ]

class ResourceInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['thumbnail_url']

    def create(self, validated_data):
        validated_data['resource_type'] = 'profile_photo'
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data['resource_type'] = 'profile_photo'
        return super().update(instance, validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    
    profile_categories = ProfileCategoryInlineSerializer(many=True, write_only=True, required=False)
    profile_languages = ProfileLanguageInlineSerializer(many=True, write_only=True, required=False)
    availabilities = AvailabilityInlineSerializer(many=True, write_only=True, required=False)
    profile_photo = ResourceInlineSerializer(write_only=True, required=False)
    profile_photo_url = serializers.SerializerMethodField() 

    class Meta:
        model = Profile
        fields = [
            'id', 'first_name', 'last_name', 'email', 'phone_number', 'gender','online',
            'profile_categories', 'profile_languages', 'availabilities','profile_photo','profile_photo_url'
        ]

    def create(self, validated_data):
        categories_data = validated_data.pop('profile_categories', [])
        languages_data = validated_data.pop('profile_languages', [])
        availabilities_data = validated_data.pop('availabilities', [])
        profile_photo_data = validated_data.pop('profile_photo', None)

        profile = Profile.objects.create(**validated_data)

        for category in categories_data:
            ProfileCategory.objects.create(profile=profile, **category)
        for language in languages_data:
            ProfileLanguage.objects.create(profile=profile, **language)
        for availability in availabilities_data:
            Availability.objects.create(profile=profile, **availability)
        if profile_photo_data:
            Resource.objects.create(profile=profile, resource_type='profile_photo', **profile_photo_data)

        return profile

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('profile_categories', [])
        languages_data = validated_data.pop('profile_languages', [])
        availabilities_data = validated_data.pop('availabilities', [])
        profile_photo_data = validated_data.pop('profile_photo', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if categories_data:
            ProfileCategory.objects.filter(profile=instance).delete()
            for category in categories_data:
                ProfileCategory.objects.create(profile=instance, **category)

        if languages_data:
            ProfileLanguage.objects.filter(profile=instance).delete()
            for language in languages_data:
                ProfileLanguage.objects.create(profile=instance, **language)

        if availabilities_data:
            Availability.objects.filter(profile=instance).delete()
            for availability in availabilities_data:
                Availability.objects.create(profile=instance, **availability)

        if profile_photo_data:
            Resource.objects.filter(profile=instance, resource_type='profile_photo').delete()
            Resource.objects.create(profile=instance, resource_type='profile_photo', **profile_photo_data)

        return instance
    
    def validate_email(self, value):
        if value and Profile.objects.filter(email=value).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise serializers.ValidationError("A profile with this email already exists.")
        return value

    def validate_phone_number(self, value):
        if value and Profile.objects.filter(phone_number=value).exclude(pk=self.instance.pk if self.instance else None).exists():
            raise serializers.ValidationError("A profile with this phone number already exists.")
        return value
    
    def get_profile_photo_url(self, obj):
        photo = Resource.objects.filter(profile=obj, resource_type='profile_photo').first()
        return photo.thumbnail_url if photo else None


class ProfileCategorySerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = ProfileCategory
        fields = ['id', 'category', 'category_name', 'profile', 'years_of_experience']
        

class ProfileLanguageSerializer(serializers.ModelSerializer):
    language_name = serializers.CharField(source='language.name', read_only=True)

    class Meta:
        model = ProfileLanguage
        fields = ['id', 'language', 'language_name', 'profile', 'proficiency', 'is_native']




