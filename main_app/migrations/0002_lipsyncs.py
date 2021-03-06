# Generated by Django 4.0.5 on 2022-07-06 22:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LipSyncs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=50)),
                ('episode', models.CharField(max_length=50)),
                ('song', models.CharField(max_length=100)),
                ('vs', models.CharField(max_length=100)),
                ('queen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.queen')),
            ],
        ),
    ]
