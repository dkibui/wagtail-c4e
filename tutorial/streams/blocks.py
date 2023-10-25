from wagtail import blocks
from wagtail.blocks import StructBlock


class TitleAndTextBlock(StructBlock):
    title = blocks.CharBlock(required=True)
    text = blocks.TextBlock(required=True)

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
