from django.urls import path, include
from .views import (
    TraineeListView,
    TraineeDetailView,
    TraineeDeleteView,
    TraineeCreateView,
    TraineeUpdateView
)
from rest_framework.routers import DefaultRouter
from trainee import views

router = DefaultRouter()
router.register(r'trainees', views.TraineeViewSet)

urlpatterns = [
    path('', TraineeListView.as_view(), name='traineeList'),
    path('detail/<int:pk>', TraineeDetailView.as_view(), name='traineeDetail'),
    path('delete/<int:pk>', TraineeDeleteView.as_view(), name='deleteTrainee'),
    path('addTrainee', TraineeCreateView.as_view(), name="addTrainee"),
    path('updateTrainee/<int:pk>', TraineeUpdateView.as_view(), name="updateTrainee"),
    path('', include(router.urls)),
    path('trainees/', views.TraineeListCreateView.as_view(), name='trainee-list-create'),
    path('trainees/<int:pk>/', views.TraineeRetrieveUpdateDestroyView.as_view(), name='trainee-retrieve-update-destroy'),
    path('track-update/<int:pk>/', views.track_update, name='track-update'),
]