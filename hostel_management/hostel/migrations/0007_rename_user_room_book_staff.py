# Generated by Django 5.0.2 on 2024-03-26 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0006_room_book_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room_book',
            old_name='user',
            new_name='staff',
        ),
    ]
