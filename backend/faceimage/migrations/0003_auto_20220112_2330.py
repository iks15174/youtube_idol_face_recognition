# Generated by Django 3.2.10 on 2022-01-12 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faceimage', '0002_alter_facedetectjob_finished_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='facedetectjob',
            name='image_group',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detect_jobs', to='faceimage.imagegroup'),
        ),
        migrations.AddField(
            model_name='facedetectjob',
            name='link',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
    ]