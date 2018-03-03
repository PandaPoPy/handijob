from django.contrib import admin

from offers.models import Offer, Enterprise


class OfferAdmin(admin.ModelAdmin):
    pass

admin.site.register(Offer, OfferAdmin)


class EnterpriseAdmin(admin.ModelAdmin):
    pass

admin.site.register(Enterprise, EnterpriseAdmin)


# class ApplianceAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(Appliance, ApplianceAdmin)
