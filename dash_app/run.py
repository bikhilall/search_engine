import os
from app import app


if __name__ == '__main__':
    os.environ['QUERIER_API_BASE_URL'] = "http://0.0.0.0:8081"
    app.run_server(debug=True, port=8085)