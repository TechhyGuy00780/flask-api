from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/execute", methods=["POST"])
def execute_command():
    data = request.json
    command = data.get("command", "")

    if not command:
        return jsonify({"error": "No command provided"}), 400

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        return jsonify({
            "output": result.stdout or "Executed successfully",
            "error": result.stderr if result.stderr else None
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
