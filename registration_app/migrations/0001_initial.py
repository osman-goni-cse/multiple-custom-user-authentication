# Generated by Django 3.2 on 2022-09-04 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import registration_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_applicant', models.BooleanField(default=False)),
                ('is_circular_admin', models.BooleanField(default=False)),
                ('is_department_admin', models.BooleanField(default=False)),
                ('is_cs_admin', models.BooleanField(default=False)),
                ('is_super_admin', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('last_login', models.DateField(auto_now=True, verbose_name='last login')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApplicantRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=200)),
                ('confirm_email', models.EmailField(max_length=254)),
                ('confirm_password', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=False)),
                ('facebook_id', models.URLField(blank=True)),
                ('profile_pic', models.ImageField(upload_to='profile_pics', validators=[registration_app.validators.validate_file_size, registration_app.validators.validate_file_extension])),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
