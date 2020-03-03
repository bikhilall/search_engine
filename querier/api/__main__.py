#!/usr/bin/env python3

import connexion
from search_engine_core import db
from api.encoder import JSONEncoder


def build_app():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Sentence Encoder'}, pythonic_params=True)
    return app



if __name__ == '__main__':
    db.DbInterfaceSingleton()
    app = build_app()
    app.run(port=8081)
