from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class HomePage(Page):
    templates = "home/home_page.html"

    banner_title = models.CharField(max_length=255, blank=True, null=False)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title")
    ]
