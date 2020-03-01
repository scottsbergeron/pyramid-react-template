from .database import use_session
from .db_tables import song
from sqlalchemy.sql import (
    delete,
    insert,
    select,
    text,
    update
)


class Datastore:

    @staticmethod
    def _row_to_dict(row):
        """
        :param sqlalchemy.engine.RowProxy row:
        :rtype: dict
        """
        return {key: value for key, value in row.items()}

    def create_song(self, song_name, song_artist, song_genre):
        """
        :param str song_name:
        :param str song_artist:
        :param str song_genre:
        :rtype: dict
        """
        with use_session() as session:
            params = {
                'name': song_name,
                'artist': song_artist,
                'genre': song_genre
            }
            stmt = insert(song, params)
            session.execute(stmt)
            session.commit()

            # Get the newly created song
            stmt = text('SELECT LAST_INSERT_ID()')
            rs = session.execute(stmt)
            return self._get_song(session, rs.scalar())

    def delete_song(self, song_id):
        """
        :param int song_id:
        """
        with use_session() as session:
            stmt = delete(song).where(song.c.id == song_id)
            session.execute(stmt)
            session.commit()

    def get_song(self, song_id):
        """
        :param int song_id:
        :rtype: dict
        """
        with use_session() as session:
            return self._get_song(session, song_id)

    def list_songs(self):
        """
        :rtype: dict
        """
        with use_session() as session:
            stmt = select([song])
            rs = session.execute(stmt)
            return [
                self._row_to_dict(row)
                for row in rs
            ]

    def replace_song(self, song_id, song_name, song_artist, song_genre):
        """
        :param int song_id:
        :param str song_name:
        :param str song_artist:
        :param str song_genre:
        :rtype: dict
        """
        with use_session() as session:
            params = {
                'name': song_name,
                'artist': song_artist,
                'genre': song_genre
            }
            stmt = update(song).where(song.c.id == song_id).values(**params)
            session.execute(stmt)
            session.commit()
            return self._get_song(session, song_id)

    def _get_song(self, session, song_id):
        """
        :param sqlalchemy.orm.session.Session
        :param int song_id:
        :rtype: dict
        """
        stmt = select([song]).where(song.c.id == song_id)
        rs = session.execute(stmt)
        row = rs.fetchone()
        return self._row_to_dict(row)
