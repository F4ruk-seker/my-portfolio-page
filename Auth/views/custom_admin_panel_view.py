from django.shortcuts import redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from Auth.models import OTPDevice
from Account.models import CustomUserModel

from base.models.pages import AdminLoginPage
from base.functions.view_counter_ruler import ViewCountWithRule


class ViewCounter(ViewCountWithRule):
    def __init__(self, page, request):
        super().__init__(page, request)

    def can(self):
        return True

    def can_ban(self):
        pass  #


class CustomAdminLogin(LoginView):
    form_class = AuthenticationForm
    authentication_form = None
    template_name = "admin/customized-login-admin.html"
    redirect_authenticated_user = False
    extra_context = None

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        login(self.request, form.get_user())
        # self.request.session.__setitem__('session_authorization',False)
        return redirect('otp-admin')

    def get(self, request, *args, **kwargs):
        page = AdminLoginPage.objects.first()
        if page is not None:
            counter = ViewCounter(page, self.request)
            counter()
        return super().get(request, *args, **kwargs)

