from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(
        {
            "service": "portfolio-cicd-app",
            "status": "ok",
            "deployment": "kubernetes-ready",
        }
    )


if __name__ == "__main__":
    app.run(port=8080)
