from .models import Property
from django.db.models import Q

class FilterData:
    def general_filter(self, price, category, ward):
        properties = Property.objects.filter(
            Q(price__iexact = price) |
            Q(category__name__icontains = category) &
            Q(ward__name__icontains = ward),
            is_active = True,
            is_deleted = False
        )

        if properties.exists():
            return properties
        else:
            pass

    @staticmethod
    def get_properties():
        properties = Property.objects.all()
        return properties
