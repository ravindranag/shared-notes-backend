from django.urls import path, include
from .views import UserView, UserDetailView


urlpatterns = [
	path('', UserView.as_view(), name='Create user'),
	path('<int:pk>/', UserDetailView.as_view())
]
