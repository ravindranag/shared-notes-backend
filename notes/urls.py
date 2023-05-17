from django.urls import path
from .views import NoteListView


urlpatterns = [
    path('', NoteListView.as_view()),
	path('create/', NoteListView.as_view()),
	path('<int:pk>/', NoteListView.as_view()),
]
