from django.urls import path
from .views import (
    TraineeListView,
    TraineeDetailView,
    TraineeDeleteView,
    TraineeCreateView,
    TraineeUpdateView
)

urlpatterns = [
    path('', TraineeListView.as_view(), name='traineeList'),
    path('detail/<int:pk>', TraineeDetailView.as_view(), name='traineeDetail'),
    path('delete/<int:pk>', TraineeDeleteView.as_view(), name='deleteTrainee'),
    path('addTrainee', TraineeCreateView.as_view(), name="addTrainee"),
    path('updateTrainee/<int:pk>', TraineeUpdateView.as_view(), name="updateTrainee"),
]