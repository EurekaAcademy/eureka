# Generated by Django 4.2.8 on 2024-07-22 19:22

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_course_skills'),
        ('dashboard', '0010_remove_registerprogramselection_program_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', wagtail.fields.StreamField([('content1', wagtail.blocks.CharBlock(required=False)), ('content2', wagtail.blocks.CharBlock(required=False)), ('content3', wagtail.blocks.CharBlock(required=False)), ('content4', wagtail.blocks.CharBlock(required=False)), ('content5', wagtail.blocks.CharBlock(required=False)), ('content6', wagtail.blocks.CharBlock(required=False)), ('content7', wagtail.blocks.CharBlock(required=False)), ('content8', wagtail.blocks.CharBlock(required=False)), ('content9', wagtail.blocks.CharBlock(required=False)), ('content10', wagtail.blocks.CharBlock(required=False)), ('content11', wagtail.blocks.CharBlock(required=False)), ('content12', wagtail.blocks.CharBlock(required=False))], blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pricing_course', to='courses.course')),
                ('course_level', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='schedule_course', to='dashboard.courselevel')),
            ],
        ),
    ]