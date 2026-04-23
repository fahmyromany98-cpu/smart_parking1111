from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

slots = {
    1: "free", 2: "free", 3: "free",
    4: "free", 5: "free", 6: "free"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    available = sum(1 for s in slots.values() if s == "free")
    return jsonify({
        "total": len(slots),
        "available": available,
        "occupied": len(slots) - available,
        "slots": [{"number": n, "status": s} for n, s in slots.items()]
    })

@app.route('/update', methods=['POST'])
def update():
    data = request.json or {}
    slot = data.get('slot')
    status = data.get('status')
    if slot in slots and status in ['free', 'occupied']:
        slots[slot] = status
        return jsonify({"success": True})
    return jsonify({"success": False})

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)