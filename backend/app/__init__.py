from pyramid.config import Configurator
from pyramid.events import NewRequest


class RootContext:

    def __init__(self, request):
        """
        :param pyramid.request.Request request:
        """
        pass


def main(global_config, **app_settings):
    with Configurator(settings=app_settings, root_factory=RootContext) as config:

        # Add database
        config.include('app.data_layer.database')

        # Add views
        config.include('app.views.songs')

        # Add subscribers
        config.add_subscriber(
            'app.libs.pyramid.subscribers.add_cache__cors_headers_response_callback', NewRequest
        )

        config.scan()
        return config.make_wsgi_app()
