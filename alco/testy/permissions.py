# from rest_framework import permissions
# from .models import *
#
# class UpdateOnlyNews(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request,
#         # so we'll always allow GET, HEAD or OPTIONS requests.
#         if Level.status_positions == 'NE':
#
#
#         # Instance must have an attribute named `owner`.
#         return obj.user == request.user