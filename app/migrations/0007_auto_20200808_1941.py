# Generated by Django 2.2.4 on 2020-08-08 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20200720_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=255, unique=True)),
                ('value', models.IntegerField(db_index=True)),
                ('tenure', models.IntegerField(db_index=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Packages',
            },
        ),
        migrations.CreateModel(
            name='PaidUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, null=True)),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Package')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Paid Users',
            },
        ),
        migrations.AlterModelOptions(
            name='looking_for_attr',
            options={'verbose_name_plural': 'Attributes Filters'},
        ),
        migrations.AlterModelOptions(
            name='looking_for_cities',
            options={'verbose_name_plural': 'Cities Filter'},
        ),
        migrations.AlterModelOptions(
            name='looking_for_countries',
            options={'verbose_name_plural': 'Countries Filters'},
        ),
        migrations.AlterModelOptions(
            name='looking_for_jobs',
            options={'verbose_name_plural': 'Job Filters'},
        ),
        migrations.AlterModelOptions(
            name='looking_for_religions',
            options={'verbose_name_plural': 'Religion Filters'},
        ),
        migrations.AlterModelOptions(
            name='looking_for_states',
            options={'verbose_name_plural': 'State Filters'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'User Profiles'},
        ),
        migrations.AlterModelOptions(
            name='profilepictures',
            options={'verbose_name_plural': 'User Profile Pictures'},
        ),
        migrations.AddField(
            model_name='profile',
            name='block_profile_pics',
            field=models.BooleanField(blank=True, db_index=True, default=False, null=True),
        ),
        migrations.CreateModel(
            name='ReportUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_description', models.TextField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('to_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='report_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Report User Center',
            },
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.IntegerField(blank=True, choices=[(1, 'Credit Card'), (2, 'Debit Card'), (3, 'Online Transfer'), (4, 'Cash'), (5, 'Cheque')], db_index=True, null=True)),
                ('paid_on', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Package')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.PaidUser')),
            ],
            options={
                'verbose_name_plural': 'Payment Details',
            },
        ),
        migrations.CreateModel(
            name='MessageCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('seen_on', models.DateTimeField(blank=True, db_index=True, null=True)),
                ('to_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='to_user', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Message Center',
            },
        ),
    ]
