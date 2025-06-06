# Generated by Django 5.2 on 2025-04-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('supplier', models.CharField(max_length=100)),
                ('received_date', models.DateField()),
                ('quantity_kg', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quality_check_passed', models.BooleanField(default=False)),
                ('inspection_notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
