from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from cbv.models import Post
from django.shortcuts import get_object_or_404
from django.db.models import F
# Create your views here.

class Ex2View(TemplateView):
    template_name = 'ex2.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.get(id=1)
        context['data'] = "context data for Ex2"
        return context

class PostPreLoadTaskView(RedirectView):
    pattern_name = 'singlepost'

    def get_redirect_url(self, *args, **kwargs):
        # post = get_object_or_404(Post, pk=kwargs['pk'])
        # post.count = f('count') +1
        # post.save()

        post = Post.objects.filter(pk=kwargs['pk'])
        post.update(count=F('count') + 1)

        return super().get_redirect_url(*args, **kwargs)
    

class SinglePostView(TemplateView):
    template_name = 'ex4.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        return context