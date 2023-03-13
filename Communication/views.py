from django.shortcuts import render
from django.views.generic import FormView
from .forms import NewMessageForm
from django.urls import reverse_lazy


class NewMessage(FormView):
    template_name = 'contact.html'
    form_class = NewMessageForm
    success_url = reverse_lazy('message-new')

    def get_context_data(self, **kwargs):
        form = self.get_form()
        kwargs['SubjectOptions'] = form.fields['Subject'].choices
        return super().get_context_data(**kwargs)

    def get(self,*args,**kwargs):
        return super().get(args,kwargs)

    # def post(self, request, *args, **kwargs):
    #
    #     form = self.get_form()
    #     if form.is_valid():
    #         return self.form_valid(form)
    #     else:
    #         print(form.messages)
    #         return self.form_invalid(form)

    def form_valid(self, form):
        response = super().form_valid(form)
        form = form.save(commit=False)
        form.sender_detail = {
            'HTTP_SEC_CH_UA':self.request.META.get('HTTP_SEC_CH_UA',None),
            'HTTP_SEC_CH_UA_MOBILE':self.request.META.get('HTTP_SEC_CH_UA_MOBILE',None),
            'HTTP_SEC_CH_UA_PLATFORM':self.request.META.get('HTTP_SEC_CH_UA_PLATFORM',None),
            'HTTP_ACCEPT_LANGUAGE':self.request.META.get('HTTP_ACCEPT_LANGUAGE',None),
            'REMOTE_ADDR':self.request.META.get('REMOTE_ADDR',None)
        }
        form.save()
        print("ACEPTED")

        return response



# Create your views here.


"""
HTTP_SEC_CH_UA "Not_A Brand";v="99", "Brave";v="109", "Chromium";v="109"
HTTP_SEC_CH_UA_MOBILE ?0
HTTP_SEC_CH_UA_PLATFORM "Windows"
HTTP_ACCEPT_LANGUAGE tr-TR,tr
REMOTE_ADDR 127.0.0.1
"""