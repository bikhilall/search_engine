from api.__main__ import build_app
from search_engine_core import db

if __name__ == '__main__':
    import os

    os.environ['ENCODER_API_BASE_URL'] = 'http://0.0.0.0:8080'
    db.DbInterfaceSingleton(host='localhost')
    app = build_app()
    app.run(port=8083)
