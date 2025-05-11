from django.db import models
from django.contrib.auth.models import User
from common.models import BaseModel
from common.constants import AVAILABILITY_TYPE_CHOICES
from common.constants import WEEKDAY_CHOICES
from common.constants import  RESOURCE_TYPE_CHOICES

class Profile(BaseModel):
    user = models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    display_name = models.CharField(max_length=32, null=True, blank=True)
    email = models.EmailField(max_length=64, null=True, blank=True)
    phone_number = models.CharField(max_length=45, null=True, blank=True)
    about = models.TextField(max_length=1024, null=True, blank=True)
    display_name = models.CharField(max_length=64, null=True, blank=True)
    head_line = models.CharField(max_length=255, null=True, blank=True)

    is_vendor = models.BooleanField(null=True, blank=True)
    is_adult = models.BooleanField(null=True, blank=True)
    email_verified = models.BooleanField(null=True, blank=True)
    online = models.BooleanField(null=True, blank=True)
    completed_registration = models.BooleanField(null=True, blank=True)

    created_date = models.DateTimeField(null=True, blank=True)
    time_zone = models.CharField(max_length=64, null=True, blank=True)

    def __str__(self):
        return self.display_name or f"{self.first_name} {self.last_name}"
    
class Category(BaseModel):
    name = models.CharField(max_length=64, null=True, blank=True)
    is_featured = models.BooleanField(null=True, blank=True)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return self.name or f"Category {self.name}"
    
class ProfileCategory(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='category_id', related_name='user_categories')
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, db_column='profile_id', related_name='user_categories')

    class Meta:
        db_table = 'profile_category'
        indexes = [
            models.Index(fields=['category'], name='fk_user_category_category1_idx'),
            models.Index(fields=['profile'], name='fk_user_category_profile1_idx'),
        ]
        unique_together = ('category', 'profile')  # optional constraint for uniqueness

    def __str__(self):
        return f"User {self.profile_id} - Category {self.category_id}"

    

class Availability(BaseModel):
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='availabilities')
    availability_type = models.CharField(
        max_length=1,
        choices=AVAILABILITY_TYPE_CHOICES,
        null=True,
        blank=True
    )
    repeat_on = models.CharField(
        max_length=32,
        null=True,
        blank=True,
        help_text="Comma-separated weekdays (1=Mon ... 7=Sun)"
    )
    date_start = models.DateField(null=True, blank=True)
    date_end = models.DateField(null=True, blank=True)
    time_start = models.TimeField(null=True, blank=True)
    time_end = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.profile} | {self.get_availability_type_display()}"
    
    def get_repeat_on_display(self):
        if not self.repeat_on:
            return ""
        days = self.repeat_on.split(',')
        return ', '.join(dict(WEEKDAY_CHOICES).get(day, f'Day {day}') for day in days)
    

class Resource(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    resource_type = models.CharField(max_length=50, choices=RESOURCE_TYPE_CHOICES)
    thumbnail_url = models.URLField(max_length=500, blank=True, null=True)