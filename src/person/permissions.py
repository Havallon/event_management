from rest_framework import status
from rest_framework.permissions import BasePermission
from person.choices import PersonRole


class AdminPermission(BasePermission):

    def has_permission(self, request, view):
        has_permission = bool(request.user and request.user.is_authenticated and request.user.role == PersonRole.admin)
        return has_permission


def is_admin(request, view):
    permission = AdminPermission()
    has_permission = permission.has_permission(request, view)
    if not has_permission:
        view.permission_denied(
            request,
            message='You do not have permission to perform this action.',
            code=status.HTTP_403_FORBIDDEN
        )
