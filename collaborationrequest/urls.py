from django.urls import path
from .views import CollaborationRequestDetailsView, CollaborationRequestListCreateView

urlpatterns = [
    path('', CollaborationRequestListCreateView.as_view()),
    path('<int:pk>', CollaborationRequestDetailsView.as_view()),
]