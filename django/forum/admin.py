from django.contrib import admin
from .models import Board, Post, Thread


class ForumModelAdmin(admin.ModelAdmin):
    exclude = ("created_at", "updated_at", "created_by", "updated_by")

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    def __init__(self, model, admin_site):
        self.list_display = [
            field.name for field in model._meta.fields
        ]
        super(ForumModelAdmin, self).__init__(model, admin_site)


admin.site.register(Board, ForumModelAdmin)
admin.site.register(Post, ForumModelAdmin)
admin.site.register(Thread, ForumModelAdmin)

