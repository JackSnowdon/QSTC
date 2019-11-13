# Generated by Django 2.2.7 on 2019-11-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_roundtube'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vtip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.IntegerField()),
                ('liner', models.CharField(default='Vtip', max_length=32)),
                ('ton', models.CharField(choices=[('Neeedles', 'Needles'), ('Tubes', 'Tubes')], default='Tubes', max_length=20)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]