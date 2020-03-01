from contextlib import contextmanager
from MySQLdb.constants import CLIENT
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker
)
from sqlalchemy.pool import QueuePool
import MySQLdb

DEFAULT_CONNECT_TIMEOUT = 10
DEFAULT_POOL_RECYCLE = 540
DEFAULT_POOL_PRE_PING = False
DEFAULT_POOL_SIZE = 10
DEFAULT_MAX_OVERFLOW = 20

pool = None


def create_session():
    """
    :rtype: sqlalchemy.orm.session.Session
    """
    engine = create_engine('mysql+mysqldb://', pool=pool)
    return scoped_session(sessionmaker(bind=engine, expire_on_commit=False))()


@contextmanager
def use_session():
    """
    :rtype: sqlalchemy.orm.session.Session
    """
    session = create_session()
    try:
        yield session
    finally:
        session.close()


def includeme(config):
    global pool

    settings = config.registry.settings
    db_settings = {
        'host': settings['database.host'],
        'port': settings['database.port'],
        'user': settings['database.user'],
        'password': settings['database.password']
    }

    pool = QueuePool(
        _get_db_conn(
            database='main',
            **db_settings
        ),
        recycle=DEFAULT_POOL_RECYCLE,
        pre_ping=DEFAULT_POOL_PRE_PING,
        pool_size=DEFAULT_POOL_SIZE,
        max_overflow=DEFAULT_MAX_OVERFLOW
    )


def _get_db_conn(host, port, database, user, password):
    """
    :param str host:
    :param int port:
    :param str database:
    :param str user:
    :param str password:
    :rtype: function
    """
    def conn():
        return MySQLdb.connect(
            host=host,
            port=int(port),
            database=database,
            user=user,
            password=password,
            binary_prefix=True,
            connect_timeout=DEFAULT_CONNECT_TIMEOUT,
            client_flag=CLIENT.FOUND_ROWS
        )
    return conn
