# Generated by Django 2.0.6 on 2018-06-15 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DecimalField(decimal_places=5, max_digits=8)),
                ('RER', models.IntegerField()),
                ('Flow', models.DecimalField(decimal_places=5, max_digits=8)),
                ('delta_O2', models.DecimalField(decimal_places=5, max_digits=8)),
                ('delta_CO2', models.DecimalField(decimal_places=5, max_digits=8)),
                ('VES', models.DecimalField(decimal_places=5, max_digits=8)),
                ('raw_O2', models.DecimalField(decimal_places=5, max_digits=8)),
                ('raw_CO2', models.DecimalField(decimal_places=5, max_digits=8)),
                ('Temperature', models.DecimalField(decimal_places=5, max_digits=8)),
                ('Pressure', models.DecimalField(decimal_places=5, max_digits=8)),
                ('RH_percentage', models.DecimalField(decimal_places=5, max_digits=8)),
                ('EE', models.DecimalField(decimal_places=5, max_digits=8)),
                ('RH', models.DecimalField(decimal_places=5, max_digits=8)),
                ('RQ', models.DecimalField(decimal_places=5, max_digits=8)),
                ('VO_2', models.DecimalField(decimal_places=5, max_digits=8)),
                ('VCO_2', models.DecimalField(decimal_places=5, max_digits=8)),
                ('Haldane', models.DecimalField(decimal_places=5, max_digits=8)),
            ],
        ),
    ]