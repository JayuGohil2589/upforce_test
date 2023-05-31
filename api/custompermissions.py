from rest_framework.permissions import BasePermission


class isPrivateBlogsAccessible(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        return False


class isReadWriteUpdateDeletePermitted(BasePermission):
    def has_object_permission(self, request, view, obj):
        if (
            request.method == "PATCH"
            or request.method == "PUT"
            or request.method == "DELETE"
        ):
            if request.user == obj.author:
                return True
            return False
        return True


class isReadAndCreateAndDeleteOnlyPermitted(BasePermission):
    def has_permission(self, request, view):
        if (
            request.method == "GET"
            or request.method == "POST"
            or request.method == "DELETE"
        ):
            return True
        return False
