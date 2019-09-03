import nltk
import json

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from django.utils.html import strip_tags
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .forms import DocForm
from .models import VisDoc

# Create your views here.

class index(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        user = request.user
        active_roll = request.user.roll_set.get(is_active = True)
        since_cleared =  timezone.now().date() - active_roll.course.last_cleared
        print(since_cleared.days)
        if since_cleared.days >= 1:
            course = active_roll.course
            all_docs = active_roll.course.visdoc_set.all()
            for doc in all_docs:
                age = timezone.now() - doc.date_created
                print(age.days)
                if age.days >=1 and doc.retained == False:
                    doc.delete()
            my_docs = user.visdoc_set.all()
            course_docs = active_roll.course.visdoc_set.all().exclude(creator=user)
            course.last_cleared = timezone.now()
            course.save()
        else:
            my_docs = user.visdoc_set.all()
            course_docs = active_roll.course.visdoc_set.all().exclude(creator=user)

        return render(request, 'textvis/index.html', {'my_docs':my_docs, 'course_docs':course_docs} )

class new(LoginRequiredMixin, View):

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    stopwords = set(nltk.corpus.stopwords.words('english'))
    formatted_text = ""


    def get(self, request):
        form = DocForm()
        return render(request, 'textvis/new.html', { 'form': form })

    def post(self, request):
        form = DocForm(request.POST)
        new_doc = VisDoc()
        if form.is_valid():
            word_len_sum = 0
            stripped = strip_tags(form.cleaned_data['text'])
            rough_words = stripped.split()


            strip_punct_tokens = [word for word in rough_words if len(word) > 1 or word.isalpha()]
            new_doc.word_count = len(strip_punct_tokens)

            total_strip = [token.lower().strip('“.”;,') for token in strip_punct_tokens if not token.isdigit()]
            new_doc.lexical_diversity = len(set(total_strip)) / len(total_strip)

            no_stop_tokens = [token for token in strip_punct_tokens if not token.lower() in self.stopwords]

            fdist = nltk.probability.FreqDist(no_stop_tokens)
            new_doc.most_common_words = json.dumps(fdist.most_common(10))

            long_words = [token for token in no_stop_tokens if len(token) > 5]

            fdist = nltk.probability.FreqDist(long_words)
            new_doc.most_common_long_words = json.dumps(fdist.most_common(10))

            paras = stripped.split('\n')
            for graf in paras:
                    if not graf.isspace():
                        new_doc.para_count = new_doc.para_count + 1
                        para_len = len(nltk.word_tokenize(graf))
                        self.formatted_text = self.formatted_text + '<p class="para length_{0}">'.format(str(para_len))
                        sentences = nltk.tokenize.sent_tokenize(graf)
                        for sent in sentences:
                            new_doc.sent_count = new_doc.sent_count + 1
                            tokens = nltk.word_tokenize(sent)
                            pos = nltk.pos_tag(tokens)
                            for pair in pos:
                                if len(pair[0]) > 1 or pair[0] == 'I' or pair[0] == 'a':
                                    word_len_sum += len(pair[0])
                                    if pair[1][0] == "N":
                                        new_doc.nouns += 1
                                    elif pair[1][0] == "V":
                                        new_doc.verbs += 1
                                    elif pair[1] == "JJS":
                                        new_doc.adj += 1
                                        new_doc.superlative += 1
                                    elif pair[1][0] == "J":
                                        new_doc.adj += 1
                                    elif pair[1][0:2] == "RB":
                                        new_doc.adv += 1
                                    elif pair[1][0:3] == "PRP":
                                        new_doc.personal_pro += 1
                                    elif pair[1] == "CC":
                                        new_doc.coord_conj +=1
                                    if pair[0] in [item[0] for item in json.loads(new_doc.most_common_words)] or pair[0] in [item[0] for item in json.loads(new_doc.most_common_long_words)]:
                                        spantag = '<span class="{0} common_word">'.format(pair[1])
                                        self.formatted_text = self.formatted_text + spantag + pair[0] + "</span> "
                                    else:
                                        spantag = '<span class="{0}">'.format(pair[1])
                                        self.formatted_text = self.formatted_text + spantag + pair[0] + "</span> "
                                elif pair[0] == "." or pair[0] == "," or pair[0] == "?" or pair[0] == "!":
                                    spantag = '<span class="punct">'
                                    self.formatted_text = self.formatted_text + spantag + pair[0] + "</span> "
                                else:
                                    self.formatted_text = self.formatted_text + pair[0]
                    self.formatted_text = self.formatted_text + "</p>"


            lexcial_count = new_doc.nouns + new_doc.verbs + new_doc.adj + new_doc.adv
            new_doc.lexical_density =  lexcial_count / new_doc.word_count

            new_doc.name=form.cleaned_data['name']
            new_doc.creator=request.user
            active_roll = request.user.roll_set.get(is_active = True)
            new_doc.host_course = active_roll.course
            new_doc.text=self.formatted_text
            new_doc.date_created=timezone.now()
            new_doc.avg_word_len = word_len_sum/new_doc.word_count
            new_doc.save()

            return HttpResponseRedirect(reverse('textvis:display', args=(new_doc.id,)))
        else:
            print('badForm')
            form = DocForm()
            return render(request, 'textvis/new.html', { 'form': form })

class display(LoginRequiredMixin, View):

        login_url = '/login/'
        redirect_field_name = 'redirect_to'

        def get(self, request, doc_id):
                doc = get_object_or_404(VisDoc, pk=doc_id)
                return render(request, 'textvis/display.html', { 'doc': doc})

@login_required(login_url='/login/')
def deleteDoc(request, doc_id):
    doc = get_object_or_404(VisDoc, pk=doc_id)
    if request.user == doc.creator:
        doc.delete()
        return HttpResponseRedirect(reverse('textvis:index'))
    else:
        return HttpResponseRedirect(reverse('textvis:index'))

@login_required(login_url='/login/')
def retainDoc(request, doc_id):
    doc = get_object_or_404(VisDoc, pk=doc_id)
    if request.user == doc.creator:
        doc.retained = True
        doc.save()
        return HttpResponseRedirect(reverse('textvis:index'))
    else:
        return HttpResponseRedirect(reverse('textvis:index'))
