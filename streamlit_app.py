import streamlit as st
import os
import numpy as np
import pandas as pd
import urllib.request
from PIL import Image
import glob

md_files = sorted([int(x.strip('Day').strip('.md')) for x in glob.glob1('content',"*.md") ])
# Logo and Navigation
col1, col2, col3 = st.columns((1,4,1))
with col2:
    st.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))
st.markdown('# 30 Dias de Streamlit')

days_list = [f'Dia {x}' for x in md_files]

selected_day = st.selectbox('Iniciar o Desafio 👇', days_list)

with st.expander("Sobre o desafio #30DaysOfStreamlit"):
    st.markdown('''
    O **#30DaysOfStreamlit** é um desafio de código desenvolvido para ajudar você a inicar a construção de apps com Streamlit.
        
    No final você conseguirá:
    - Configurar o seu ambiente de desenvolvimento para construir apps com Streamlit 
    - Construir sua primeira aplicação Streamlit 
    - Aprender sobre todas as sensacionais ferramentas (*widgets*) que podem ser usadas no seu app Streamlit
    ''')

# Sidebar
st.sidebar.header('Sobre')
st.sidebar.markdown('[Streamlit](https://streamlit.io) é uma biblioteca Python que permite a criação de aplicações interativasis, baseadas em dados em Python.')

st.sidebar.header('Recursos')
st.sidebar.markdown('''
- [Documentação do Streamlit (em ingl6es)](https://docs.streamlit.io/)
- [Cheat sheet](https://docs.streamlit.io/library/cheatsheet)
- [Livro - Amazon USA](https://www.amazon.com/dp/180056550X) (Getting Started with Streamlit for Data Science)
- [Livro - Amazon Brasil](https://www.amazon.com.br/dp/180056550X/) (Getting Started with Streamlit for Data Science)
- [Livro - Amazon Espanha](https://www.amazon.es/-/pt/dp/180056550X/) (Getting Started with Streamlit for Data Science)

- [Blog (em inglês)](https://blog.streamlit.io/how-to-master-streamlit-for-data-science/) (How to master Streamlit for data science)
''')

st.sidebar.header('Deploy')
st.sidebar.markdown('Você pode rapidamente fazer um deploy usando o [Streamlit Cloud](https://streamlit.io/cloud) em alguns cliques.')

# Display content
for i in days_list:
    if selected_day == i:
        st.markdown(f'# 🗓️ {i}')
        # Workaround to keep files name in English while displaying them in Portuguese
        pt_to_en = i.replace('Dia', 'Day')
        j = pt_to_en.replace(' ', '')
        with open(f'content/{j}.md', 'r') as f:
            st.markdown(f.read())
        if os.path.isfile(f'content/figures/{j}.csv') == True:
            st.markdown('---')
            st.markdown('### Figures')
            df = pd.read_csv(f'content/figures/{j}.csv', engine='python')
            for i in range(len(df)):
                st.image(f'content/images/{df.img[i]}')
                st.info(f'{df.figure[i]}: {df.caption[i]}')
