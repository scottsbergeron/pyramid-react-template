from collections import namedtuple


Route = namedtuple('Route', 'path, name')


class Routes:

    SongsView = Route(path='/api/v1/songs', name='songs')
    SongView = Route(path=r'/api/v1/songs/{song_id:\d+}', name='song')
