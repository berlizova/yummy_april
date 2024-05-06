from django.contrib import admin
from .models import DishCategory, Dish, RestaurantStaff
from django.utils.safestring import mark_safe

# Register your models here.
@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_visible', 'sort')
    lis_editable = ('name', 'is_visible', 'sort')
    list_filter = ('is_visible',)
    search_fields = ('name',)

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag', 'name', 'price', 'is_visible', 'sort', 'category')
    list_editable = ('price', 'is_visible', 'sort')
    list_filter = ('category', 'is_visible',)
    list_fields = ('name', 'description')

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50px' height='50px'")

    photo_src_tag.short_description = 'Dish_photo'


@admin.register(RestaurantStaff)
class RestaurantStaffAdmin(admin.ModelAdmin):
    list_display = ('photo_src_tag','name', 'position', 'is_visible')
    list_editable = ('position', 'is_visible')
    list_filter = ('position', 'is_visible')
    list_fields = ('name',)

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f"<img src='{obj.photo.url}' width='50px' height='50px'")

    photo_src_tag.short_description = 'Staff_photo'
