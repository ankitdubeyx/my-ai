from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

MODEL = "phi3"

def query_local(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            }
        )
        return response.json()["response"]
    except Exception as e:
        return f"Error connecting to model: {e}"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    reply = query_local(user_input)
    return jsonify({"response": reply})

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>My AI Assistant</title>
    <style>
        body { background: #0f172a; color: white; font-family: Arial; text-align: center; }
        #chat { width: 80%; height: 400px; margin: auto; overflow-y: auto; border: 1px solid #333; padding: 10px; border-radius: 10px; }
        input { width: 60%; padding: 10px; border-radius: 5px; border: none; }
        button { padding: 10px; background: #22c55e; border: none; border-radius: 5px; }
        button:hover { background: #16a34a; }
    </style>
</head>
<body>
    <h1>Ankit's AI Assistant </h1>
    <div id="chat"></div><br>
    <input id="msg" placeholder="Ask something..." />
    <button onclick="send()">Send</button>

    <script>
        async function send() {
            let input = document.getElementById("msg");
            let text = input.value;
            input.value = "";

            let chat = document.getElementById("chat");
            chat.innerHTML += "<p><b>You:</b> " + text + "</p>";

            let res = await fetch("/chat", {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify({message: text})
            });

            let data = await res.json();
            chat.innerHTML += "<p><b>AI:</b> " + data.response + "</p>";
            chat.scrollTop = chat.scrollHeight;
        }
    </script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    print("🚀 Open: http://127.0.0.1:5000")
    app.run(debug=False, use_reloader=False)