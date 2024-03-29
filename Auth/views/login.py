from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from Auth.models import AuthToken
from Auth.forms import user_login_form
from base.functions.view_counter_ruler import ViewCountWithRule
from base.models.pages import AdminLoginPage


class ViewCounter(ViewCountWithRule):
    def __init__(self, page, request):
        super().__init__(page, request)

    def can(self):
        return True


class LoginView(View):
    @staticmethod
    def get_auth_token(token):
        pass

    def get(self, request):
        if page := AdminLoginPage.objects.first():
            counter = ViewCounter(page, self.request)
            counter()
        if request.user.is_authenticated:
            # return redirect('Data:data_list')
            return redirect('home')
        else:
            token = request.GET.get('AuthToken')
            if token:
                try:
                    _token = AuthToken.objects.get(token=token)
                    if _token:
                        meta = request.META
                        _token.usage = f"{meta.get('REMOTE_ADDR')},"
                        _token.save()
                        login(request, _token.user)
                        return redirect('home')
                except:
                    return render(request, template_name='login.html')
            else:
                return render(request, template_name='login.html')

    def post(self, request):

        counter = ViewCounter(AdminLoginPage.objects.first(), self.request)
        counter()

        form = user_login_form(request.POST or None)
        if form.is_valid():
            user = authenticate(
                request,
                username=form.cleaned_data.get('name_or_email'),
                password=form.cleaned_data.get('password')
            )
            if user:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "login error")
                return redirect("Auth:login")
        else:
            # return render(request,template_name='login.html')
            return redirect('Auth:login')

