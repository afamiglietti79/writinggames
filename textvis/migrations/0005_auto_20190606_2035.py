# Generated by Django 2.2.1 on 2019-06-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textvis', '0004_auto_20190606_1504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visdoc',
            name='avg_adj_sent',
        ),
        migrations.RemoveField(
            model_name='visdoc',
            name='avg_adv_sent',
        ),
        migrations.RemoveField(
            model_name='visdoc',
            name='avg_nouns_sent',
        ),
        migrations.RemoveField(
            model_name='visdoc',
            name='avg_para_len',
        ),
        migrations.RemoveField(
            model_name='visdoc',
            name='avg_sent_len',
        ),
        migrations.RemoveField(
            model_name='visdoc',
            name='avg_verbs_sent',
        ),
        migrations.RemoveField(
            model_name='visdoc',
            name='no_cc_sents',
        ),
        migrations.RemoveField(
            model_name='visdoc',
            name='no_pp_sents',
        ),
        migrations.RemoveField(
            model_name='visdoc',
            name='no_sc_sents',
        ),
        migrations.AddField(
            model_name='visdoc',
            name='adj',
            field=models.IntegerField(default=0, verbose_name='Number of Adjectives'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='adv',
            field=models.FloatField(default=0, verbose_name='Number of Adverbs'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='coord_conj',
            field=models.IntegerField(default=0, verbose_name='Number of Coordinating Conjunctions'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='lexical_density',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='lexical_diversity',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='nouns',
            field=models.IntegerField(default=0, verbose_name='Number of nouns'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='para_count',
            field=models.IntegerField(default=0, verbose_name='Paragraph Count'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='personal_pro',
            field=models.IntegerField(default=0, verbose_name='Number of Personal Pronouns'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='sent_count',
            field=models.IntegerField(default=0, verbose_name='Sentence Count'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='superlative',
            field=models.IntegerField(default=0, verbose_name='Number of superlatives'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='verbs',
            field=models.IntegerField(default=0, verbose_name='Number of verbs'),
        ),
        migrations.AddField(
            model_name='visdoc',
            name='word_count',
            field=models.IntegerField(default=0, verbose_name='Word Count'),
        ),
    ]
