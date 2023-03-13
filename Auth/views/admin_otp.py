from django.views.generic import View
from django.shortcuts import redirect
from django.shortcuts import render
from Auth.models import OTPDevice
import pyotp


class OTPView(View):
    template_name = "admin/otp.html"

    def get(self,request):
        if request.user.is_authenticated and not request.user.is_superuser:
            return render(request,template_name = "admin/otp.html")
        elif request.user.is_authenticated and request.user.is_superuser:
            return redirect('admin:index')
        else:
            return redirect('login')

    def post(self,request):
        user = request.user

        otp_code = request.POST.get('otp', None)
        if user.is_authenticated and not user.is_superuser and otp_code:
            otp_models = OTPDevice.objects.filter(user_id=user.id)
            for otp_model in otp_models:
                if otp_model.is_active:
                    totp = pyotp.TOTP(otp_model.hash_gen)
                    if totp.verify(otp_code):  # => True
                        user.is_superuser = True
                        user.save()
                        return redirect('admin:index')

            return render(request,template_name="admin/otp.html")
        else:
            return render(request, template_name="admin/otp.html")
