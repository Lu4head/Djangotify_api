from django.urls import path
from reviews.views import ReviewListCreateView, ReviewRetrieveUpdateDeleteView

urlpatterns = [
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create-view'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDeleteView.as_view(), name='review-detail-view'),
]
