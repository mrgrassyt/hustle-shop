from flask import Flask, redirect, url_for

app = Flask(__name__)

# Data for the store
products = [
    {"id": 0, "name": "Sapphire R9 280", "price": 29, "img": "https://www.techpowerup.com/gpu-specs/pics/sapphire-r9-280-dual-x-oc.g2005.jpg"},
    {"id": 1, "name": "16GB DDR3 RAM", "price": 24, "img": "https://m.media-amazon.com/images/I/61Nl5B67P8L._AC_UF894,1000_QL80_.jpg"},
    {"id": 2, "name": "GA-970A-UD3P", "price": 39, "img": "https://static.gigabyte.com/StaticFile/Image/Global/99861611681f2157143093282f6e9b46/Product/10041/png/1000"}
]

# Set your current cash here manually whenever you sell something!
stats = {"cash": 0, "goal": 250}

@app.route('/')
def index():
    progress = min(int((stats['cash'] / stats['goal']) * 100), 100)
    
    items_html = ""
    for p in products:
        items_html += f"""
        <div style="background:#1a1a1a; border:1px solid #333; padding:15px; width:200px; border-radius:10px;">
            <img src="{p['img']}" style="width:100%; height:120px; object-fit:contain;">
            <h3 style="font-size:16px;">{p['name']}</h3>
            <p style="color:#00ff41; font-weight:bold;">€{p['price']}.00</p>
            <a href="https://wa.me/37124502113?text=Hi!%20I%20am%20interested%20in%20the%20{p['name']}" 
               target="_blank" 
               style="background:#00ff41; color:black; padding:10px; text-decoration:none; display:block; border-radius:5px; font-weight:bold;">
               BUY
            </a>
        </div>
        """

    return f"""
    <html>
    <head><title>Gustavs' Hardware Shop</title></head>
    <body style="background:#0a0a0a; color:white; font-family:sans-serif; text-align:center; padding:20px;">
        <h1 style="color:#00ff41;">GUSTAVS' HARDWARE SHOP</h1>
        <div style="background:#222; width:80%; margin: 20px auto; padding:15px; border-radius:10px;">
            <p>Hustle Progress: €{stats['cash']} / €{stats['goal']}</p>
            <div style="background:#444; width:100%; height:20px; border-radius:10px; overflow:hidden;">
                <div style="background:#00ff41; width:{progress}%; height:100%;"></div>
            </div>
        </div>
        <div style="display:flex; justify-content:center; gap:20px; flex-wrap:wrap;">{items_html}</div>
    </body>
    </html>
    """

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
