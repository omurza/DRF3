# Generated by Django 5.1.3 on 2024-11-12 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220, verbose_name='заголовк')),
                ('description', models.TextField(verbose_name='описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('pages', models.IntegerField(max_length=600, verbose_name='колво-страниц')),
                ('logo', models.ImageField(upload_to='media', verbose_name='логотип')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]