from django.views.generic.base import TemplateView

from rateflix.models import Movie, Genre


class LandingView(TemplateView):

    template_name = 'movies.html'

    def get(self, request, *args, **kwargs):
        genre = request.GET.get('genre')
        if genre:
            kwargs['genre__name'] = genre
        return self.render_to_response(self.get_context_data(**kwargs))

    def get_context_data(self, **kwargs):
        data = {
            'genres': Genre.objects.exclude(movie=None).order_by('name'),
            'movies': self.get_movies(**kwargs),
            'types': ['TV show', 'movie', 'anything']
        }
        return data

    def get_movies(self, **filters):
        movies = (Movie
                .objects
                .filter(**filters)
                .rated()
                .order_by('-rating')[:10])
        return [movie.context_manager.get_context_for_popover()
                    for movie in movies]


class AutocompleteView(TemplateView):

    def get(self, request, *args, **kwargs):
        import ipdb; ipdb.set_trace();
        return super(AutocompleteView, self).get(request, *args, **kwargs)