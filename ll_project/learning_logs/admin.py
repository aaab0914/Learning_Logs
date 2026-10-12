from django.contrib import admin

from .models import Entry, Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["text", "date_added", "owner"]
    search_fields = ["text", "owner"]
    date_hierarchy = "date_added"


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ["topic", "text", "date_added"]
    search_field = ["topic", "text"]
