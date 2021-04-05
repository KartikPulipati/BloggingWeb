from django.contrib import admin
from .models import blog

class blogAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
admin.site.register(blog, blogAdmin)
