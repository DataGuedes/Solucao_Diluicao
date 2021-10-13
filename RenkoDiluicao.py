import streamlit as st
from PIL import Image
import os

img = Image.open("logo-renko-2.png")
st.sidebar.image(img, width=240)

st.title('DILUIÇÃO DE PRODUTOS - RENKO')
st.write(f'Aqui você consegue encontrar de forma prática e resumida como funciona a diluição de {os.linesep}produtos Renko'
        f'{os.linesep*2}Temos um menu ao lado esquerdo apresentando alguns modelos de diluição já prontos, mas caso{os.linesep}necessário, você pode personalizar a forma de diluição conforme a milimitragem de seu {os.linesep}recipiente, exemplo: {os.linesep*3}'
        f'Caso você tenha um galão de 5L e um produto de alta diluicao que seria 1:200, no campo{os.linesep}descrito "Recipiente(em ml) você digita 5000 (5 litros em ML)\{os.linesep*2}'
        f'Já dentro do campo "produto" você informa a diluição dele, que no caso é 200{os.linesep*2}'
        f'Formula utilizada e resultado abaixo{os.linesep*2}')
st.latex(r'''
         (recipiente ^l* 1000) / d
         ''')

st.sidebar.title('Menu - Produtos')

diluicao = ['Selecione uma opção', '1:2', '1:5', '1:9', '1:10', '1:12', '1:20', '1:25', '1:30', '1:40', '1:50', '1:60', '1:100', '1:200', '1:250', '1:300']

produto = st.sidebar.selectbox('Diluição (não envolve ceras e produtos p/ lavanderia)', diluicao)
perso_rec = st.sidebar.number_input('Digite quantos ML tem seu recipiente')
perso_dil = st.sidebar.number_input('Digite a forma de diluição do produto')

if produto == '1:2':
    st.info('Em um recipiente de 1L será despejado no mínimo 500ml de produto')
elif produto == '1:5':
    st.info('Em um recipiente de 1L será despejado no mínimo 200ml de produto')
elif produto == '1:9':
    st.info('Em um recipiente de 1L será despejado no mínimo 112ml de produto')
elif produto == '1:10':
    st.info('Em um recipiente de 1L será despejado no mínimo 100ml de produto')
elif produto == '1:12':
    st.info('Em um recipiente de 1L será despejado no mínimo 83ml de produto')
elif produto == '1:20':
    st.info('Em um recipiente de 1L será despejado no mínimo 50ml de produto')
elif produto == '1:25':
    st.info('Em um recipiente de 1L será despejado no mínimo 40ml de produto')
elif produto == '1:30':
    st.info('Em um recipiente de 1L será despejado no mínimo 33ml de produto')
elif produto == '1:40':
    st.info('Em um recipiente de 1L será despejado no mínimo 25ml de produto')
elif produto == '1:50':
    st.info('Em um recipiente de 1L será despejado no mínimo 20ml de produto')
elif produto == '1:60':
    st.info('Em um recipiente de 1L será despejado no mínimo 16ml de produto')
elif produto == '1:100':
    st.info('Em um recipiente de 1L será despejado no mínimo 10ml de produto')
elif produto == '1:200':
    st.info('Em um recipiente de 1L será despejado no mínimo 5ml de produto')
elif produto == '1:250':
    st.info('Em um recipiente de 1L será despejado no mínimo 4ml de produto')
elif produto == '1:300':
    st.info('Em um recipiente de 1L será despejado no mínimo 3ml de produto')

if perso_rec == 0 and perso_dil > 0:
    st.warning('Campo do recipiente vázio')
elif perso_dil == 0 and perso_rec > 0:
    st.warning('Campo da diluição vázio')
elif perso_dil == 0 and perso_rec == 0:
    st.error('Campos persnonlizados vázios')
else:
    resultado = perso_rec / perso_dil
    if resultado <= 1:
        st.success(f'Em um recipiente de {perso_rec :.0f}ml será despejado no mínimo 1ml de produto')
    else:
        st.success(f'Em um recipiente de {perso_rec :.0f}ml será despejado no mínimo {resultado :.0f}ml de produto')

st.write('Accesse o site da Renko [clicando aqui](http://renko.com.br) para maiores informações')