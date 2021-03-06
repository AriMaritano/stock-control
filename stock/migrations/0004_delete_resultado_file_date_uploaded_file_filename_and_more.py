# Generated by Django 4.0 on 2021-12-22 16:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_result_alter_file_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Resultado',
        ),
        migrations.AddField(
            model_name='file',
            name='date_uploaded',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='file',
            name='filename',
            field=models.CharField(default='noname', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='result',
            name='file1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file1', to='stock.file'),
        ),
        migrations.AlterField(
            model_name='result',
            name='file2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='file2', to='stock.file'),
        ),
    ]
