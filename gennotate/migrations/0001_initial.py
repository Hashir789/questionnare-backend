# Generated by Django 4.2.11 on 2024-04-17 21:05

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
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('urll', models.URLField()),
                ('type', models.IntegerField()),
                ('generated', models.BooleanField(default=False)),
                ('question1', models.IntegerField(null=True)),
                ('question2', models.IntegerField(null=True)),
                ('question3', models.IntegerField(null=True)),
                ('question4', models.IntegerField(null=True)),
                ('grade', models.BooleanField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]