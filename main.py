from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Jacek",
        "email": "bukala.jacek@gmail.com",
        "birth": "13.10.1987"
    }

    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200

if __name__ == "__main__":
       app.run(debug=True)

#1. Run in terminal python main.py
#2. Run in browser http://127.0.0.1:5000/get-user/13?extra=%22hello%22