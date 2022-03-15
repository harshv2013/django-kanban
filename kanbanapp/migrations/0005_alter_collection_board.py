# Generated by Django 4.0.2 on 2022-03-03 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanbanapp', '0004_remove_collection_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collections', to='kanbanapp.board'),
        ),
    ]