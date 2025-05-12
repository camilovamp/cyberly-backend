import django_filters
from profiles.models import Profile

class ProfileFilter(django_filters.FilterSet):
    gender = django_filters.CharFilter(field_name='gender', lookup_expr='iexact')
    online = django_filters.BooleanFilter(field_name='online')
    languages = django_filters.NumberFilter(method='filter_by_language')
    categories = django_filters.NumberFilter(method='filter_by_category')
    experience = django_filters.NumberFilter(method='filter_by_experience')
    availability_date = django_filters.DateFilter(method='filter_by_availability_date')
    availability_time = django_filters.TimeFilter(method='filter_by_availability_time')

    class Meta:
        model = Profile
        fields = ['gender', 'online']

    def filter_by_language(self, queryset, name, value):
        return queryset.filter(languages__language_id=value)

    def filter_by_category(self, queryset, name, value):
        return queryset.filter(user_categories__category_id=value)

    def filter_by_experience(self, queryset, name, value):
        return queryset.filter(user_categories__years_of_experience__gte=value)

    def filter_by_availability_date(self, queryset, name, value):
        return queryset.filter(availabilities__date_start__lte=value, availabilities__date_end__gte=value)

    def filter_by_availability_time(self, queryset, name, value):
        return queryset.filter(availabilities__time_start__lte=value, availabilities__time_end__gte=value)
