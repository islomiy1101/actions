# Generated by Django 3.1 on 2020-11-28 12:08

import ckeditor_uploader.fields
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
            name='Contact_Us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('contact_number', models.CharField(blank=True, max_length=250, unique=True)),
                ('email', models.EmailField(max_length=100)),
                ('subject', models.CharField(max_length=250)),
                ('message', models.TextField()),
                ('added_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Biz bilan Aloqa',
            },
        ),
        migrations.CreateModel(
            name='PartQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parttitle', models.CharField(max_length=200)),
                ('partdesc', models.CharField(blank=True, max_length=1500)),
                ('digital', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Test Bo`limlari Nomi',
            },
        ),
        migrations.CreateModel(
            name='Question_Lang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_lang', models.CharField(max_length=250)),
                ('desc', models.CharField(blank=True, max_length=250)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('audio', ckeditor_uploader.fields.RichTextUploadingField()),
            ],
            options={
                'verbose_name_plural': 'Tillar Nomi (Test yechish uchun)',
            },
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provin', models.CharField(blank=True, choices=[('Andijon', 'Andijon'), ('Buxoro', 'Buxoro'), ('Fargʻona', 'Fargʻona'), ('Jizzax', 'Jizzax'), ('Xorazm', 'Xorazm'), ('Namangan', 'Namangan'), ('Navoiy', 'Navoiy'), ('Qashqadaryo', 'Qashqadaryo'), ('Qoraqalpogʻiston', 'Qoraqalpogʻiston'), ('Samarqand', 'Samarqand'), ('Sirdaryo', 'Sirdaryo'), ('Surxondaryo', 'Surxondaryo'), ('Qashqadaryo', 'Qashqadaryo'), ('Toshkent', 'Toshkent')], max_length=200, null=True)),
                ('state', models.CharField(blank=True, max_length=250, null=True)),
                ('contact_number', models.IntegerField()),
                ('contact_number2', models.CharField(max_length=250)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profiles/%Y/%m/%d')),
                ('city', models.CharField(blank=True, max_length=250, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(default='Male', max_length=250, null=True)),
                ('occupation', models.CharField(blank=True, max_length=250, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_on', models.DateTimeField(auto_now=True, null=True)),
                ('dateofbirth', models.DateField()),
                ('sert_id', models.CharField(max_length=10, null=True, unique=True)),
                ('balance', models.IntegerField(default=False)),
                ('training_center', models.CharField(max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Ro`yxatdan O`tganlar',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_questions', models.CharField(max_length=100)),
                ('correct_answers', models.CharField(max_length=100)),
                ('result', models.CharField(max_length=250)),
                ('place_number', models.CharField(blank=True, max_length=250)),
                ('place_number_country', models.CharField(blank=True, max_length=250)),
                ('question_langid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondapp.question_lang')),
                ('register_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondapp.register')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Natijalar',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qname', ckeditor_uploader.fields.RichTextUploadingField()),
                ('qitem1', models.CharField(blank=True, max_length=250)),
                ('qitem2', models.CharField(blank=True, max_length=250)),
                ('qitem3', models.CharField(blank=True, max_length=250)),
                ('qitem4', models.CharField(blank=True, max_length=250)),
                ('answer', models.CharField(blank=True, max_length=250)),
                ('partquestion_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondapp.partquestion')),
                ('question_langid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondapp.question_lang')),
            ],
            options={
                'verbose_name_plural': 'Savollar',
            },
        ),
        migrations.AddField(
            model_name='partquestion',
            name='question_langid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondapp.question_lang'),
        ),
        migrations.CreateModel(
            name='AnswerQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ansa', models.CharField(max_length=300, null=True)),
                ('is_true', models.BooleanField(blank=True)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondapp.question')),
                ('question_langid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='secondapp.question_lang')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Javoblar',
            },
        ),
    ]
