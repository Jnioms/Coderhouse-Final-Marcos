from django.urls import reverse_lazy

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


class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = "blog/blog_detail.html"

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