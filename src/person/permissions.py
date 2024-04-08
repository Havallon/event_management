from rest_framework import status
from person.choices import PersonRole


def is_admin(request, view):
    has_permission = request.user and request.user.is_authenticated and request.user.role == PersonRole.admin
    if not has_permission:
        view.permission_denied(
            request,
            message='You do not have permission to perform this action.',
            code=status.HTTP_403_FORBIDDEN
        )
