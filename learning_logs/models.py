from django.db import models


class Topic(models.Model):
    """Um assunto que o usuário está aprendendo."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retorna uma representação em string do modelo no painel de admin."""
        return f"{self.text} - {self.date_added.astimezone().strftime('%d/%m/%Y %H:%M:%S')}"
    
class Entry(models.Model):
    """Algo específico aprendido sobre um assunto."""

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) 
    """ o on_delete=models.CASCADE significa que se o tópico for excluído, todas as entradas relacionadas a ele também serão excluídas. """
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Retorna uma representação em string do modelo no painel de admin."""
        return f"{self.text[:50]}..."