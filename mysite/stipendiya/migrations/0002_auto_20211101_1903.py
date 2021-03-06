# Generated by Django 3.2.8 on 2021-11-01 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stipendiya', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingliz_tili',
            new_name='Fanlar',
        ),
        migrations.RemoveField(
            model_name='informatika',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='ozbekiston_tarixi',
            name='rating',
        ),
        migrations.AlterField(
            model_name='talaba',
            name='informatika',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='informatika', to='stipendiya.informatika'),
        ),
        migrations.AlterField(
            model_name='talaba',
            name='ingliz_tili',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ingliz_tili', to='stipendiya.ingliz_tili'),
        ),
        migrations.AlterField(
            model_name='talaba',
            name='ozbekiston_tarixi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ozbekiston_tarixi', to='stipendiya.ozbekiston_tarixi'),
        ),
        migrations.AlterModelTable(
            name='fanlar',
            table='fanlar',
        ),
        migrations.DeleteModel(
            name='Informatika',
        ),
        migrations.DeleteModel(
            name='Ozbekiston_tarixi',
        ),
    ]
