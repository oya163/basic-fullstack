# Generated by Django 4.0.6 on 2023-01-27 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thelab_backend', '0003_companyname_updated_at_alter_companyname_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyname',
            options={'managed': True, 'ordering': ['-updated_at']},
        ),
    ]
