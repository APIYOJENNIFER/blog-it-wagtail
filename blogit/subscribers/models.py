from django.db import models
from wagtail.models import Page
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.contrib.forms.panels import FormSubmissionsPanel

# Create your models here.


class FormField(AbstractFormField):
    page = ParentalKey(
        "SubscribersPage", on_delete=models.CASCADE, related_name="form_fields"
    )


class SubscribersPage(AbstractForm):
    """Define the subscribers model"""

    intro = RichTextField(blank=True)
    email = models.CharField(
        max_length=100, blank=False, null=False, help_text="Email address"
    )
    full_name = models.CharField(
        max_length=100, blank=False, null=False, help_text="First and last name"
    )

    content_panels = AbstractForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel("intro"),
        InlinePanel("form_fields", label="Form fields"),
    ]
