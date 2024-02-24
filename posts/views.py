from django.shortcuts import render, redirect
from .forms import PostForm
from .models import PostModel

# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.cleaned_data.get("post")
            book_name = post_form.cleaned_data.get("book_name")
            book_author = post_form.cleaned_data.get("book_author")
            post_type = post_form.cleaned_data.get("post_type")
            author = request.user.account
            post_instance = PostModel.objects.create(
                post=post,
                author=author,
                book_name=book_name,
                book_author=book_author,
                post_type=post_type,
            )
            return redirect('home')
    else:
        post_form = PostForm()
    return render(request, 'post_form.html', {'form': post_form, 'type':'Add Post'})