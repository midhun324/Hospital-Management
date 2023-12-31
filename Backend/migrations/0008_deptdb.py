# Generated by Django 3.2.10 on 2023-08-28 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0007_doctordb_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='deptDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='department')),
            ],
        ),
    ]
