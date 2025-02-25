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


# Security Best Practices in LibraryProject

## 1. Configured Secure Settings
- **`DEBUG = False`** in production.
- Enforced **XSS Protection** (`SECURE_BROWSER_XSS_FILTER`).
- Clickjacking prevention with **X-Frame-Options** (`DENY`).
- **CSRF and Session cookies secured over HTTPS**.

## 2. Protected Forms Against CSRF
- **All forms include `{% csrf_token %}`** to prevent CSRF attacks.

## 3. Secure Data Access in Views
- **SQL Injection Prevention**: Queries use Django ORM, not raw SQL.
- **Django Forms Used** to validate user input safely.

## 4. Implemented Content Security Policy (CSP)
- **`django-csp`** middleware restricts JavaScript & styles to prevent XSS.

## 5. Testing Security Measures
- **Manual Testing**:
  - Ensured unauthorized users cannot access views.
  - Checked forms for CSRF protection.
  - Verified CSP headers in browser.

**Django app secured**
