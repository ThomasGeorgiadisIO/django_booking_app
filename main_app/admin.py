from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(EndUser)
admin.site.register(TourGuide)
admin.site.register(TourExperience)
admin.site.register(OrderDetail)
admin.site.register(WishList)