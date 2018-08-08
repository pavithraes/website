# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-08-08 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0063_blogindex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorapproval',
            name='understands_mentor_contract',
            field=models.BooleanField(default=False, help_text='I understand that Outreachy mentors will need to sign a <a href="/generic-mentor-contract-export/">mentor contract</a> after they accept an applicant as an intern', validators=[home.models.mentor_read_contract]),
        ),
    ]
