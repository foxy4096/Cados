# Generated by Django 4.0.3 on 2022-10-15 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advocate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Full Name')),
                ('profile_pic', models.ImageField(upload_to='images/advocate', verbose_name='Avatar')),
                ('short_bio', models.CharField(max_length=100, verbose_name='Short Biography')),
                ('long_bio', models.TextField(blank=True, null=True, verbose_name='Long Biography')),
                ('advocate_years_exp', models.PositiveIntegerField(verbose_name='Advocate Year Experience')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='images/company')),
                ('summary', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube', models.URLField()),
                ('github', models.URLField()),
                ('twitter', models.URLField()),
                ('advocate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='advocate', to='api.advocate')),
            ],
        ),
        migrations.AddField(
            model_name='advocate',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company', to='api.company'),
        ),
    ]
