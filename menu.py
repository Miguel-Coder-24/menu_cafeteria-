import streamlit as st

# =============================
# Datos del menú
# =============================
menu = {
    "Bebidas calientes": [
        ("Americano grande", 4000),
        ("Americano pequeño", 2000),
        ("Expreso", 3000),
        ("Capuchino", 6000),
        ("Mocachino", 7000),
        ("Aromáticas", 2000),
        ("Chocolate", 6000),
        ("Café con leche", 4000),
    ],

    "Bebidas frías": [
        ("Malteada", 12000),
        ("Nevados", 12000),
        ("Jugos naturales (Agua)", 5000),
        ("Jugos naturales (Leche)", 6000),
        ("Yogur personal", 5000),
        ("Yogur litro", 12000),
    ],

    "Helados artesanales": [
        ("Helado artesanal", 3000),
        ("Helado en bola vaso", 3500),
        ("Helado en bola cono", 4000),
        ("Helado en bola 2 cono", 4000),
        ("Helado con brownie", 10000),
    ],

    "Comidas y repostería": [
        ("Almojábana", 3000),
        ("Galleta de café", 2000),
        ("Galletas de ciruela", 2000),
        ("Galletas surtidas", 2000),
        ("Pudín de café", 5000),
        ("Pudín de ciruela", 5000),
        ("Muffin de café", 2000),
        ("Muffin de ciruela", 2000),
        ("Maní garrapiñado", 3000),
        ("Nibs de cacao naturales", 8000),
        ("Nibs de cacao caramelizados", 8000),
        ("Mini galletas con nibs de cacao", 3000),
        ("Alfajores con nibs de cacao", 5000),
        ("Brownies", 5000),
        ("Caramelos artesanales", 3000)
    ],

    "Café y cacao en grano": [
        ("Café de libra", 35000),
        ("Café de media libra", 18000),
        ("Café de 125 gramos", 10000),
        ("Café orgánico libra", 55000),
        ("Café orgánico media libra", 30000),
        ("Chocolate puro 250g", 30000),
        ("Chocolate 70%", 25000),
        ("Chocolate de bola", 20000),
    ]
}


# =============================
# Interfaz con Streamlit
# =============================
st.set_page_config(page_title="Menú de Cafetería", page_icon="☕", layout="centered")

st.title("☕ Menú de Cafetería")
st.markdown("Escanea el QR o navega en el menú para ver nuestros productos:")

# Mostrar categorías
for categoria, productos in menu.items():
    with st.expander(categoria, expanded=False):
        for producto, precio in productos.items():
            st.write(f"• **{producto}** — ${precio:,.0f}")

st.success("¡Gracias por visitarnos! 🥰")
