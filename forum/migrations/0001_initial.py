# Generated by Django 4.0.5 on 2022-06-13 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('text', models.TextField(verbose_name='正文')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='编辑时间')),
                ('published_date', models.DateTimeField(blank=True, null=True, verbose_name='发布时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
        ),
    ]