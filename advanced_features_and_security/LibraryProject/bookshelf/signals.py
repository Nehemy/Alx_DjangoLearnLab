from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.name == "bookshelf":  # Ensure this only runs for the bookshelf app
        # Create Groups
        editors_group, _ = Group.objects.get_or_create(name="Editors")
        viewers_group, _ = Group.objects.get_or_create(name="Viewers")
        admins_group, _ = Group.objects.get_or_create(name="Admins")

        # Get permissions related to Book model
        content_type = ContentType.objects.get_for_model(Book)
        can_view = Permission.objects.get(codename="can_view", content_type=content_type)
        can_create = Permission.objects.get(codename="can_create", content_type=content_type)
        can_edit = Permission.objects.get(codename="can_edit", content_type=content_type)
        can_delete = Permission.objects.get(codename="can_delete", content_type=content_type)

        # Assign permissions to groups
        editors_group.permissions.add(can_view, can_create, can_edit)
        viewers_group.permissions.add(can_view)
        admins_group.permissions.add(can_view, can_create, can_edit, can_delete)
