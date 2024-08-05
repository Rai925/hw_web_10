# Generated by Django 5.0.7 on 2024-08-05 05:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("quotes", "0004_remove_author_created_at_author_see_also_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="quote",
            name="created_at",
        ),
        migrations.AlterField(
            model_name="quote",
            name="author",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="quotes",
                to="quotes.author",
            ),
        ),
        migrations.AlterField(
            model_name="quote",
            name="tags",
            field=models.ManyToManyField(related_name="quotes", to="quotes.tag"),
        ),
    ]