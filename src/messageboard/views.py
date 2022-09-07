from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from messageboard.models import Messages
from django.urls import reverse_lazy

class MessageListView(ListView):
    model = Messages
    template_name = "messageboard/messages_list.html"

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Messages
    success_url = reverse_lazy('message_view')
    fields = ["body"]
    template_name = "messageboard/messages_edit.html"

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

class MessageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Messages
    success_url = reverse_lazy('message_view')
    fields = ["body"]
    template_name = "messageboard/messages_edit.html"

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.username or self.request.user.is_staff:
            return True
        return False

class MessageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Messages
    success_url = reverse_lazy('message_view')
    template_name = "messageboard/messages_confirm_delete.html"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.username or self.request.user.is_staff:
            return True
        return False