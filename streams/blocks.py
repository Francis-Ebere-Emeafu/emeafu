"""Stream Fields Content"""

from typing_extensions import Required
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class TitleAndTextBlock(blocks.StructBlock):
    """Title and Text only"""
    title = blocks.CharBlock(required=True, help_text="Add title here")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"


class RichtextBlock(blocks.RichTextBlock):
    """RichText with all the features"""
    class Meta:
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText Content"


class SimpleRichtextBlock(blocks.RichTextBlock):
    """Richtext without all the features"""
    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs, ):
        super().__init__(**kwargs)
        self.features = [
            "bold",
            "italic",
            "link",
        ]
    
    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Simple RichText"

    
class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)."""
    title = blocks.CharBlock(required=True, help_text="Add your title")

    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=50)),
                ("text", blocks.TextBlock(required=True, max_length=500)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If button page is selected, that will be used first")),
            ]
        )
    )

    class Meta:
        template = "streams/card_blocks.html"
        icon = "edit"
        label = "Staff Cards"


class CTABlock(blocks.StructBlock):
    """A simple call to action section"""
    title = blocks.CharBlock(required=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=False, default="Learn More", max_length=40)
    
    class Meta:
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to Action"