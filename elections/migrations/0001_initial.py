# Generated by Django 3.2.7 on 2021-10-19 15:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('candidate_id', models.IntegerField(primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('election_id', models.TextField(max_length=5, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('started', models.BooleanField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('candidates', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='elections.candidate')),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_voted', models.DateTimeField(auto_now=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate', to='elections.candidate')),
                ('election', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='election', to='elections.election')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voter', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
