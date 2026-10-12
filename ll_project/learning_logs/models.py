import re

from better_profanity import profanity
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    RegexValidator,
)
from django.db import models
from django.db.models.functions import Lower

profanity.load_censor_words()


def validate_no_profanity(value):
    """Validator to check for profanity."""
    if profanity.contains_profanity(value):
        raise ValidationError(
            "Content contains inappropriate or offensive language.", code="profanity"
        )


def validate_stripped_length(value):
    # """ Reject content that is only numbers or only symbols. """
    if len(value.strip()) < 5:
        raise ValidationError(
            "Content must be at least 5 characters after trimming.",
            code="min_length",
        )


def validate_meaningful_content(value):
    """Reject content that is only numbers or only symbols."""
    stripped = value.strip()
    if stripped.isdigit():
        raise ValidationError(
            "Content cannot be only numbers.",
            code="Only_numbers",
        )
    if not re.search(r"[a-zA-Z\u4e00-\u9fff]", stripped):
        raise ValidationError(
            "Content must contain at least one letter.",
            code="no_letters",
        )


text_validator = RegexValidator(
    regex=r"^[a-zA-Z0-9\s\.\,\!\?\-\'\"\(\)\:\/\n\r]+$",
    message="Only letters, numbers, spaces, and basic punctuation are allowed.",
)


def validate_no_excessive_whitespace(value):
    if re.search(r"\s{5,}", value):
        raise ValidationError(
            "Content contains excessive whitespace.",
            code="excessive_whitespace",
        )


def validate_no_repeated_chars(value):
    if re.search(r"(.)\1{4,}", value):
        raise ValidationError(
            "Content contains too many repeated characters.",
            code="repeated_chars",
        )


def validate_no_html(value):
    if re.search(r"<[^>]+>", value):
        raise ValidationError(
            "HTML tags are not allowed.",
            code="html_not_allowed",
        )


class Topic(models.Model):
    """A topic the user is learning about."""

    text = models.CharField(
        max_length=200,
        validators=[
            MinLengthValidator(5, message="Topic must be at least 5 characters long."),
            MaxLengthValidator(200, message="Topic must not exceed 200 characters."),
            text_validator,
            validate_no_profanity,
        ],
    )
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-date_added"]
        indexes = [models.Index(fields=["-date_added"])]
        constraints = [
            models.UniqueConstraint(
                Lower("text"),
                "owner",
                name="unique_topic_per_owner_ci",
            )
        ]

    def __str__(self):
        """Return a string representation of the model."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="entries")
    text = models.TextField(
        validators=[
            MinLengthValidator(5, message="Entry must be at least 5 characters long."),
            text_validator,
            validate_no_profanity,
        ]
    )
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a simple string representing the entry."""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text
