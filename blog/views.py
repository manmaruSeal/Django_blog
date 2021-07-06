from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    #queryset
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    
    #モデルとテンプレの紐づけ
    return render(request, 'blog/post_list.html', {'posts': posts})