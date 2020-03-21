import connexion

from api.encoder import JSONEncoder


def build_app():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Sentence Encoder'}, pythonic_params=True)
    return app


def get_flask_app():
    return build_app().app


if __name__ == '__main__':
    app = build_app()
    app.run(port=8080)
