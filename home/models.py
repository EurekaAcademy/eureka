from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
# from wagtailcloudinary.fields import CloudinaryField
# from wagtailcloudinary.widgets import AdminCloudinaryChooser
from cloudinary.models import CloudinaryField
from courses.models import Course


class HomePage(Page):
    template = 'home/home_page.html'
    max_count = 1
    why_get_skills = RichTextField(null=True, blank=True)
    ad_note = RichTextField(null=True, blank=True)
    what_you_will_learn = RichTextField(null=True, blank=True)
    image1 = CloudinaryField(null=True, blank=True)
    what_graduates_receive = RichTextField(null=True, blank=True)
    image2 = CloudinaryField(null=True, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('why_get_skills'),
        FieldPanel('ad_note'),
        FieldPanel('what_you_will_learn'),
        FieldPanel('image1'),
        FieldPanel('what_graduates_receive'),
        FieldPanel('image2'),
    ]

class About(Page):
    template = 'home/about.html'
    heading_title = models.CharField(max_length=500, null=True, blank=True)
    banner = CloudinaryField(null=True, blank=True, help_text='upload image banner to display.')
    intro = RichTextField(null=True, blank=True)
    contents = StreamField([
        ('content1', blocks.StructBlock([
            ('title', blocks.CharBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
            ('text', blocks.RichTextBlock(required=False)),
        ])),
        ('content2', blocks.StructBlock([
            ('title', blocks.CharBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
            ('text', blocks.RichTextBlock(required=False)),
        ])),
        ('content3', blocks.StructBlock([
            ('title', blocks.CharBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
            ('text', blocks.RichTextBlock(required=False)),
        ])),
        ('content4', blocks.StructBlock([
            ('title', blocks.CharBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
            ('text', blocks.RichTextBlock(required=False)),
        ])),
        ('content5', blocks.StructBlock([
            ('title', blocks.CharBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
            ('text', blocks.RichTextBlock(required=False)),
        ])),
        ('content6', blocks.StructBlock([
            ('title', blocks.CharBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
            ('text', blocks.RichTextBlock(required=False)),
        ])),
        ('content7', blocks.StructBlock([
            ('title', blocks.CharBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
            ('text', blocks.RichTextBlock(required=False)),
        ])),
        ('content8', blocks.StructBlock([
            ('title', blocks.CharBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
            ('text', blocks.RichTextBlock(required=False)),
        ])),
        ('content9', blocks.StructBlock([
            ('title', blocks.CharBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
            ('text', blocks.RichTextBlock(required=False)),
        ])),
        ('content10', blocks.StructBlock([
            ('title', blocks.CharBlock(required=False)),
            ('image', ImageChooserBlock(required=False)),
            ('text', blocks.RichTextBlock(required=False)),
        ])),
        
        ('more_text', blocks.RichTextBlock(required=False)),
    ], null=True, blank=True, use_json_field=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('heading_title'),
        FieldPanel('banner'),
        FieldPanel('intro'),
        FieldPanel('contents'),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(About, self).get_context(request, *args, **kwargs)
        courses = Course.objects.all()
        context['courses'] = courses
        
        return context

class AboutProgram(Page):
    template = 'home/about-program.html'
    heading_title = models.CharField(max_length=500, null=True, blank=True)
    banner = CloudinaryField(null=True, blank=True, help_text='upload image banner to display.')
    intro = RichTextField(null=True, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('heading_title'),
        FieldPanel('banner'),
        FieldPanel('intro'),
    ]

class MeetLeadership(Page):
    template = 'home/meet-leadership.html'
    heading_title = models.CharField(max_length=500, null=True, blank=True)
    banner = CloudinaryField(null=True, blank=True, help_text='upload image banner to display.')
    contents = RichTextField(null=True, blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('heading_title'),
        FieldPanel('banner'),
        FieldPanel('contents'),
    ]