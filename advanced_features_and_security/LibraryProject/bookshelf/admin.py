from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser
from django.apps import AppConfig

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    

class CustomUserAdmin(UserAdmin):
    
    model = CustomUser
    list_display = ("email", "first_name", "last_name", "date_of_birth", "is_staff", "is_superuser")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Information", {"fields": ("first_name", "last_name", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "first_name", "last_name", "date_of_birth", "profile_photo", "password1", "password2"),
        }),
    )

class BookshelfConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "bookshelf"

    def ready(self):
        import bookshelf.signals

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Book, BookAdmin)