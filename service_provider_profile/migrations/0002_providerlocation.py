# Generated by Django 3.2.7 on 2021-09-10 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service_provider_profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProviderLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=50)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service_provider_profile.providerprofile')),
            ],
        ),
    ]
