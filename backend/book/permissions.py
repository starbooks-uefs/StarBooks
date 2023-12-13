# permissions.py
from rest_framework import permissions

class IsEBookOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # verificar se o usuário atual é o proprietário do e-book:
        return obj.producer == request.user.producer_profile
