# Generated by Django 4.2.5 on 2023-10-18 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0022_alter_applicants_custom_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicants',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='applicants', to='recruiter.jobpost'),
        ),
    ]
