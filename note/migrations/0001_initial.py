# Generated by Django 2.1.7 on 2019-02-19 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='售后')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auth.Group', verbose_name='部门')),
            ],
            options={
                'verbose_name': '售后单位',
                'verbose_name_plural': '售后单位',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('gz', models.CharField(max_length=30, verbose_name='故障')),
                ('jg', models.FloatField(verbose_name='价格')),
                ('sl', models.IntegerField(verbose_name='数量')),
                ('dd', models.CharField(max_length=30, verbose_name='地点')),
                ('bz', models.BooleanField(verbose_name='报账')),
                ('fs', models.CharField(max_length=30, verbose_name='方式')),
                ('zt', models.CharField(default='未通知售后', max_length=15)),
                ('tzsj', models.DateField(blank=True, null=True, verbose_name='通知时间')),
                ('dxsj', models.DateField(blank=True, null=True, verbose_name='到校时间')),
                ('fxsj', models.DateField(blank=True, null=True, verbose_name='返校时间')),
                ('xysc', models.DurationField(blank=True, null=True, verbose_name='响应时长')),
                ('xfsc', models.DurationField(blank=True, null=True, verbose_name='修复时长')),
                ('hj', models.FloatField(blank=True, null=True, verbose_name='合计')),
                ('sn', models.CharField(blank=True, default='无', max_length=30, null=True, verbose_name='序列号')),
                ('shry', models.CharField(blank=True, max_length=30, null=True, verbose_name='售后人员')),
                ('shdh', models.CharField(blank=True, max_length=30, null=True, verbose_name='电话')),
            ],
            options={
                'verbose_name': '维修记录',
                'verbose_name_plural': '维修记录',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='Report_time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='名称')),
                ('bz', models.CharField(default='无', max_length=30, verbose_name='备注')),
                ('bzsj', models.DateField(verbose_name='报账时间')),
                ('used', models.BooleanField(default=False, verbose_name='是否已使用')),
                ('sh', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='note.Customer', verbose_name='售后')),
            ],
            options={
                'verbose_name': '报账时间',
                'verbose_name_plural': '报账时间',
                'ordering': ['-bzsj'],
            },
        ),
        migrations.CreateModel(
            name='Unit_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='型号')),
            ],
            options={
                'verbose_name': '设备型号',
                'verbose_name_plural': '设备型号',
            },
        ),
        migrations.CreateModel(
            name='Unit_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='类型')),
                ('sh', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='note.Customer', verbose_name='售后单位')),
            ],
            options={
                'verbose_name': '设备类型',
                'verbose_name_plural': '设备类型',
            },
        ),
        migrations.AddField(
            model_name='unit_model',
            name='lx',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='note.Unit_type', verbose_name='类型'),
        ),
        migrations.AddField(
            model_name='note',
            name='bzsj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='note.Report_time', verbose_name='报账时间'),
        ),
        migrations.AddField(
            model_name='note',
            name='lb',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='note.Unit_type', verbose_name='类型'),
        ),
        migrations.AddField(
            model_name='note',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='note',
            name='sh',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='note.Customer', verbose_name='售后'),
        ),
        migrations.AddField(
            model_name='note',
            name='xh',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='note.Unit_model', verbose_name='型号'),
        ),
    ]
