from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mysite', '0003_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='mysite/static/gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='description',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.Project'),
        ),
    ]