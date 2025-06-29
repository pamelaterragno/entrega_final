from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.views.generic import ListView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

def home(request):
    return render(request, 'home.html')


class PostListView(ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'



class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

def about_me(request):
    return render(request, 'sobremi.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('list')
    else:
        form = PostForm()
    return render(request, 'crear.html', {'form': form})


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = PostForm(instance=post)
    return render(request, 'editar.html', {'form': form})


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('list')

@login_required
def perfil(request):
    return render(request, 'perfil.html')


@login_required
def profile(request):
    return render(request, 'profile.html')
