from django.db.models import Manager
from django.db.models.query import QuerySet


class MovieQuerySet(QuerySet):

    def unrated(self):
        return self.filter(rating=0)


class MovieManager(Manager):

    def get_query_set(self):
        return MovieQuerySet(self.model)
