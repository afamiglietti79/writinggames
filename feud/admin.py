from django.contrib import admin

from .models import Prompt, Response

# Register your models here.

class promptAdmin(admin.ModelAdmin):
    fields = ['name', 'secret_code', 'start_date', 'time_offered']

class responseAdmin(admin.ModelAdmin):
    fields = ['text', 'creator', 'votes']

admin.site.register(Prompt, promptAdmin)
admin.site.register(Response, responseAdmin)
