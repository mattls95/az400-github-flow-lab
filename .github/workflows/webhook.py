from flask import Flask, request

app = Flask(__name__)


@app.post("/webhook")
def github_webhook():
    event = request.headers.get("X-GitHub-Event")
    payload = request.get_json()

    print(f"Received GitHub event: {event}")

    if event == "pull_request":
        action = payload.get("action")
        pr = payload.get("pull_request", {})

        if (
            action == "closed"
            and pr.get("merged") is True
            and pr.get("base", {}).get("ref") == "main"
        ):
            print("PR merged into main!")

    return "", 200


if __name__ == "__main__":
    app.run(port=5000)