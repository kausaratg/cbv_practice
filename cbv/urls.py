from django.urls import path
from cbv import views
from django.views.generic import TemplateView, RedirectView
urlpatterns=[
    path('', TemplateView.as_view(template_name="ex1.html", extra_context={'title':'custom title'}), name="ex1"), 
    path('ex2', views.Ex2View.as_view(), name="ex2"),
    path('rdt/', RedirectView.as_view(url="https://youtube.com/veryacademy"), name="go-to-very" ),
    path('ex3<str:pk>', views.PostPreLoadTaskView.as_view(), name="redirect_task" ),
    path('ex4/<str:pk>', views.SinglePostView.as_view(), name="singlepost"),
]