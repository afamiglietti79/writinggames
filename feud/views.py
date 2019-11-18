from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils import timezone
from django.urls import reverse
from django.utils.html import strip_tags
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import json

from .models import Prompt, Response, FeudBallot
from .forms import PromptForm, ResponseForm, EditPromptForm

# Create your views here.

class index(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        user = request.user
        active_roll = request.user.roll_set.get(is_active = True)
        prompt_list = active_roll.course.prompt_set.all()
        return render(request, 'feud/index.html', {'prompt_list':prompt_list} )

class newPrompt(LoginRequiredMixin, View):

    def get(self, request):
        form = PromptForm()
        return render(request, 'feud/newprompt.html', { 'form': form })

    def post(self, request):
        form = PromptForm(request.POST)
        new_prompt = Prompt()
        if form.is_valid():
            new_prompt.name = form.cleaned_data['name']
            stripped = strip_tags(form.cleaned_data['text'])
            paragraphed_text = ""
            for graf in stripped.split('\n'):
                paragraphed_text = paragraphed_text + '<p>' + graf + '</p>'
            new_prompt.text = paragraphed_text
            new_prompt.creator = request.user

            active_roll = request.user.roll_set.get(is_active = True)
            new_prompt.host_course = active_roll.course
            new_prompt.date_created = timezone.now()
            new_prompt.save()
            return HttpResponseRedirect(reverse('feud:index'))
        else:
            return render(request, 'feud/newprompt.html', { 'form': form })


class displayPrompt(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, prompt_id):
        prompt = get_object_or_404(Prompt, pk=prompt_id)
        try:
            response = prompt.response_set.get(creator=request.user)
        except (KeyError, Response.DoesNotExist):
            form = ResponseForm()
            return render(request, 'feud/displayprompt.html', {'prompt':prompt, 'form':form })
        else:
            return HttpResponseRedirect(reverse('feud:listresponses', args=(prompt.id, )))

    def post(self, request, prompt_id):
        prompt = get_object_or_404(Prompt, pk=prompt_id)
        form = ResponseForm(request.POST)
        new_response = Response()
        if form.is_valid():
            stripped = strip_tags(form.cleaned_data['text'])
            paragraphed_text = ""
            for graf in stripped.split('\n'):
                paragraphed_text = paragraphed_text + '<p>' + graf + '</p>'
            new_response.text = paragraphed_text
            new_response.prompt = prompt
            new_response.creator = request.user
            new_response.date_created=timezone.now()
            new_response.save()
            return HttpResponseRedirect(reverse('feud:listresponses', args=(prompt.id, )))
        else:
            return render(request, 'feud/displayprompt.html', {'prompt':prompt, 'form':form })

class listResponses(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, prompt_id):
        prompt = get_object_or_404(Prompt, pk=prompt_id)
        responses = prompt.response_set.all()
        return render(request, 'feud/listresponses.html', {'prompt':prompt, 'responses':responses})

class editPrompt(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request, prompt_id):
        prompt = get_object_or_404(Prompt, pk=prompt_id)
        form = EditPromptForm(instance=prompt)
        return render(request, 'feud/editprompt.html', { 'form': form, 'prompt':prompt })

    def post(self, request, prompt_id):
        prompt = get_object_or_404(Prompt, pk=prompt_id)
        form=EditPromptForm(request.POST, instance=prompt)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('feud:index'))
        else:
            return render(request, 'feud/editprompt.html', { 'form': form, 'prompt':prompt })

@login_required(login_url='/login/')
def ajaxResponses(request, prompt_id):
    prompt = get_object_or_404(Prompt, pk=prompt_id)
    user = request.user
    if prompt.creator == request.user:
        print("instructor")
        vote_flag = "instr"
        responses = prompt.response_set.order_by('-votes')
        response_list = [{'id':r.pk, 'text': r.text, 'votes':r.votes, 'first_name':r.creator.first_name, 'last_name':r.creator.last_name } for r in responses]
    elif prompt.is_accepting_votes == prompt.WAITING_TO_VOTE:
        responses = prompt.response_set.all()
        response_list = [{'id':r.pk, 'text': r.text, 'votes':r.votes} for r in responses]
        vote_flag = "wait"
    elif prompt.is_accepting_votes == prompt.VOTING_COMPLETE or prompt.feudballot_set.filter(voter=request.user):
        vote_flag = "done"
        responses = prompt.response_set.order_by('-votes')
        response_list = [{'id':r.pk, 'text': r.text, 'votes':r.votes} for r in responses]
    else:
        vote_flag = "open"
        responses = prompt.response_set.all()
        response_list = [{'id':r.pk, 'text': r.text, 'votes':r.votes} for r in responses]
    return JsonResponse({'responses':response_list, 'vote_flag':vote_flag })

@login_required(login_url='/login/')
def toggleVoteStatus(request, prompt_id):
    prompt = get_object_or_404(Prompt, pk=prompt_id)
    if prompt.is_accepting_votes == prompt.VOTING_COMPLETE or prompt.is_accepting_votes == prompt.WAITING_TO_VOTE:
        prompt.is_accepting_votes = prompt.VOTING_OPEN
        vote_label = "Close Voting"
    else:
        prompt.is_accepting_votes = prompt.VOTING_COMPLETE
        vote_label ="Open Voting"
    prompt.save()
    return JsonResponse({'button_label': vote_label })

@login_required(login_url='/login/')
def vote(request, response_id):
    response = get_object_or_404(Response, pk=response_id)
    if not response.prompt.feudballot_set.filter(voter=request.user):
        response.votes = response.votes + 1
        print(response.votes)
        ballot = FeudBallot()
        ballot.voter = request.user
        ballot.prompt = response.prompt
        ballot.date_created = timezone.now()
        response.save()
        ballot.save()
    else:
        print("Already voted")
    return JsonResponse({'voted': True})

@login_required(login_url='/login/')
def deletePrompt(request, prompt_id):
    prompt = get_object_or_404(Prompt, pk=prompt_id)
    if request.user == prompt.creator:
        prompt.delete()
        return HttpResponseRedirect(reverse('feud:index'))
    else:
        return HttpResponseRedirect(reverse('feud:index'))
