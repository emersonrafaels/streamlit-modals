import hydralit_components as hc
import streamlit as st


hc.hydralit_experimental(True)

# HTML
file_html = open("index.html", "r",
                 encoding="utf-8").read()

# CSS
file_css = open("css/styles.css", "r",
                encoding="utf-8").read()

# JS
file_js = open("js/scripts.js", "r",
               encoding="utf-8").read()

# EXIBINDO O CONTEÚDO HTML
st.markdown(file_html, unsafe_allow_html=True)

# INCORPORANDO O CSS
st.write(f'<style>{file_css}</style>',
         unsafe_allow_html=True)

# INCORPORANDO O JS
st.write()
st.write(f'<script>{file_js}</script>',
         unsafe_allow_html=True)

query_param = st.experimental_get_query_params()

if query_param:
    st.write('We captured these values from the experimental modal form using Javascript + HTML + Streamlit + Hydralit Components.')
    st.write(query_param)