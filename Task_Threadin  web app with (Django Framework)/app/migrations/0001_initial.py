# Generated by Django 2.2.24 on 2021-10-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('confirmpassword', models.CharField(max_length=40)),
                ('firstname', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=10)),
                ('IDnumber', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=40)),
                ('address', models.CharField(max_length=40)),
                ('copyid', models.ImageField(upload_to='')),
                ('proofofaddress', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'userregistration',
            },
        ),
    ]