from django.contrib import admin
from .models import Sections, Books, RatingStar, Rating
# Register your models here.

admin.site.register(Sections)
admin.site.register(Books)
admin.site.register(RatingStar)
admin.site.register(Rating)