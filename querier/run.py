from api.__main__ import build_app

if __name__ == '__main__':
    app = build_app()
    app.run(port=8083)
