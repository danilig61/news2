# Generated by Django 4.2.2 on 2023-06-22 14:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_alter_article_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='news',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='news',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]
