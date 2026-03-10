from flask import Flask, render_template_string

app = Flask(__name__)

# Data for the store
products = [
    {
        "id": 0, 
        "name": "Sapphire R9 280", 
        "price": 29, 
        "img": "https://i.postimg.cc/kXzbYGcL/20260308-200614.jpg",
        "specs": "8GB VRAM, Dual-X Cooling, Great for 1080p esports."
    },
    {
        "id": 1, 
        "name": "16GB DDR3 RAM", 
        "price": 24, 
        "img": "https://i.postimg.cc/zB8WwQjV/7fa0f758-07fc-45b9-8c13-0d6121e6f59b.jpg",
        "specs": "2x8GB Sticks, 1600MHz, HyperX Blue heatspreaders."
    },
    {
        "id": 2, 
        "name": "GA-970A-UD3P", 
        "price": 39, 
        "img": "https://static.gigabyte.com/StaticFile/Image/Global/99861611681f2157143093282f6e9b46/Product/10041/png/1000",
        "specs": "AM3+ Socket, Supports FX-series CPUs, Ultra Durable."
    }
]

stats = {"cash": 0, "goal": 250}

@app.route('/')
def index():
    progress = min(int((stats['cash'] / stats['goal']) * 100), 100)
    items_html = ""
    for p in products:
        items_html += f"""
        <div style="background:#1a1a1a; border:1px solid #333; padding:15px; width:220px; border-radius:10px; margin:10px;">
            <img src="{p['img']}" style="width:100%; height:150px; object-fit:cover; border-radius:5px;">
            <h3 style="font-size:16px; margin:10px 0;">{p['name']}</h3>
            <p style="color:#00ff41; font-weight:bold;">€{p['price']}.00</p>
            
            <a href="/product/{p['id']}" style="text-decoration:none; background:#333; color:white; padding:8px; display:block; border-radius:5px; margin-bottom:5px; font-size:12px;">VIEW DETAILS</a>
            
            <button onclick="toggleContact({p['id']})" style="width:100%; background:#00ff41; color:black; padding:10px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">BUY</button>
            
            <div id="contact-{p['id']}" style="display:none; margin-top:10px; background:#222; border-radius:5px; padding:8px; text-align:left;">
                <a href="https://wa.me/37124502113?text=Hi!%20I%20am%20interested%20in%20the%20{p['name']}" target="_blank" style="color:#00ff41; text-decoration:none; display:block; padding:5px; font-size:13px;">💬 WhatsApp</a>
                <a href="https://discord.gg/SQY8pRtUdh" target="_blank" style="color:#00ff41; text-decoration:none; display:block; padding:5px; font-size:13px;">🎮 Discord</a>
            </div>
        </div>
        """

    return f"""
    <html>
    <head>
        <title>Gustavs' Shop</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script>
            function toggleContact(id) {{
                var el = document.getElementById('contact-' + id);
                el.style.display = el.style.display === 'none' ? 'block' : 'none';
            }}
        </script>
    </head>
    <body style="background:#0a0a0a; color:white; font-family:sans-serif; text-align:center; padding:20px;">
        <h1 style="color:#00ff41;">GUSTAVS' HARDWARE SHOP</h1>
        <div style="background:#222; width:90%; max-width:600px; margin: 20px auto; padding:15px; border-radius:10px;">
            <p>Hustle Progress: €{stats['cash']} / €{stats['goal']}</p>
            <div style="background:#444; width:100%; height:20px; border-radius:100px; overflow:hidden;">
                <div style="background:#00ff41; width:{progress}%; height:100%;"></div>
            </div>
        </div>
        <div style="display:flex; justify-content:center; gap:10px; flex-wrap:wrap;">{items_html}</div>
    </body>
    </html>
    """

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    p = products[product_id]
    return f"""
    <html>
    <body style="background:#0a0a0a; color:white; font-family:sans-serif; text-align:center; padding:40px;">
        <h1 style="color:#00ff41;">{p['name']} - Specs</h1>
        <img src="{p['img']}" style="width:300px; border-radius:10px;">
        <div style="background:#1a1a1a; padding:20px; border-radius:10px; max-width:400px; margin:20px auto; border:1px solid #00ff41;">
            <p style="font-size:18px;">{p['specs']}</p>
            <h2 style="color:#00ff41;">Price: €{p['price']}</h2>
        </div>
        <a href="/" style="color:#00ff41; text-decoration:none; font-weight:bold;">← BACK TO SHOP</a>
    </body>
    </html>
    """

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
<div style="margin-bottom: 20px; padding: 10px; background: #1a1a1a; border-bottom: 1px solid #333; display: flex; justify-content: center; gap: 15px; flex-wrap: wrap;">
    <a href="#" style="color: #00ff41; text-decoration: none; font-size: 14px; font-weight: bold;">CPU</a>
    <a href="#" style="color: #00ff41; text-decoration: none; font-size: 14px; font-weight: bold;">GPU</a>
    <a href="#" style="color: #00ff41; text-decoration: none; font-size: 14px; font-weight: bold;">PSU</a>
    <a href="#" style="color: #00ff41; text-decoration: none; font-size: 14px; font-weight: bold;">MOBO</a>
    <a href="#" style="color: #00ff41; text-decoration: none; font-size: 14px; font-weight: bold;">RAM</a>
    <a href="#" style="color: #00ff41; text-decoration: none; font-size: 14px; font-weight: bold;">CASE</a>
</div>
