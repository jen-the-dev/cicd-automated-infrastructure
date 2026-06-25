from flask import Flask, jsonify


def get_health_payload():
    return {
        "service": "portfolio-cicd-app",
        "status": "ok",
        "deployment": "kubernetes-ready",
    }


def create_app():
    flask_app = Flask(__name__)

    @flask_app.get("/health")
    def health():
        return jsonify(get_health_payload())

    return flask_app


app = create_app()


if __name__ == "__main__":
    app.run(port=8080)
