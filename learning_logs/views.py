from django.shortcuts import render
from .models import Topic

def index(request):
    """A página inicial do Learning Log."""

    return render(request, 'index.html')

def topics(request):
    """A página de tópicos do Learning Log."""

    topics = Topic.objects.order_by('date_added')

    context = {'topics': topics}

    return render(request, 'topics.html', context)

def topic(request, topic_id):
    """Mostra um único tópico e todas as suas entradas."""

    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')

    context = {'topic': topic,
               'entries': entries
              }

    return render(request, 'topic.html', context)