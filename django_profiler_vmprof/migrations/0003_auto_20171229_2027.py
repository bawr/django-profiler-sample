# Generated by Django 2.0 on 2017-12-29 20:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_profiler_vmprof', '0002_auto_20171018_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestprofile',
            name='request_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]