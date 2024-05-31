from django.db import models
from django import forms

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalManyToManyField
from django.core.paginator import Paginator


# Create your models here.
class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by("-first_published_at")
        paginator = Paginator(blogpages, 10)
        page_number = request.GET.get("page")
        blogposts = paginator.get_page(page_number)
        context["blogposts"] = blogposts
        return context

    content_panels = Page.content_panels + [FieldPanel("intro")]


class BlogPage(Page):
    image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL
    )
    date = models.DateField("Publish date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    authors = ParentalManyToManyField("blog.Author", blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("date"),
                FieldPanel("authors", widget=forms.CheckboxSelectMultiple),
            ],
            heading="Blog information",
        ),
        FieldPanel("image"),
        FieldPanel("intro"),
        FieldPanel("body"),
    ]


@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255)
    author_image = models.ForeignKey(
        "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("author_image"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Authors"
