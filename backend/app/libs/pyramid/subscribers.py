def add_cache__cors_headers_response_callback(event):
    def cache__cors_headers(request, response):
        """
        :param pyramid.request.Request request:
        :param pyramid.request.Response response:
        """
        response.cache_control = 'no-cache, no-store, must-revalidate'
        response.pragma = 'no-cache'
        response.headerlist = [
            *response.headerlist,
            ('Access-Control-Allow-Origin', '*'),
            ('Access-Control-Allow-Methods', 'OPTIONS,GET,POST,PUT,PATCH,DELETE'),
            ('Access-Control-Allow-Headers', 'Content-Type, Authorization'),
            ('Access-Control-Allow-Credentials', 'true'),
            ('Access-Control-Max-Age', '86400')
        ]
    event.request.add_response_callback(cache__cors_headers)
