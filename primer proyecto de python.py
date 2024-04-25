#!/usr/bin/env python
# coding: utf-8

# In[52]:


import json
with open ('Data_CO2_Proyecto_1.json') as f:
    data = json.load(f)
    
data


# In[53]:


type (data)


# In[54]:


data.keys()


# In[55]:


data.values()


# In[56]:


data ['ISO 3166-1 alpha-3']


# In[57]:


### Exploracion de 'Country' y de 'ISO 3166-1 alpha-3'


# In[58]:


set(data['Country'])


# In[59]:


set(data['ISO 3166-1 alpha-3'])


# In[60]:


len(set(data['Country']))


# In[61]:


len(set(data['ISO 3166-1 alpha-3']))


# In[62]:


diccionario_paises = zip(data['ISO 3166-1 alpha-3'], data['Country'])


# In[63]:


diccionario_paises


# In[64]:


diccionario_paises = dict(diccionario_paises)


# In[65]:


diccionario_paises


# In[66]:


len(diccionario_paises[0])


# ### Exploramos 'Year'

# ### los anos son consecutivos, parece que tenemos los datos estructurados por paises

# In[67]:


data['Year']


# In[68]:


len(data['Year'])


# In[69]:


len(set(data['Year']))


# In[70]:


max(set(data['Year']))


# In[71]:


min(set(data['Year']))


# In[72]:


2021 - 1750


# ### exploracion de dimensiones de nuestros datos

# In[73]:


len(data['Country'])


# In[74]:


len(data['Year'])


# In[75]:


len(set(data['Country']))


# In[76]:


len(set(data['Year']))


# In[77]:


232*272


# In[78]:


len(data)


# In[79]:


63104 * 11


# ### exploramos total

# In[82]:


data.keys()


# In[80]:


data['Gas']


# In[81]:


data['Year']


# In[83]:


data['Total']


# In[84]:


type(data['Total'])


# In[111]:


dict.fromkeys(data['Country'])


# In[112]:


list(dict.fromkeys(data['Country']))[-3]


# In[114]:


Paises_unicos = list(dict.fromkeys(data['Country']))
Paises_unicos


# In[85]:


data['Total'][0]


# In[86]:


len(data['Total'])


# In[89]:


len(set(data['Year']))


# In[94]:


data['Total'][728]


# In[95]:


data['Coal'][728] + data['Oil'][728] + data['Gas'][728] + data['Cement'][728] + data['Flaring'][728] + data['Other'][728]


# In[97]:


set(data['Country'])


# ### EXPLORAMOS LOS SLICING DE LAS LISTA DE DATOS
# 

# Hemos encontrado el sistema para localizar los datos correspondientes a cada pais 

# In[98]:


data['Country'][63103]


# In[101]:


data['Country'][:272]


# In[100]:


data['Year'][:272]


# In[102]:


data['Cement'][:271]


# In[107]:


data['Country'][62832:63104]


# In[108]:


len(data['Country'][62832:63104])


# In[109]:


data['Year'][62832:63104]


# In[110]:


data['Coal'][62832:63104]


# In[105]:


data['Country'][63103]


# In[117]:


data['Total'][62832:63104]


# In[116]:


max(data['Total'][62832:63104])


# In[118]:


min(data['Total'][62832:63104])


# In[106]:


63103 - 272


# In[123]:


data['Country'][272:(272*3)]


# In[122]:


len(data['Country'][272:(272*2)])


# In[120]:


Paises_unicos


# In[126]:


paises_enumerados = dict(zip(Paises_unicos, range(272)))


# In[127]:


paises_enumerados


# In[128]:


paises_enumerados['Global']


# In[130]:


data['Country'][(272*231) : (272*232)]


# ### Creamos una funcion que nos calcule el slicing

# In[133]:


paises_enumerados['Armenia']


# In[ ]:


data['Country'][(272*231) : (272*232)]


# In[134]:


len(set(data['Year']))


# In[138]:


def slicing(pais):
    indice = paises_enumerados[pais]
    inicio = indice * len(set(data['Year']))
    fin = inicio + len(set(data['Year']))
    return inicio, fin


# In[139]:


slicing('Armenia')


# In[140]:


data['Country'][2448 : 2720]


# In[141]:


inicio, fin = slicing('Armenia')


# In[142]:


data['Country'][inicio : fin]


# In[144]:


inicio, fin = slicing('USA')


# In[143]:


data['Oil'][inicio : fin]


# In[145]:


def slicing(pais):
    try:
        indice = paises_enumerados[pais]
        inicio = indice * len(set(data['Year']))
        fin = inicio + len(set(data['Year']))
        return inicio, fin
    except:
        print('Algo no ha ido bien')


# In[146]:


slicing('Afganistan')


# In[148]:


paises_enumerados.get('Afghanistan', 'Pais no encontrado')


# In[152]:


def slicing(pais):
    try:
        indice = paises_enumerados.get(pais, 'País no encontrado')
        if type(indice) == str:
            print(pais, ': País no encontrado, vuelve a ingresarlo')
            return
        inicio = indice * len(set(data['Year']))
        fin = inicio + len(set(data['Year']))
        return inicio, fin
    except:
        print('Algo no ha ido bien')


# In[153]:


slicing('Afganistan')


# In[ ]:




