from django.shortcuts import render
from django.views.generic import ListView

from posts.models import Post


class HomePageView(ListView):
    template_name = 'home.html'
    model = Post
