# Generated by Django 3.2.6 on 2021-10-24 10:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainsite', '0002_delete_myuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='body',
            new_name='pub_body',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='pub_title',
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='MemberPost',
        ),
    ]