
from django.shortcuts import reverse
from django.shortcuts import redirect


class OTPMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        path = reverse('admin:index')
        response = self.get_response(request)
        otp_gen = request.session.get('session_authorization')# False None | True
        if request.path.startswith(path):

            if request.path == reverse("admin:login") or request.path == reverse("otp-admin") or otp_gen:
                pass
            # elif otp_gen:
            #     pass
            else:
                response = redirect(reverse("admin:login"))
                # if path == reverse("admin:login") and path == reverse("otp-admin"):
            #     pass
            # elif request.path == reverse("admin:login") or request.path == reverse("otp-admin"):
            #     pass

        return response


