from django.urls import path
from .views import IndexView, BookDetailView, GenreView, AddBookView, AddEditView
app_name='books'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('add/', AddBookView.as_view(), name="add"),
    path('g/<str:genre>', GenreView.as_view(), name="genre"),
    path('<slug:slug>/', BookDetailView.as_view(), name="book_detail"),
    path('<slug:slug>/edit', AddEditView.as_view(), name="edit_detail"),


]
