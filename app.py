import os
from flask import Flask

app = Flask(__name__)

# --- 1. YOUR DATA ---
products = [
    {"id": 0, "name": "Sapphire R9 280", "price": 29, "stock": "available", "img": "https://i.postimg.cc/kXzbYGcL/20260308-200614.jpg", "specs": "3GB GDDR5. Dual-X Cooling. Needs 2x 6-pin."},
    {"id": 1, "name": "16GB DDR3 RAM", "price": 24, "stock": "available", "img": "https://i.postimg.cc/zB8WwQjV/7fa0f758-07fc-45b9-8c13-0d6121e6f59b.jpg", "specs": "HyperX Blue. 1600MHz CL10."},
    {"id": 2, "name": "GA-970A-UD3P", "price": 39, "stock": "available", "img": "https://i.postimg.cc/k47M0L6V/image-348234.jpg", "specs": "Gigabyte AM3+. Supports FX-series CPUs. Ultra Durable."},
]

stats = {"cash": 0, "goal": 200} 
MY_NUMBER = "37124502113"

# --- 2. THE VIBE (CSS) ---
STYLE = """
<style>
    body { background:#0a0a0a; color:white; font-family:sans-serif; text-align:center; margin:0; }
    .nav { background:#111; padding:20px; border-bottom:1px solid #333; }
    .nav a { color:#00ff41; text-decoration:none; font-weight:bold; }
    
    .card { 
        display:inline-block; background:#111; border:1px solid #333; 
        margin:10px; padding:15px; width:240px; border-radius:12px; 
        text-decoration:none; color:white; vertical-align:top; position:relative;
        transition: all 0.3s ease;
    }
    .card:hover { 
        border-color:#00ff41; 
        transform: translateY(-8px); 
        box-shadow: 0 10px 20px rgba(0, 255, 65, 0.2);
        background: #161616;
    }
    
    .btn-buy { background:#00ff41; color:black; padding:10px; border:none; border-radius:5px; font-weight:bold; width:100%; cursor:pointer; display:block; text-decoration:none; margin-top:10px; text-align:center; }
    .btn-specs { background:transparent; color:#00ff41; padding:8px; border:1px solid #00ff41; border-radius:5px; font-weight:bold; width:100%; cursor:pointer; display:block; text-decoration:none; margin-top:8px; font-size:12px; text-align:center; }
    
    .social-btn { display:block; padding:12px; margin:10px 0; border-radius:8px; text-decoration:none; color:white; font-weight:bold; transition: 0.2s; text-align:center;}
    .social-btn:hover { transform: scale(1.05); filter: brightness(1.2); }
    .discord { background: #5865F2; } .facebook { background: #1877F2; } .whatsapp { background: #25D366; }
</style>
"""

@app.route('/')
def home():
    pct = min(int((stats['cash'] / stats['goal']) * 100), 100) if stats['goal'] > 0 else 0
    items = ""
    for p in products:
        items += f'''
        <div class="card">
            <a href="/product/{p['id']}" style="text-decoration:none; color:white;">
                <img src="{p['img']}" style="width:100%; height:150px; object-fit:cover; border-radius:8px;">
                <h3 style="margin:12px 0;">{p['name']}</h3>
            </a>
            <p style="color:#00ff41; font-weight:bold; font-size:1.2em; margin:5px 0;">€{p['price']}</p>
            <a href="/product/{p['id']}" class="btn-specs">🔍 VIEW SPECS</a>
            <a href="/buy/{p['id']}" class="btn-buy">🛒 BUY NOW</a>
        </div>'''
    
    return f"<html><head><meta name='viewport' content='width=device-width, initial-scale=1.0'>{STYLE}</head><body>" \
           f"<div class='nav'><a href='/'>🏠 LAB HOME</a></div>" \
           f"<h1 style='margin-top:30px; letter-spacing:1px;'>GUSTAVS' HARDWARE 🧪</h1>" \
           f"<div style='max-width:400px; margin:20px auto; background:#111; padding:20px; border-radius:15px; border:1px solid #333;'>" \
           f"<p style='margin:0 0 10px 0; font-size:12px; color:#888;'>HUSTLE PROGRESS</p>" \
           f"<div style='background:#222; border-radius:10px; overflow:hidden;'><div style='background:linear-gradient(90deg, #00ff41, #008f25); width:{pct}%; height:12px;'></div></div>" \
           f"<p style='margin:10px 0 0; font-weight:bold; color:#00ff41;'>€{stats['cash']} / €{stats['goal']} ({pct}%)</p></div>" \
           f"<div style='display:flex; justify-content:center; flex-wrap:wrap; padding:20px;'>{items}</div>" \
           f"</body></html>"

@app.route('/product/<int:pid>')
def detail(pid):
    p = next((x for x in products if x['id'] == pid), None)
    return f'''<html><head><meta name='viewport' content='width=device-width, initial-scale=1.0'>{STYLE}</head><body>
    <div class="nav"><a href="/">⬅️ BACK</a></div>
    <div style="max-width:450px; margin:40px auto; background:#111; padding:30px; border:1px solid #333; border-radius:15px; text-align:left;">
        <img src="{p['img']}" style="width:100%; border-radius:10px;">
        <h1 style="color:#00ff41;">{p['name']}</h1>
        <p style="color:#ccc; line-height:1.6;">{p['specs']}</p>
        <h2>€{p['price']}.00</h2>
        <a href="/buy/{p['id']}" class="btn-buy" style="font-size:18px; padding:15px;">🛒 GO TO CHECKOUT</a>
    </div></body></html>'''

@app.route('/buy/<int:pid>')
def buy_menu(pid):
    p = next((x for x in products if x['id'] == pid), None)
    wa_link = f"https://wa.me/{MY_NUMBER}?text=Hi+Gustavs!+I+want+to+buy+the+{p['name'].replace(' ', '+')}"
    return f'''<html><head><meta name='viewport' content='width=device-width, initial-scale=1.0'>{STYLE}</head><body>
    <div class="nav"><a href="/">⬅️ CANCEL</a></div>
    <div style="max-width:400px; margin:40px auto; background:#111; padding:30px; border-radius:15px; border:1px solid #333;">
        <h2 style="color:#00ff41;">Contact Gustavs</h2>
        <p>Buying: <b>{p['name']}</b></p>
        <a href="{wa_link}" target="_blank" class="social-btn whatsapp">📱 WHATSAPP</a>
        <a href="https://discord.gg/SQY8pRtUdh" target="_blank" class="social-btn discord">💬 DISCORD</a>
        <a href="https://facebook.com" target="_blank" class="social-btn facebook">👥 FACEBOOK</a>
    </div></body></html>'''

if __name__ == '__main__':
    # Using the same port logic from your old online code
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port)
