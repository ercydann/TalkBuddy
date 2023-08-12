# Generated by Django 4.1.7 on 2023-06-24 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mychatapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mychatapp.profile')),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(related_name='my_friends', to='mychatapp.friend'),
        ),
    ]
