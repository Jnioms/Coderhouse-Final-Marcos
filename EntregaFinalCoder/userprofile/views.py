from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy

from userprofile.forms import SignUpForm, UserEditForm
from userprofile.models import UserProfile

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def Signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'userprofile/signup.html', {'form': form})

@login_required
def EditUser(request):

    if request.method == "GET":
        form = UserEditForm(initial={"email": request.user.email,
                            "first_name": request.user.first_name, "last_name": request.user.last_name})
        return render(request, "userprofile/edit_user.html", {"form": form})
    else:
        form = UserEditForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data

            userdata = request.user

            userdata.email = data["email"]
            userdata.password1 = data["password1"]
            userdata.password2 = data["password2"]
            userdata.first_name = data["first_name"]
            userdata.last_name = data["last_name"]

            userdata.save()
            return redirect("profile_index")
        else:
            return render(request, "userprofile/edit_user.html", {"form": form})


class UserDetail(DetailView):
    model = UserProfile
    template_name = "userprofile/index.html"

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UserProfile
    success_url = reverse_lazy('profile_index')
    fields = ["userbio", "image"]
    template_name = "userprofile/edit_user.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author or self.request.user.is_staff:
            return True
        return False

def ProfileIndex(request):

    obj = get_object_or_404(UserProfile, username_id=request.user.id)

    return redirect(obj)

