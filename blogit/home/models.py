"""Home Page Model"""

from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HomePage(Page):
    """Model defining the structure of home page"""

    image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL
    )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        blogindexpage = self.get_descendants().live().order_by("-first_published_at")
        context["blogindexpage"] = blogindexpage
        return context

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
            ]
        )
    ]
