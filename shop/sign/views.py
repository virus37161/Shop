from shop_app.models import User
from django.views.generic.edit import UpdateView

from django.shortcuts import render
from django.shortcuts import redirect

class ConfirmUser (UpdateView):
    model = User
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = User.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active = True)
                user.update(code = None)
            else:
                return render(self.request, 'account/invalid_code.html')
        return redirect('/main')
