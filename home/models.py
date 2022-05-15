"""Home Page for Post Listing and Post Details"""

from dataclasses import Field
from tabnanny import verbose
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from requests import request

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet


from streams import blocks


class BlogAuthorsOrderable(Orderable):
    """This allows the user to select a blog author"""

    page = ParentalKey("home.BlogDetailPage", related_name="blog_authors")
    author = models.ForeignKey(
        "home.BlogAuthor",
        on_delete=models.CASCADE,
    )

    panels = [
        # Use a SnippetChooserPanel because blog.BlogAuthor is registered as a snippet
        SnippetChooserPanel("author"),
    ]


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
        context['posts'] = BlogDetailPage.objects.live().public().order_by('-date')
        context['news_feed'] = context['posts'][:25]

        context['four_posts'] = context['posts'][:4]
        context['fift_post'] = context['posts'][4:5]
        context['next_four_post'] = context['posts'][5:9]

        return context

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page"


@register_snippet
class BlogAuthor(models.Model):
    """Article Authors for the ADNEWS BLOG """

    user = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True, null=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="+",
    )

    panles = [
        MultiFieldPanel(
            [
                FieldPanel("user"),
                FieldPanel("name"),
                ImageChooserPanel("image"),
            ],
            heading="Name and Image",
        ),
        MultiFieldPanel(
            [
                FieldPanel("website"),
            ],
            heading="Links"
        )
    ]
    
    def __str__(self):
        """String representation of this class"""
        return "{} {}".format(self.name, self.user)

    class Meta:
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"
        

class BlogCategory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Blog Article Category"
        verbose_name_plural = "Blog Article Categories"


class BlogDetailPage(Page):
    """Actual Blog Post"""

    date = models.DateTimeField(auto_now_add=timezone.now())
    category = models.ForeignKey(
        BlogCategory,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text="Category of blog article"
    )

    custom_title = models.CharField(
        max_length=100,
        blank=False,
        null=True,
        help_text="Overwrites the default title"
    )

    content_first_paragraph = models.TextField(
        null=True,
        help_text="First paragrap of article"
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
        FieldPanel("category"),
        ImageChooserPanel("blog_image"),
        FieldPanel("content_first_paragraph"),
        MultiFieldPanel(
            [
                InlinePanel("blog_authors", label="Author of Article", min_num=1, max_num=1),
            ]
        ),
        StreamFieldPanel("content"),
    ]

    def __str__(self):
        return "{} {}".format(self.custom_title, self.date)

    class Meta:
        verbose_name = "Article Page"
        verbose_name_plural = "Article Pages"

    # def save(self, *args, **kwargs):
    #     if self.author is None:
    #         request = kwargs.pop('request')
    #         self.author = request.user
    #         print(self.author)

    #     super().save(*args, **kwargs)


