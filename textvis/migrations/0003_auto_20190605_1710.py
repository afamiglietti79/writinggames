# Generated by Django 2.2.1 on 2019-06-05 17:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('textvis', '0002_visdoc_doc_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visdoc',
            old_name='doc_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='visdoc',
            old_name='doc_text',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='visdoc',
            name='doc_date',
        ),
        migrations.AddField(
            model_name='visdoc',
            name='avg_adj_sent',
            field=models.FloatField(default=0, verbose_name='Average Adjectives per Sentence'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='avg_adv_sent',
            field=models.FloatField(default=0, verbose_name='Average Adjectives per Sentence'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='avg_nouns_sent',
            field=models.FloatField(default=0, verbose_name='Average Nouns per Sentence'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='avg_para_len',
            field=models.IntegerField(default=0, verbose_name='Average Paragraph Length'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='avg_sent_len',
            field=models.IntegerField(default=0, verbose_name='Average Sentence Length'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='avg_verbs_sent',
            field=models.FloatField(default=0, verbose_name='Average Verbs per Sentence'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='avg_word_len',
            field=models.IntegerField(default=0, verbose_name='Average Word Length'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visdoc',
            name='most_common_long_words',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visdoc',
            name='most_common_words',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='visdoc',
            name='no_cc_sents',
            field=models.IntegerField(default=0, verbose_name='Sentences with Coordinating Conjunction'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='no_pp_sents',
            field=models.IntegerField(default=0, verbose_name='Sentences with Personal Pronoun'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='no_sc_sents',
            field=models.IntegerField(default=0, verbose_name='Sentences with Superlative or Comparative'),
        ),
    ]
