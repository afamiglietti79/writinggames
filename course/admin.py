from django.contrib import admin

from .models import course, roll

# Register your models here.

class courseAdmin(admin.ModelAdmin):
    fields = ['name', 'secret_code', 'start_date', 'time_offered']

class rollAdmin(admin.ModelAdmin):
    fields = ['course', 'user','is_active']

admin.site.register(roll, rollAdmin)
admin.site.register(course, courseAdmin)
