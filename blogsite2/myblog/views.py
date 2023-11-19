from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import JsonResponse

# Create your views here.
def index(request):
    post = Post.objects.all()
    return render(request, 'index.html', {'Post': post})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'myblog/post_detail.html', {'post': post})

def category_posts(request, category_id):
    category = get_object_or_404(category, pk=category_id)
    posts = Post.objects.filter(category=category).select_related('author', 'category')
    return render(request, 'myblog/category_posts.html', {'category': category, 'posts': posts})

def tag_posts(request, tag_id):
    tag = get_object_or_404(Tag, pk=tag_id)
    posts = Post.objects.filter(tags=tag).select_related('author', 'category')
    return render(request, 'myblog/tag_posts.html', {'tag': tag, 'posts': posts})
    
def ultima_publicacion(request):
    ultima_publicacion = Publicacion.objects.latest('fecha_publicacion')
    return render(request, 'index.html', {'ultima_publicacion': ultima_publicacion})

def detalle_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, pk=publicacion_id)
    data = {
        'titulo': publicacion.titulo,
        'contenido': publicacion.contenido,
        'fecha_publicacion': publicacion.fecha_publicacion.strftime('%Y-%m-%d %H:%M:%S'),
    }
    return JsonResponse(data)