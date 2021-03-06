from haystack import indexes
from things.models import Thing


class ThingIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=True)

	def get_model(self):
		return Thing
		