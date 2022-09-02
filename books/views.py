from re import template
from django.shortcuts import render
from books.models import Book
from django.views.generic import TemplateView, DetailView, ListView, FormView, CreateView, UpdateView
from django.db.models import F
from django.utils import timezone
from books.forms import AddForm
# Create your views here.
class IndexView(ListView):
    model = Book
    template_name = 'home.html'
    context_object_name = 'books'
    paginate_by = 4

    # def get_queryset(self):
    #     return Book.objects.all()[:3]





class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Book.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count')+1)
        context['time'] = timezone.now()
        return context

class GenreView(ListView):
    model=Book
    template_name="home.html"
    context_object_name = 'books'
    paginate_by = 2
    def get_queryset(self, *args, **kwargs):
        return Book.objects.filter(genre__icontains = self.kwargs.get('genre'))

# class AddBookView(FormView):
#     template_name='add.html'
#     form_class = AddForm
#     success_url = '/books/'

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)


class AddBookView(CreateView):
    model = Book
    template_name = 'add.html'
    success_url = '/books/'
    form_class = AddForm
    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['title'] = 'Enter Title'
        return initial

class AddEditView(UpdateView):
    model = Book
    template_name = 'add.html'
    form_class = AddForm
    success_url = '/books/'
