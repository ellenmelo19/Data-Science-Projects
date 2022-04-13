#!/usr/bin/env python
# coding: utf-8

# # Meu primeiro projeto de Data Science

# ## Fuga de Helicóptero!

# Começamos importando algumas funções de ajuda

# In[10]:


from helper import *


# ## Coleta dos dados

# Agora, vamos coletar os dados da lista 

# In[12]:


url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'

data = data_from_url(url)


# Imprimindo as três primeiras colunas:

# In[15]:


for row in data:
    print(row[:3])


# ## Retirando os 'Detalhes'
# 

# Inicializamos uma variável chamada `index` de valor `0`. O propósito de criar essa variável é para nos ajudar a saber qual coluna estamos modificando.

# In[17]:


index = 0

for row in data:
    data[index] = row[:-1]
    index += 1


# In[19]:


print(data[:3])


# ## Extraindo o ano
# 

# Vamos extrair o ano, recursivamente , da coluna.

#  Assim, `date = fetch_year(row[0])`, é a extração do ano da data em `row[0]` e atribuição à variável `date`.
# Depois, substituímos o valor de `row[0]` pelo ano que acabamos de extrair.

# In[17]:


from helper import *

url = 'https://en.wikipedia.org/wiki/List_of_helicopter_prison_escapes'
data = data_from_url(url)

for row in data:
    date = fetch_year(row[0])
    row[0] = date


# In[18]:


print(data[:3])


# ## Tentativas por ano

# Criar uma lista de listas com dois elementos: ano e tentativas.

# Primeiros e últimos anos:

# In[19]:


min_year = min(data, key=lambda x: x[0])[0]
max_year = max(data, key=lambda x: x[0])[0]


# Vamos criar uma lista dos anos variando do menor ao maior. Assim iremos determinar quantas tentativas de fuga da prisão ocorreram em cada ano.

# In[20]:


years = []
for y in range(min_year, max_year + 1):
    years.append(y)


# Agora criamos uma lista onde cada elemento é `[<year>, 0].`

# In[21]:


attempts_per_year = []
for y in years:
    attempts_per_year.append([y, 0])


# Por fim, acrescentamos à entrada (de índice 1) +1 cada vez que um ano aparece nos dados.

# In[22]:


# Para cada coluna em data
for row in data:
    for ya in attempts_per_year:
        y = ya[0]
        
        #Atribuir o valor do ano em ya para y
        if row[0] == y:
            ya[1] += 1
            
#Imprimir os resultados            
print(attempts_per_year)  


# Em que ano ocorreram mais tentativas de fuga da prisão com um helicóptero?

# In[23]:


get_ipython().run_line_magic('matplotlib', 'inline')
barplot(attempts_per_year)


# R: Os anos em que ocorreram mais tentativas de fuga de helicóptero foram 1986, 2001, 2007 e 2009, com três tentativas cada.

# E se quiséssemos responder à pergunta: 
# Em quais países ocorrem as mais tentativas de fuga de helicóptero?

# # Tentativas por país

# Em nossos dados, cada país pode aparecer várias vezes. Assim vamos contar quantas vezes cada país aparece, respondendo assim à pergunta.

# In[24]:


#Contar o número de ocorrências para cada país
countries_frequency = df["Country"].value_counts()


# In[25]:


print_pretty_table(countries_frequency)


# Concluímos então que o país com mais tentativas de fuga de prisão por helicóptero é a França.

# In[ ]:




