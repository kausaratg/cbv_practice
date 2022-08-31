from django.urls import path
from .views import IndexView, BookDetailView, GenreView
app_name='books'
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('g/<str:genre>', GenreView.as_view(), name="genre"),
    path('<slug:slug>/', BookDetailView.as_view(), name="book_detail"),
]
