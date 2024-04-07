from rest_framework.permissions import IsAuthenticated


def is_authenticated(request, view):
    permission = IsAuthenticated()
    if not permission.has_permission(request, view):
        view.permission_denied(
            request,
            message=getattr(permission, 'message', None),
            code=getattr(permission, 'code', None)
        )
    return