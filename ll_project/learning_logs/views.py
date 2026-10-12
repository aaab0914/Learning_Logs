from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import EntryForm, TopicForm
from .models import Entry, Topic


def index(request):
    """The home page for Learning Log."""
    return render(request, "learning_logs/index.html")


@login_required
def topics(request):
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by("date_added")
    content = {"topics": topics}

    return render(request, "learning_logs/topics.html", content)


@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = get_object_or_404(Topic, id=topic_id, owner=request.user)
    entries = topic.entries.order_by("-date_added")

    context = {"topic": topic, "entries": entries}
    return render(request, "learning_logs/topic.html", context)


@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != "POST":
        # No data submitted; create a blank form.
        form = TopicForm(request_user=request.user)
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST, request_user=request.user)

        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            try:
                new_topic.full_clean()
                new_topic.save()
                return redirect("learning_logs:topics")
            except ValidationError as e:
                form.add_error(None, e)

    # Display a blank or invalid form.
    context = {"form": form}
    return render(request, "learning_logs/new_topic.html", context)


@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = get_object_or_404(Topic, id=topic_id, owner=request.user)

    if request.method != "POST":
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            try:
                new_entry.full_clean()
                new_entry.save()
                return redirect("learning_logs:topic", topic_id=topic_id)
            except ValidationError as e:
                form.add_error(None, e)

    # Display a blank or invalid form.
    context = {"topic": topic, "form": form}
    return render(request, "learning_logs/new_entry.html", context)


@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = get_object_or_404(Entry, id=entry_id, topic__owner=request.user)
    topic = entry.topic

    if request.method != "POST":
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)

        if form.is_valid():
            entry = form.save(commit=False)
            try:
                entry.full_clean()
                entry.save()
                return redirect("learning_logs:topic", topic_id=topic.id)
            except ValidationError as e:
                form.add(None, e)

    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "learning_logs/edit_entry.html", context)


# def register(request):
#     if request.user.is_authenticated:
#         return redirect("learning_logs:index")


# 1.delete entry
# 2.delete topic
