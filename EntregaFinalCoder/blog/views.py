from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

from django.db.models import Q

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from blog.models import Blog

class BlogListView(ListView):
    model = Blog
    template_name = "blog/blog_list.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Blog.objects.filter(Q(author__username__icontains=query) | Q(title__icontains=query) | Q(subtitle__icontains=query)).distinct()
        else:
            object_list = Blog.objects.all()
        return object_list


def BlogLike(request, slug):
    post = get_object_or_404(Blog, slug=request.POST.get('blog_slug'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse("blog_detail", kwargs={"slug": slug}))


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Blog, slug=self.kwargs['slug'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    success_url = reverse_lazy('blog_view')
    fields = ["title", "subtitle", "body", "image"]
    template_name = "blog/blog_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    success_url = reverse_lazy('blog_view')
    fields = ["title", "subtitle", "body", "image"]
    template_name = "blog/blog_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_view')
    template_name = "blog/blog_confirm_delete.html"