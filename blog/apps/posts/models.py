#coding> utf-8
from django.db import models
from autoslug import AutoSlugField
from taggit.managers import TaggableManager

class Category(models.Model):

	name = models.CharField(u'Nome', max_length=100, unique=True)
	slug = AutoSlugField(populate_from='name')

	def __unicode__(self):
		return self.name

class Post(models.Model):

	STATUS_CHOICES = (
		('published','Publicado'),
		('draft','Rascunho'),
		('pending','Pendente')
	)

	category = models.ForeignKey(Category, verbose_name=u'categoria')

	title = models.CharField(u'Titulo', max_length=200, unique=True)
	slug = AutoSlugField(populate_from='title')
	summary = models.CharField(u'Resumo', max_length=255)
	content = models.TextField(u'Conteudo')
	tags = TaggableManager()
	image = models.ImageField(u'Imagem', upload_to='%y/%m/%d/posts')
	author = models.CharField(u'Autor', max_length=100)
	status = models.CharField(u'Status', choices=STATUS_CHOICES, max_length=10)
	is_highlight = models.BooleanField(u'E destaque', default=False)
	creation_date = models.DateTimeField(u'Data da criacao', auto_now_add=True)
	update_date = models.DateTimeField(u'Data de update', auto_now=True)

	def __unicode__(self):
		return self.title
