import streamlit as st

# =============================
# Datos del menú
# =============================
menu = {
    "Bebidas calientes": [
        ("Americano grande", 4000),
        ("Americano pequeño", 2000),
        ("Mocachino", 7000),
        ("Chocolate", 6000),
        ("Capuchino", 6000),
        ("Café con leche", 4000),
        ("Expreso", 3000),
        ("Aromáticas", 2000),
    ],

    "Bebidas frías": [
        ("Malteada", 12000),
        ("Nevados", 12000),
        ("Yogur litro", 12000),
        ("Jugos naturales (Leche)", 7000),
        ("Jugos naturales (Agua)", 6000),
        ("Yogur personal", 5000),
    ],

    "Helados artesanales": [
        ("Helado con brownie", 10000),
        ("Helado 2 bolas cono", 7000),
        ("Helado 1 bola cono", 4000),
        ("Helado 1 bola vaso", 3500),
        ("Helado artesanal", 3000),
    ],

    "Comidas y repostería": [
        ("Brownie de chocolate", 5000),
        ("Pudín de (café, ciruela)", 5000),
        ("Sándwich jamón y queso", 5000),
        ("Pancakes jamón y queso", 5000),
        ("Alfajores con nibs de cacao", 5000),
        ("Almojábana", 3000),
        ("Empanadas (jamón y queso, pollo, carne, hawaianas", 3000),
        ("Maní garrapiñado", 3000),
        ("Caramelos artesanales", 3000),
        ("Mini galletas con nibs de cacao", 3000),
        ("Galletas de (café, ciruela, surtidas)", 2000),
        ("Muffin de (café, ciruela)", 2000),
        ("Dedos de queso", 1500),   
    ],

    "Café y cacao en grano": [
        ("Café de libra", 35000),
        ("Café de media libra", 18000),
        ("Café de 125 gramos", 10000),
        ("Café orgánico libra", 55000),
        ("Café orgánico media libra", 30000),
        ("Chocolate puro 250g", 30000),
        ("Chocolate 70% 250g", 25000),
        ("Chocolate de bola 250g", 20000),
        ("Chocolate mini puro", 7000),
        ("Chocolate mini 70%", 6000),
        ("Chocolate mini bola", 5000),
        ("Nibs de cacao naturales", 8000),
        ("Nibs de cacao caramelizados", 8000),
    ]
}


# =============================
# Interfaz con Streamlit
# =============================
st.set_page_config(page_title="Menú de Cafe & Cacao", page_icon="☕", layout="centered")

st.title("☕ Menú de Cafe & Cacao")

# Mostrar categorías
for categoria, productos in menu.items():
    with st.expander(categoria, expanded=False):
        for producto, precio in productos:
            st.write(f"• **{producto}** — ${precio:,.0f}")

st.success("¡Gracias por visitarnos! 🥰")
