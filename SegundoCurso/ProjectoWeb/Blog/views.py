from django.shortcuts import render
from Blog.models import Categoria, Post

# Create your views here.


def blog(request):
    blogs= Post.objects.all()
    return render(request, "blog/blog.html", {"blogs":blogs})

def categoria(request, categoria_id):
    cat= Categoria.objects.get(id= categoria_id)
    blogs=Post.objects.filter(categorias=cat)
    return render(request, "blog/categorias.html", {"categorias":cat, "blogs":blogs})