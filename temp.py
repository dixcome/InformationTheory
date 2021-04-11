import streamlit as st

def calculate(prompt):
       length = len(prompt)
       prob = {}
       for p in prompt:
           if p in prob:
               prob[p] += 1
           else: 
               prob[p] = 1
   
       for k in prob:
           prob[k] = round(prob[k]/length, 2)
           st.write("'"+ k+"'" +": "+ str(prob[k]))
       #return prob

def file_p(file):
     with open('C:/Users/Kamilla/.spyder-py3/'+file) as f:
        str_text = f.read()
        length = len(str_text)
        prob = {}
        for p in str_text:
           if p in prob:
               prob[p] += 1
           else: 
               prob[p] = 1
   
        for k in prob:
           prob[k] = round(prob[k]/length, 2)
           st.write("'"+ k+"'" +": "+ str(prob[k]))
        
def open_file(file):
     with open('C:/Users/Kamilla/.spyder-py3/'+file) as f:
        str_text = f.read()
        return str_text
st.title('Probabilities in your text \U0001F63C')
st.sidebar.subheader('Calculate probabilities of symbols in your text️')
prompt = st.sidebar.text_input('Type your text:')
if(st.sidebar.button('Show results')):
   st.subheader('Your text is: ')
   st.write("'"+ prompt+ "'")
   st.success('Your result:')
   calculate(prompt)
file = st.sidebar.text_input('Type your file name:')
if(st.sidebar.button('Show')):
   st.subheader('Your text is: ')
   st.write("'"+open_file(file) + "'")
   st.success('Your result:')
   file_p(file)






 
   
  
           
           
           
        
   






        
