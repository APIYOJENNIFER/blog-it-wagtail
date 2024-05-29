"""Home Page Model"""

from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HomePage(Page):
    """Model defining the structure of home page"""

    image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
            ]
        )
    ]
