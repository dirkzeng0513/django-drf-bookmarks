# Generated by Django 2.0.6 on 2018-07-09 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmark', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='locations.Bookmark')),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='locations.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('bookmark', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='locations.Bookmark')),
            ],
        ),
    ]
