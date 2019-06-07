from django.db import models
import json

# Create your models here.

class VisDoc(models.Model):
    name = models.CharField(max_length=64)
    text = models.TextField()
    date_created = models.DateTimeField()
    word_count = models.IntegerField('Word Count', default=0)
    para_count = models.IntegerField('Paragraph Count', default=0)
    sent_count = models.IntegerField('Sentence Count', default=0)
    avg_word_len = models.FloatField('Average Word Length', default=0)
    nouns = models.IntegerField('Number of nouns', default=0)
    verbs = models.IntegerField('Number of verbs', default=0)
    adj = models.IntegerField('Number of Adjectives', default=0)
    adv = models.FloatField('Number of Adverbs', default=0)
    coord_conj = models.IntegerField('Number of Coordinating Conjunctions', default=0)
    personal_pro = models.IntegerField('Number of Personal Pronouns', default=0)
    superlative = models.IntegerField('Number of superlatives', default=0)
    most_common_words = models.TextField()
    most_common_long_words = models.TextField()
    lexical_density = models.FloatField(default=0)
    lexical_diversity = models.FloatField(default=0)

    def para_len(self):
        return(self.word_count/self.para_count)

    def sent_len(self):
        return(self.word_count/self.sent_count)

    def percent_nouns(self):
        return((self.nouns/self.word_count) * 100)

    def percent_verbs(self):
        return((self.verbs/self.word_count) * 100)

    def percent_adj(self):
        return((self.adj/self.word_count) * 100)

    def percent_adv(self):
        return((self.adv/self.word_count) * 100)

    def most_common_words_as_obj(self):
        return(json.loads(self.most_common_words))

    def most_common_long_words_as_obj(self):
        return(json.loads(self.most_common_long_words))
