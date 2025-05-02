from flask import Flask, g, jsonify, request

app = Flask(__name__)

@app.before_request
def load_user():
    # Simulate loading user data from a session or database
    g.user = {"id": 1, "username": "alice"} if request.headers.get("Authorization") else None
    print(g.user)

@app.route("/profile")
def profile():
    if g.user:
        print(g.user)
        return jsonify({"user": g.user})
    else:
        return jsonify({"error": "Unauthorized"}), 401

if __name__ == "__main__":
    app.run(debug=True)
