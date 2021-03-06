# Generated by Django 3.1.1 on 2020-11-09 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='E_Signature',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tenant',
            name='complaint_type',
            field=models.CharField(blank=True, choices=[('PL', 'Plumbing'), ('EL', 'Electrical'), ('Rv', 'Renovation'), ('Ot', 'Others')], default='Ot', max_length=200),
        ),
    ]
