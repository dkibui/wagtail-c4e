from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from streams import blocks


class FlexPage(Page):
    template = "flex/flex_page.html"

    # @todo - Add stream fields
    content = StreamField([("title_and_text", blocks.TitleAndTextBlock())],
                          use_json_field=True
                          )
    sub_title = models.CharField(max_length=255, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("sub_title"),
        FieldPanel("content"),
    ]

    class Meta:
        verbose_name = "Flex Page"
        verbose_name_plural = "Flex Pages"
