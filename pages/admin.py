from django.contrib import admin

from pages.models import Home

class HomeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Home, HomeAdmin)