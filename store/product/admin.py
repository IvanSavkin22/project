from django.contrib import admin
from .models import Category, Subcategory, Product, Lecture, Material


class LectureInline(admin.StackedInline):
    model = Lecture
    fields = ('title', 'description', 'stage')


class MaterialInline(admin.StackedInline):
    model = Material
    fields = ('title', 'text', 'file', 'material_type', 'stage')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [LectureInline]
    list_display = ('title', 'category', 'subcategory', 'price')

    class Media:
        js = ('js/admin.js',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        # Список скрываемых полей в зависимости от выбранных категорий и подкатегорий
        hidden_fields = {
            'Аксессуары': {
                'Монитор': ['id_graphics_card', 'id_processor', 'id_motherboard', 'id_ram', 'id_ssd'],
                'Клавиатуры': ['id_graphics_card', 'id_processor', 'id_motherboard', 'id_ram', 'id_ssd'],
                'Мыши': ['id_graphics_card', 'id_processor', 'id_motherboard', 'id_ram', 'id_ssd'],
                'Гарнитура': ['id_graphics_card', 'id_processor', 'id_motherboard', 'id_ram', 'id_ssd'],
            },
        }

        selected_category = obj.category.title if obj and obj.category else None
        selected_subcategory = obj.subcategory.title if obj and obj.subcategory else None

        if selected_category and selected_subcategory:
            fields_to_hide = hidden_fields.get(selected_category, {}).get(selected_subcategory, [])
            for field in fields_to_hide:
                # Скройте поля, используя CSS стиль
                form.base_fields[field].widget.attrs['style'] = 'display:none;'

        return form


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    inlines = [MaterialInline]
    list_filter = ('product__title',)


admin.site.register(Material)
admin.site.register(Category)
admin.site.register(Subcategory)
