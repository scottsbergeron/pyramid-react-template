from app.data_layer.datastore import Datastore


class SongFacade:

    def __init__(self):
        self._datastore = Datastore()

    def create_song(self, song_name, song_artist, song_genre):
        """
        :param str song_name:
        :param str song_artist:
        :param str song_genre:
        :rtype: dict
        """
        return self._datastore.create_song(song_name, song_artist, song_genre)

    def delete_song(self, song_id):
        """
        :param int song_id:
        """
        self._datastore.delete_song(song_id)

    def get_song(self, song_id):
        """
        :param int song_id:
        :rtype: dict
        """
        return self._datastore.get_song(song_id)

    def list_songs(self):
        """
        :rtype: dict
        """
        return self._datastore.list_songs()

    def replace_song(self, song_id, song_name, song_artist, song_genre):
        """
        :param int song_id:
        :param str song_name:
        :param str song_artist:
        :param str song_genre:
        :rtype: dict
        """
        return self._datastore.replace_song(song_id, song_name, song_artist, song_genre)
