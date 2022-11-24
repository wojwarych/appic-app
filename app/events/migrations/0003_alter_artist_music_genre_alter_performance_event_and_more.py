# Generated by Django 4.1.3 on 2022-11-24 14:05

import django.contrib.postgres.constraints
import django.contrib.postgres.fields.ranges
from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_btree_gist_extension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='music_genre',
            field=models.CharField(choices=[('rock', 'Rock'), ('pop', 'Pop')], max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='performance',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performances', to='events.event'),
        ),
        migrations.AddConstraint(
            model_name='performance',
            constraint=django.contrib.postgres.constraints.ExclusionConstraint(expressions=((events.models.TsTzRange('start', 'end', django.contrib.postgres.fields.ranges.RangeBoundary()), '&&'), ('event', '=')), name='exclude_overlapping_performances'),
        ),
    ]
