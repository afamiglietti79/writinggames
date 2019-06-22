from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse

from .forms import EnrollForm
from .models import course, roll

# Create your views here.

class enroll(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        form = EnrollForm()
        return render(request, 'course/enroll.html', { 'form': form })

    def post(self, request):
        form = EnrollForm(request.POST)
        new_roll = roll()
        if form.is_valid():
            try:
                my_course = course.objects.get(secret_code = form.cleaned_data['secret_code'])
            except (KeyError, course.DoesNotExist):
                return render(request, 'course/enroll.html', { 'form': form, 'error_message':'code not found!'})
            else:
                new_roll.course = my_course
                new_roll.user = request.user
                new_roll.is_active = True
                new_roll.save()
                return HttpResponseRedirect(reverse('home:index'))
