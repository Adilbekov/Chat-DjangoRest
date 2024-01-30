from django.contrib import admin
from apps.chat.models import Message, FrontMessage, BackMessage, DataScienceMessage

# Register your models here.
@admin.register(Message)
class MessageAdminFilter(admin.ModelAdmin):
    list_display = ('content',)
    list_filter = ('content',)
    search_fields = ('content', )

@admin.register(FrontMessage)
class MessageAdminFilter(admin.ModelAdmin):
    list_display = ('content', )
    list_filter = ('content', )
    search_fields = ('content', )

@admin.register(BackMessage)
class MessageAdminFilter(admin.ModelAdmin):
    list_display = ('content', )
    list_filter = ('content', )
    search_fields = ('content', )

@admin.register(DataScienceMessage)
class MessageAdminFilter(admin.ModelAdmin):
    list_display = ('content', )
    list_filter = ('content', )
    search_fields = ('content', )