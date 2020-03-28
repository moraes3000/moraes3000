from django.urls import path
from blog.views.blog import HomeTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='HomeTemplateView'),

]
