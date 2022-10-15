# Generated by Django 4.1.1 on 2022-10-15 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Door',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('is_car_park', models.BooleanField(default=False)),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.area')),
            ],
        ),
        migrations.CreateModel(
            name='DoorAction',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('action', models.CharField(choices=[('in', 'IN'), ('out', 'OUT')], default='in', max_length=10, null=True)),
                ('door', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.door')),
            ],
        ),
        migrations.CreateModel(
            name='DoorRecord',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('recorded_at', models.DateTimeField()),
                ('recorded_date', models.CharField(max_length=30)),
                ('recorded_time', models.CharField(max_length=30)),
                ('count', models.IntegerField(default=0)),
                ('door_actions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report.dooraction')),
            ],
        ),
    ]
