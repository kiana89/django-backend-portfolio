from django.contrib import admin
from .models import CollaborationRequest

@admin.register(CollaborationRequest)
class CollaborationRequestAdmin(admin.ModelAdmin):
    list_display = ('person_type', 'full_name', 'company_name', 'email', 'phone', 'subject', 'message', 'create_at', 'update_at', 'is_read',)
    list_filter = ('person_type','is_read','create_at',)
    search_fields = ('full_name','company_name','email','subject',)
