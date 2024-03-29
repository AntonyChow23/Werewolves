# Generated by Django 3.1.3 on 2020-12-05 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werewolves', '0009_gamestatus_trigger_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamestatus',
            name='current_speaker_name',
        ),
        migrations.RemoveField(
            model_name='gamestatus',
            name='guard_target_name',
        ),
        migrations.RemoveField(
            model_name='gamestatus',
            name='seer_target_name',
        ),
        migrations.RemoveField(
            model_name='gamestatus',
            name='vote_target_name',
        ),
        migrations.RemoveField(
            model_name='gamestatus',
            name='wolves_target_name',
        ),
        migrations.AddField(
            model_name='gamestatus',
            name='is_kill',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
