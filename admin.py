from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from college.models import Notice, Branch, Profile

# Register your models here.
class NoticeAdmin(ModelAdmin):
    list_display = ["subject", "cr_date"]
    search_fields = ["subject", "msg"]
    list_filter = ["cr_date"]
    
admin.site.register(Notice, NoticeAdmin)
admin.site.register(Branch)
admin.site.register(Profile)

