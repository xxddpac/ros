# Generated by Django 2.2 on 2020-03-27 08:46

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='L2TP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=60, verbose_name='L2TP用户名')),
                ('password', models.CharField(default='', max_length=60, verbose_name='L2TP密码')),
                ('status', models.CharField(default='', max_length=60, verbose_name='VPN状态')),
            ],
            options={
                'verbose_name': 'VPN信息',
                'verbose_name_plural': 'VPN信息',
                'db_table': 'l2tp',
            },
        ),
        migrations.CreateModel(
            name='NetworkManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(default='', verbose_name='ip地址')),
                ('vpns', models.ManyToManyField(blank=True, to='network.L2TP', verbose_name='下属VPN')),
            ],
            options={
                'verbose_name': '网络设备关联VPN',
                'verbose_name_plural': '网络设备关联VPN',
                'db_table': 'network',
            },
        ),
        migrations.CreateModel(
            name='UserManage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device', models.ManyToManyField(blank=True, to='network.NetworkManage', verbose_name='下属设备')),
                ('user', models.ForeignKey(blank=True, on_delete=False, to=settings.AUTH_USER_MODEL, verbose_name='系统用户')),
            ],
            options={
                'verbose_name': '用户管理设备',
                'verbose_name_plural': '用户管理设备',
                'db_table': 'user_manage',
            },
        ),
    ]
