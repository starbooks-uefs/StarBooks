from django.urls import path
from .views import BookSubmissionView, AdminSubmissionsListView, SubmissionListCreateView, SubmissionRetrieveUpdateDestroyView, ApproveSubmissionView, DisapproveSubmissionView

urlpatterns = [
    path('submissions/create/', BookSubmissionView.as_view(), name='submission-book'),
    path('submissions/admin/<int:id_admin>/', AdminSubmissionsListView.as_view(), name='admin-submissions-by-id'),
    path('submissions/', SubmissionListCreateView.as_view(), name='submissions-list-create'),
    path('submissions/<int:pk>/', SubmissionRetrieveUpdateDestroyView.as_view(), name='submissions-retrieve-update-destroy'),
    path('submissions/approve/<int:pk>/', ApproveSubmissionView.as_view(), name='submission-approve'),
    path('submissions/disapprove/<int:pk>/', DisapproveSubmissionView.as_view(), name='submission-disapprove'),
]
