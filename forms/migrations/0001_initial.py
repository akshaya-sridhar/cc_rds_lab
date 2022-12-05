# Generated by Django 4.1.3 on 2022-12-01 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='covid_19',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State_Name', models.CharField(max_length=100)),
                ('Date_of_Record', models.DateField()),
                ('No_of_Samples', models.IntegerField()),
                ('No_of_Deaths', models.IntegerField()),
                ('No_of_Positive', models.IntegerField()),
                ('No_of_Negative', models.IntegerField()),
                ('No_of_Discharge', models.IntegerField()),
            ],
        ),
    ]
