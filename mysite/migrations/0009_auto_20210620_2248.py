# Generated by Django 3.2.3 on 2021-06-20 14:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_battery_cs_drug_ea_glass_metal_oil_other_plastic_textile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='metal',
            new_name='M',
        ),
        migrations.DeleteModel(
            name='battery',
        ),
        migrations.DeleteModel(
            name='CS',
        ),
        migrations.DeleteModel(
            name='drug',
        ),
        migrations.DeleteModel(
            name='EA',
        ),
        migrations.DeleteModel(
            name='glass',
        ),
        migrations.DeleteModel(
            name='oil',
        ),
        migrations.DeleteModel(
            name='other',
        ),
        migrations.DeleteModel(
            name='plastic',
        ),
        migrations.DeleteModel(
            name='textile',
        ),
    ]
