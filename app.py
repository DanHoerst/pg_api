from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)


def json_accept_header():
    best_match = request.accept_mimetypes.best_match(["application/json", "text/html"])
    json_match = best_match == "application/json"
    return json_match and request.accept_mimetypes[best_match] > request.accept_mimetypes["text/html"]


@app.route('/', methods=["GET", "POST"])
def hello_world():
    app.logger.debug(
        "{timestamp}: {request_method} {request_url} {request_accept_mimetypes}".format(
            timestamp=datetime.utcnow(),
            request_method=request.method,
            request_url=request.url,
            request_accept_mimetypes=request.accept_mimetypes
        )
    )
    if json_accept_header():
        json_response = {"message": "Good morning"}
        return jsonify(json_response)
    return "<p>Hello World!</p>"


if __name__ == '__main__':
    app.run()
