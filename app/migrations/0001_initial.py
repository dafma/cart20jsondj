# Generated by Django 2.0.4 on 2018-04-16 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='books', max_length=40)),
                ('description', models.CharField(max_length=1000)),
                ('featured', models.BooleanField(default=False)),
                ('multimedia', models.ImageField(blank=True, upload_to='img', verbose_name='Product Image')),
                ('name', models.CharField(max_length=100)),
                ('popularity', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='BookOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('order_date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bookorder',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Order'),
        ),
        migrations.AddField(
            model_name='bookorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Book'),
        ),
    ]
