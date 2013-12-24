import datetime
from haystack import indexes
from posts.models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    summary = indexes.CharField(model_attr='summary')
    content = indexes.CharField(model_attr='content')
    author = indexes.CharField(model_attr='author')
    category = indexes.CharField(model_attr='category')

    def prepare_category(self, obj):
    	return obj.category.name

    def get_model(self):
        return Post

    #def index_queryset(self, using=None):
    #    """Used when the entire index for model is updated."""
    #    return self.get_model().objects.filter(creation_date__lte=datetime.datetime.now())
