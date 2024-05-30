"""Home Page Model"""

from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

from blog.models import BlogPage


class HomePage(Page):
    """Model defining the structure of home page"""

    image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL
    )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        blogindexpage = (
            BlogPage.objects.all().live().order_by("-first_published_at")[:8]
        )
        context["blogindexpage"] = blogindexpage
        return context

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("image"),
            ]
        )
    ]
