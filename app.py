import streamlit as st

# Datos de los círculos
items = [
    {'nombre': 'Balin#3', 'diámetro': 6, 'precio': 27000},
    {'nombre': 'Balin#4', 'diámetro': 6, 'precio': 43000},
    {'nombre': 'Balin#5', 'diámetro': 6, 'precio': 58000},
    {'nombre': 'Balin#6', 'diámetro': 6, 'precio': 73000},
    {'nombre': 'Balin#7', 'diámetro': 6, 'precio': 98000},
    {'nombre': 'Balin#8', 'diámetro': 6, 'precio': 120000},
    {'nombre': 'Balin de goma', 'diámetro': 6, 'precio': 400}
]

st.set_page_config(page_title="Oro de León", layout="wide")
col1, col2 = st.columns([1, 5]) 

with col1:
    st.image("logo.png", width=150)  

with col2:
    st.title("Cotiza tu pulsera")

st.markdown("<p style='font-size:16px; color: gray;'>Bucaramanga</p>", unsafe_allow_html=True)



st.image("balines.png", width=300) 

cantidades = {}
for item in items:
    # Mostrar el círculo
    st.markdown(
        f"""<div style='display:flex;align-items:center;'>
            <div style='width:{item['diámetro']}px;height:{item['diámetro']}px;
                        background:#3498db;border-radius:50%;margin-right:10px;'></div>
            <span style='font-size:16px;'>{item['nombre']} - ${item['precio']}</span>
        </div>""", unsafe_allow_html=True
    )
    # Input numérico
    cantidad = st.number_input(f"Cantidad de {item['nombre']}", min_value=0, max_value=100, step=1, key=item['nombre'])
    cantidades[item['nombre']] = (cantidad, item['precio'])


if st.button("Calcular total"):
    total = sum(cant * precio for cant, precio in cantidades.values())
    st.success(f"Total a pagar: ${total + 5000}")
