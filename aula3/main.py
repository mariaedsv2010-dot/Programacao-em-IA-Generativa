import streamlit as st
st.title('CADASTRO SIMPLES')

nome = st.text_input('Nome:')
idade = st.number_input('Idade:')
email = st.text_input('E-mail:')
altura = st.number_input('Altura')

if st.button('cadastrar'):
   st.success('pessoa cadastrada')
    
    
    
    
#----------------------------------------------------

#tabuada


numero = st.number_input('numero:')
for x in range(0,11):
   calculo = x * numero
   st.write(f'{x} x {numero} = {calculo} ')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    














                   