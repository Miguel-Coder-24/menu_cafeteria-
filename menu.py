import streamlit as st
import pandas as pd

# =============================
# Datos del menú
# =============================
menu = {
    "Bebidas calientes": [      
        ("Mocachino", 7000),
        ("Chocolate", 6000),
        ("Capuchino", 6000),
        ("Café con leche", 4000),
        ("Americano grande", 4000),
        ("Expreso", 3000),
        ("Americano pequeño", 2000),
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
        ("Brownie con helado", 10000),
        ("Helado 2 bolas cono", 7000),
        ("Helado 1 bola cono", 4000),
        ("Helado 1 bola vaso", 3500),
        ("Helado artesanal", 3000),
    ],

    "Comidas y repostería": [
        ("Brownie de chocolate", 5000),
        ("Pudínes (café, ciruela)", 5000),
        ("Sándwiches jamón y queso", 5000),
        ("Pancakes jamón y queso", 5000),
        ("Alfajores con nibs de cacao", 5000),
        ("Vaso minimuffins", 5000),
        ("Almojábanas de queso", 3000),
        ("Empanadas (jamón y queso, pollo, carne, hawaianas)", 3000),
        ("Muffins de ahuyama y cacao", 3000),
        ("Maní garrapiñado", 3000),
        ("Caramelos artesanales de cacao", 3000),
        ("Mini galletas con nibs de cacao", 3000),
        ("Galletas (café, ciruela, surtidas)", 2000),
        ("Muffins (café, ciruela)", 2000),
        ("Dedos de queso", 1500),
    ],

    "Café y Cacao en grano": [
        ("Café bolsa 500g", 35000),
        ("Café bolsa 250g", 18000),
        ("Café bolsa 125g", 10000),
        ("Café orgánico 500g", 55000),
        ("Café orgánico 250g", 30000),
        ("Chocolate puro 250g", 30000),
        ("Chocolate 70% 250g", 25000),
        ("Chocolate de bola 250g", 20000),
        ("Chocolate mini puro", 7000),
        ("Chocolate mini 70%", 6000),
        ("Chocolate mini bola", 5000),
        ("Nibs de cacao naturales", 8000),
        ("Nibs de cacao caramelizados con panela", 8000),
    ]
}


# =============================
# Interfaz con Streamlit
# =============================
st.set_page_config(page_title="Menú de Cafe & Cacao", page_icon="☕", layout="wide")

st.title("☕ Menú de Cafe & Cacao")

# Mostrar categorías con tabla HTML personalizada
for categoria, productos in menu.items():
    with st.expander(categoria, expanded=False): 
        # Crear tabla HTML
        tabla_html = "<table style='width:100%; border-collapse:collapse;'>"
        tabla_html += "<thead><tr><th style='text-align:left;'>Producto</th><th style='text-align:right;'>Precio</th></tr></thead><tbody>"
        for nombre, precio in productos:
            precio_formateado = f"${precio:,}"
            tabla_html += f"<tr><td style='word-break:break-word;'>{nombre}</td><td style='text-align:right;'>{precio_formateado}</td></tr>"
        tabla_html += "</tbody></table>"
        st.markdown(tabla_html, unsafe_allow_html=True)
        
st.success("¡Gracias por visitarnos! 🥰")
