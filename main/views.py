from django.shortcuts import render
from django.views import View


class index(View):
    template_name = 'main/homePage.html'

    context = {

    }

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)


