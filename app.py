from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Flask API is running on Render!"})

@app.route('/command', methods=['POST'])
def process_command():
    data = request.json
    command = data.get("command")
    
    if command == "open whatsapp":
        return jsonify({"action": "Opening WhatsApp"})
    elif command == "turn off wifi":
        return jsonify({"action": "Turning off WiFi"})
    elif command == "turn on wifi":
        return jsonify({"action": "Turning on WiFi"})
    else:
        return jsonify({"error": "Command not recognized"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
