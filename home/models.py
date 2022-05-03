"""Home Page for Post Listing and Post Details"""

from dataclasses import Field
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from streams import blocks



class BlogListingPage(Page):
    """Listing all the Blog Posts"""

    max_count = 1
    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        help_text='Overwrites the default title'
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        """Adding custom items to our context"""
        context = super().get_context(request, *args, **kwargs)
        context['posts'] = BlogDetailPage.objects.live().public()
        context['four_posts'] = context['posts'][:4]
        context['fift_post'] = context['posts'][4:5]
        context['next_four_post'] = context['posts'][5:9]

        return context

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page"




class BlogDetailPage(Page):
    """Actual Blog Post"""

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        help_text="Overwrites the default title"
    )
    blog_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
    )

    content = StreamField(
        [
            ("full_richtext_content", blocks.RichtextBlock()),
            ("cards", blocks.CardBlock()),
            ("cta", blocks.CTABlock()),

        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        ImageChooserPanel("blog_image"),
        StreamFieldPanel("content"),
    ]

