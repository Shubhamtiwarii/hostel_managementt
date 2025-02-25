# Generated by Django 5.0.2 on 2024-03-25 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0004_remove_room_book_room_num_remove_room_book_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='room_book',
            name='hostel_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room_book',
            name='room_number',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room_book',
            name='room_type',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room_book',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
