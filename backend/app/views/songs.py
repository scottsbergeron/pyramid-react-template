from ._base import BaseView
from app.facades.song import SongFacade
from app.routes import Routes
from pyramid.view import view_defaults


@view_defaults(route_name=Routes.SongsView.name, renderer='json')
class SongsView(BaseView):

    def __init__(self, request):
        super().__init__(request)
        self._song_facade = SongFacade()

    def get(self):
        """
        List songs
        :rtype: dict
        """
        result = self._song_facade.list_songs()
        return self.json_response(result)

    def post(self):
        """
        Create a song
        :rtype: dict
        """
        body = self._request.json_body
        result = self._song_facade.create_song(
            song_artist=body.get('artist'),
            song_genre=body.get('genre'),
            song_name=body.get('name')
        )
        return self.json_response(result)


@view_defaults(route_name=Routes.SongView.name, renderer='json')
class SongView(BaseView):

    def __init__(self, request):
        super().__init__(request)
        self._song_facade = SongFacade()

    def get(self):
        """
        Get a song
        :rtype: dict
        """
        song_id = self._request.matchdict['song_id']
        result = self._song_facade.get_song(song_id)
        return self.json_response(result)

    def put(self):
        """
        Replace a song
        :rtype: dict
        """
        song_id = self._request.matchdict['song_id']
        body = self._request.json_body
        result = self._song_facade.replace_song(
            song_id=song_id,
            song_artist=body.get('artist'),
            song_genre=body.get('genre'),
            song_name=body.get('name')
        )
        return self.json_response(result)

    def delete(self):
        """
        Delete a song
        :rtype: pyramid.request.Response
        """
        song_id = self._request.matchdict['song_id']
        self._song_facade.delete_song(song_id)
        return self.empty_response()


def includeme(config):
    config.add_route(Routes.SongsView.name, Routes.SongsView.path)
    config.add_view(SongsView, attr='options', request_method='OPTIONS')
    config.add_view(SongsView, attr='get', request_method='GET')
    config.add_view(SongsView, attr='post', request_method='POST')

    config.add_route(Routes.SongView.name, Routes.SongView.path)
    config.add_view(SongView, attr='options', request_method='OPTIONS')
    config.add_view(SongView, attr='get', request_method='GET')
    config.add_view(SongView, attr='put', request_method='PUT')
    config.add_view(SongView, attr='delete', request_method='DELETE')
