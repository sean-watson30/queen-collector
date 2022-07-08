from django.contrib import admin
from .models import Queen, Category, LipSyncs, Photo

# Register your models here.
admin.site.register(Queen)
admin.site.register(LipSyncs)
admin.site.register(Category)
admin.site.register(Photo)
