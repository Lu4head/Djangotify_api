from django.urls import path
from performers.views import PerformerListCreateView, PerformerRetrieveUpdateDeleteView

urlpatterns = [
    path('performers/', PerformerListCreateView.as_view(), name='performer-list-create-view'),
    path('performers/<int:pk>/', PerformerRetrieveUpdateDeleteView.as_view(), name='performer-detail-view'),
]
