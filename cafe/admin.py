from django.contrib import admin
from django.utils.safestring import mark_safe

from cafe.models import DishCategory, Dish, Gallery,Reservation

admin.site.register(Gallery)

admin.site.register(Reservation)
@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display_links = ('id', 'name')
    list_display = ('id', 'category', 'name', 'position', 'price', 'is_visible', 'photo_src_tag',)
    list_editable = ('category', 'position', 'price', 'is_visible')
    list_filter = ('category', 'price')
    search_fields = ('name', )

    def photo_src_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}", width=50>')

    photo_src_tag.short_description = 'Dish photo'