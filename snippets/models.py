from django.db import models
from django.db.models import CharField
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from datetime import date

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):
   created = models.DateTimeField(auto_now_add=True)
   title = models.CharField(max_length=100, blank=True, default='')
   code = models.TextField()
   linenos = models.BooleanField(default=False)
   language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
   style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
   owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
   highlighted = models.TextField()

   def save(self, *args, **kwargs):
       lexer = get_lexer_by_name(self.language)
       linenos = 'table' if self.linenos else False
       options = {'title': self.title} if self.title else {}
       formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                 full=True, **options)
       self.highlighted = highlight(self.code, lexer, formatter)
       super(Snippet, self).save(*args, **kwargs)

   class Meta:
       ordering = ['created']


class Book(models.Model):

    title = models.CharField(max_length=100)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    date = models.IntegerField(min(1000), max(9999), default=date.today)
    genre = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publishing = models.CharField(max_length=100)
    image = models.ImageField(upload_to='books/')
    text = models.FileField(upload_to='books/')

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return (f'{self.name} {self.surname}')

