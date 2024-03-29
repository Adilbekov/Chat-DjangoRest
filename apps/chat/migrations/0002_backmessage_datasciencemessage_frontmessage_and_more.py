# Generated by Django 5.0.1 on 2024-01-30 15:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BackMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Группа: Backend',
                'verbose_name_plural': 'Группа: Backend',
            },
        ),
        migrations.CreateModel(
            name='DataScienceMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Группа: Data Science',
                'verbose_name_plural': 'Группа: Data Science',
            },
        ),
        migrations.CreateModel(
            name='FrontMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Группа: Frontend',
                'verbose_name_plural': 'Группа: Frontend',
            },
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Личные сообшение ', 'verbose_name_plural': 'Личные сообшение '},
        ),
        migrations.RemoveField(
            model_name='message',
            name='timestamp',
        ),
        migrations.AddField(
            model_name='message',
            name='from_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='message',
            name='to_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
