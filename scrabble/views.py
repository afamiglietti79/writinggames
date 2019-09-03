from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils import timezone
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import nltk
from nltk.corpus import wordnet
from .forms import ScrabbleForm

# Create your views here.

class ScrabbleResponse(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        sentence = "This sentence will demonstrate my technology"
        tokens = nltk.word_tokenize(sentence)
        choice_dict = {}
        for word in tokens:
            syns = wordnet.synsets(word)
            raw_syns = []
            for syn in syns:
                raw_syns.extend([l.name() for l in syn.lemmas()])
            synset = set(raw_syns)
            choiceset = [(choice, choice) for choice in synset]
            choice_dict[word] = choiceset
        form = ScrabbleForm(customchoices=choice_dict)
        return render(request, 'scrabble/sresponse.html', {'form':form} )
