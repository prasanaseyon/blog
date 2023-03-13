from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm
from .forms import EditForm
from django.http import HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render

from django.urls import reverse_lazy, reverse
import boto3


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering=['-id']
    ordering = ['-post_date', '-post_time']


def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')



import requests
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def my_view(request):
    s3_url = 'https://my-bucket.s3.amazonaws.com/path/to/image.jpg'
    try:
        response = requests.get(s3_url)
        response.raise_for_status() # raise an exception if the response is not 2xx
        content_type = response.headers['Content-Type']
        image_data = response.content
        return HttpResponse(image_data, content_type=content_type)
    except requests.exceptions.RequestException as e:
        # log the error and return a response with an error message
        logger.error(f'Error retrieving image from S3: {e}')
        return HttpResponse('Error retrieving image', status=500)
