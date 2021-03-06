# Generated by Django 3.1.1 on 2020-11-10 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0014_house_e_signature'),
        ('rentals', '0003_delete_tenant'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('is_rent_due', models.BooleanField(default=True)),
                ('total_amount_paid', models.IntegerField(default=0)),
                ('due_money', models.IntegerField()),
                ('tenant_id', models.IntegerField()),
                ('last_payment_date', models.DateTimeField()),
                ('house', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='houses.house')),
            ],
        ),
    ]
