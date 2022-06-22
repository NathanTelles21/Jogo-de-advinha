#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Importa a biblioteca random


# In[ ]:


import random


# In[ ]:


##Criar um variável chamda número para gerar um número aleatório


# In[ ]:


numero = random.randint(1, 100)


# In[ ]:


contador = 0
while contador < 3:
    print("Você tem apenas 5 chances para acertar")
    chute = input("Digite um número (1 a 100): ")
    chute = int(chute)
    diferenca = numero - chute
    if diferenca == 0:
        print("Você acertou!")
        break
    elif diferenca > 0:
        if diferenca <= 10:
            print("Você errou, o valor é maior (está quente)")
        else:
            print("Você errou, o valor é maior (está frio)")
    else:
        if abs(diferenca) <= 10:
            print("Você errou, o valor é menor (está quente)")
        else:
            print("Você errou, o valor é menor (está frio)")
    contador = contador + 1
print("O número é: %s" % numero)

