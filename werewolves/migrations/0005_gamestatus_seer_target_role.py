# Generated by Django 3.1.3 on 2020-12-02 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('werewolves', '0004_auto_20201202_0418'),
    ]

    operations = [
        migrations.AddField(
            model_name='gamestatus',
            name='seer_target_role',
            field=models.CharField(default='NONE', max_length=30, null=True),
        ),
    ]
