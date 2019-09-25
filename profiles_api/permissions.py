from rest_framework import permissions


class updateOwnProfile(permissions.BasePermission):
    """ allow users to edit their own profile"""

    def has_object_permission(self,request,view,obj):
        """check user is trying to edit their own profile """
        if request.method in permissions.SAFE_METHODS:
            """safe method is the one which is just reading (GET) call and not updating anything """
            return True

        return obj.id == request.user.id
