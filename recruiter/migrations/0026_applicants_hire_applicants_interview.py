# Generated by Django 4.2.5 on 2023-10-30 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiter', '0025_alter_jobpost_app_duedate_alter_jobpost_contact_info_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicants',
            name='hire',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='applicants',
            name='interview',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]