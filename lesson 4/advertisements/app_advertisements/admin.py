from django.contrib import admin
from .models import Advertisement

class AdvertisementAdmin(admin.ModelAdmin):
    
    list_display=["title", "description", "price", "auction", "creation_date", "updation_date"]
    actions = ["set_auction_as_false", "set_auction_as_true"]
    list_filter = ['price']
    fieldsets = (
        ('Общее', {
            'fields':('title', 'description'),
            'classes':['collapse']
        }),
        ('Финансы', {
            'fields' : ('price', 'auction'),
            'classes':['collapse']

        })
    )

    @admin.action(description = "Убрать возможность торга")
    def set_auction_as_false(self, request, queryset):
        queryset.update(auction = False)


    @admin.action(description = "Добавить возможность торга")
    def set_auction_as_true(self, request, queryset):
        queryset.update(auction = True)

admin.site.register(Advertisement, AdvertisementAdmin)


# Register your models here.
