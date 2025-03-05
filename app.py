from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Flask API is running on Render!"})

@app.route('/command', methods=['POST'])
def process_command():
    data = request.json  # Ensure request is JSON
    if not data or "command" not in data:
        return jsonify({"error": "Missing command in request"}), 400

    command = data["command"]
    
    if command == "open whatsapp":
        return jsonify({"action": "Opening WhatsApp"})
    elif command == "turn off wifi":
        return jsonify({"action": "Turning off WiFi"})
    elif command == "turn on wifi":
        return jsonify({"action": "Turning on WiFi"})
    else:
        return jsonify({"error": "Command not recognized"}), 400

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))  # Render uses PORT env variable
    app.run(host="0.0.0.0", port=port)
