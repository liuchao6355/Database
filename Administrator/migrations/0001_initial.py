# Generated by Django 3.2.9 on 2021-11-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10, verbose_name='姓名')),
                ('sex', models.CharField(default='', max_length=10, verbose_name='性别')),
                ('age', models.IntegerField(default='', verbose_name='年龄')),
                ('Idcard', models.CharField(default='', max_length=18, verbose_name='身份证号')),
                ('mobile', models.CharField(default='', max_length=11, verbose_name='联系方式')),
                ('province', models.CharField(default='内蒙古自治区', max_length=8, verbose_name='省')),
                ('city', models.CharField(default='乌兰察布市', max_length=8, verbose_name='市')),
                ('address', models.CharField(default='', max_length=30, verbose_name='详细地址')),
                ('addTime', models.DateField(auto_now_add=True, verbose_name='创建日期')),
                ('note', models.CharField(default='', max_length=30, verbose_name='备注(不超过30个字)')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
    ]
