# Generated by Django 4.0.10 on 2023-03-02 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_books_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='description',
        ),
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(blank=True, default=False, help_text=' this indicates if the active option type is enabled or not ', null=True, verbose_name='Active'),
        ),
        migrations.RemoveField(
            model_name='books',
            name='category',
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ManyToManyField(help_text='Category type refers to the type of the book based on the category', to='books.category', verbose_name='Category Type '),
        ),
    ]
