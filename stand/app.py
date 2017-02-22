#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

import eventlet
from factory import create_app, create_babel_i18n, create_redis_store
from stand.socketio_events import StandSocketIO

eventlet.monkey_patch(all=True)

# print "#" * 20
# print 'Starting Lemonade Stand'
# print "#" * 20

app = create_app()
babel = create_babel_i18n(app)
stand_socket_io = StandSocketIO(app)
redis_store = create_redis_store(app)


def main(is_main_module):
    logger = logging.getLogger(__name__)
    config = app.config['STAND_CONFIG']
    port = int(config.get('port', 5000))
    logger.debug('Running in %s mode', config.get('environment'))

    if is_main_module:
        if config.get('environment', 'dev') == 'dev':
            # admin.add_view(DataSourceModelView(DataSource, db.session))
            # admin.add_view(StorageModelView(Storage, db.session))
            app.run(debug=True, port=port)
        else:
            eventlet.wsgi.server(eventlet.listen(('', port)), app)

main(__name__ == '__main__')

