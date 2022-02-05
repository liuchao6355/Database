# Generated by Django 3.2.9 on 2021-12-09 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0012_auto_20211207_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productinfo',
            name='pic_height',
        ),
        migrations.RemoveField(
            model_name='productinfo',
            name='pic_width',
        ),
        migrations.RemoveField(
            model_name='sell',
            name='tradingitems',
        ),
        migrations.AddField(
            model_name='sell',
            name='note',
            field=models.CharField(default='', max_length=50, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='sell',
            name='tradingamount',
            field=models.IntegerField(default='0', verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='productinfo',
            name='picture',
            field=models.ImageField(default='', upload_to='picture_show', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='arrearamount',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=10, verbose_name='拖欠金额'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='payamount',
            field=models.IntegerField(default='0', verbose_name='支付金额'),
        ),
        migrations.AlterField(
            model_name='sell',
            name='paymethods',
            field=models.CharField(default='0', max_length=10, verbose_name='支付方式'),
        ),
    ]
