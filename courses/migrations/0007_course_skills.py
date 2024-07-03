# Generated by Django 4.2.8 on 2024-07-02 16:04

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_rename_modules_curriculum_beginner_modules_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='skills',
            field=wagtail.fields.StreamField([('introduction', wagtail.blocks.RichTextBlock(default='Add your content here', required=False)), ('skill_column1', wagtail.blocks.RichTextBlock(default='Add your content here', required=False)), ('skill_column2', wagtail.blocks.RichTextBlock(default='Add your content here', required=False))], blank=True, null=True),
        ),
    ]