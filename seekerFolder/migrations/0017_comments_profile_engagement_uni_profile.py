# Generated by Django 4.2.5 on 2023-10-09 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seekerFolder', '0016_alter_allprofile_bio_alter_allprofile_comp_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='profile',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='seekerFolder.allprofile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='engagement',
            name='uni_profile',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='seekerFolder.allprofile'),
            preserve_default=False,
        ),
    ]
