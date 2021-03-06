# Generated by Django 2.0.5 on 2018-08-08 19:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bounty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=4000, null=True)),
                ('size', models.DecimalField(decimal_places=2, max_digits=11, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('status_code', models.IntegerField(default=-1, null=True)),
            ],
        ),
    ]
