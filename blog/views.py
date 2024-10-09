from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post 
from django.http import Http404

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "blog/index.html"
    paginate_by = 6

def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)

    try:
        post = get_object_or_404(queryset, slug=slug)
        print(post)  # Print the post object to the console
    except Http404:
        print(f"Post with slug '{slug}' does not exist.")  # Add this line to log the missing slug
        raise  # Re-raise the exception to show the standard 404 page

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )
