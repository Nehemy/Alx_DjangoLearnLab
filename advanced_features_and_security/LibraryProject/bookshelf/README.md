# Permissions and Groups in Bookshelf App

## Custom Permissions
Four custom permissions for the `Book` model:
- `can_view`: Allows viewing books.
- `can_create`: Allows creating books.
- `can_edit`: Allows editing books.
- `can_delete`: Allows deleting books.

## Groups and Permissions
We set up the following groups:
- **Viewers**: Can only view books (`can_view`).
- **Editors**: Can view, create, and edit books (`can_view`, `can_create`, `can_edit`).
- **Admins**: Can perform all actions (`can_view`, `can_create`, `can_edit`, `can_delete`).

## Enforcing Permissions in Views
- Permissions are checked using `@permission_required` decorators.
- Users are required to log in to access views.
- Unauthorized users see an error message.

## How to Test
1. Run `python manage.py migrate` to apply database changes.
2. Go to Django Admin and create users.
3. Assign users to groups under **Groups**.
4. Log in with different users and attempt to access views.

**Now the bookshelf app has a secure permission-based access control system**
