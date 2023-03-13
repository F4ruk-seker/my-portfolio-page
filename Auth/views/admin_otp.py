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
        if user.is_authenticated and not user.is_superuser:
            otp_model = OTPDevice.objects.get(user_id=user.id)
            otp_code = request.POST.get('otp',None)
            if otp_model and otp_code:
                totp = pyotp.TOTP(otp_model.hash_gen)
                if totp.verify(otp_code):  # => True
                    user.is_superuser = True
                    user.save()
                    return redirect('admin:index')

            return render(request,template_name = "admin/otp.html")
        else:
            return render(request, template_name="admin/otp.html")