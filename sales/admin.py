# -*- coding: utf-8 -*-
from django.contrib import admin

from sales import models


class AgreementItemInline(admin.TabularInline):
    model = models.AgreementItem
    autocomplete_fields = ["good"]


class AgreementTaskInline(admin.TabularInline):
    model = models.AgreementTask


@admin.register(models.TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ["name", "created", "edited"]


@admin.register(models.AgreementItem)
class AgreementItemAdmin(admin.ModelAdmin):
    list_display = ["agreement", "good", "count"]


@admin.register(models.AgreementTask)
class AgreementTaskAdmin(admin.ModelAdmin):
    list_display = ["contragent", "status", "created", "date", "is_active"]
    date_hierarchy = "date"
    list_filter = [
        "status",
    ]
    search_fields = [
        "agreement__contragent",
    ]
    list_filter = [
        "status__name",
    ]


@admin.register(models.Agreement)
class AgreementAdmin(admin.ModelAdmin):
    inlines = [AgreementItemInline, AgreementTaskInline]
    list_display = [
        "contragent",
        "result",
        "task_status",
        "task_desc",
        "created",
        "edited",
    ]
    list_filter = [
        "result",
    ]
    search_fields = ["contragent__name"]
    autocomplete_fields = ["contragent"]
