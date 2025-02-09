# Generated by Django 5.0.3 on 2024-04-03 04:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0001_initial'),
        ('Guest', '0001_initial'),
        ('MusicBand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_bandbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_venue', models.CharField(max_length=50)),
                ('booking_fordate', models.DateField()),
                ('booking_fortime', models.TimeField()),
                ('booked_date', models.DateField(auto_now_add=True)),
                ('booking_status', models.CharField(default=0, max_length=10)),
                ('booking_amount', models.CharField(default=0, max_length=50)),
                ('payment_status', models.CharField(default=0, max_length=10)),
                ('bandwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MusicBand.tbl_bandworks')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_place')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint_status', models.CharField(default=0, max_length=10)),
                ('complaint_title', models.CharField(max_length=100)),
                ('complaint_content', models.CharField(max_length=300)),
                ('complaint_reply', models.CharField(default='Not replied', max_length=100)),
                ('complaint_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback_content', models.CharField(max_length=300)),
                ('feedback_date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_user')),
            ],
        ),
    ]
