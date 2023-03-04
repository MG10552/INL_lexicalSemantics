
# coding: utf-8

# In[1]:


import nltk


# In[2]:


grammar1 = nltk.parse_cfg(""" S -> NP VP VP -> V NP | V NP PP PP -> P NP V -> "saw" | "ate" | "walked" NP -> "John" | "Mary" | "Bob" | Det N | Det N PP Det -> "a" | "an" | "the" | "my" N -> "man" | "dog" | "cat" | "telescope" | "park" P -> "in" | "on" | "by" | "with" """)


# In[3]:


nltk.parse.cfg


# In[4]:


grammar1 = nltk.CFG.fromstring("""
  S -> NP VP
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  """)


# In[7]:


for p in grammar1.productions(): print (p)


# In[6]:


import pprint


# In[8]:


sent1="the dog saw a man in the park".split()
sent2 = ['I', 'ate', 'an', 'apple']
sent3 = "Mary saw Bob".split()
sent4 = "The man saw my cat".split()
sent5 = "Mary saw my cat in the park".split()
sent6 = "Yesterday Mary saw my cat".split()

rd_parser = nltk.RecursiveDescentParser(grammar1)


# In[9]:


for tree in rd_parser.parse(sent1):
     print (tree)


# In[10]:


import os
os.listdir('.')

def prs(parser, sent):
    for tree in parser.parse(sent):
        print (tree)
		
 

rd_parser = nltk.RecursiveDescentParser(grammar1)
rd_parser_tr = nltk.RecursiveDescentParser(grammar1,trace=2)
sr_parser_tr=nltk.ShiftReduceParser(grammar1, trace=2)
sr_parser=nltk.ShiftReduceParser(grammar1)
ch_parser_tr=nltk.ChartParser(grammar1, trace=2)
ch_parser=nltk.ChartParser(grammar1)


# In[12]:


prs(rd_parser, sent3)


# In[13]:


groucho_dep_grammar = nltk.DependencyGrammar.fromstring("""
'shot' -> 'I' | 'elephant' | 'in'
'elephant' -> 'an' | 'in'
'in' -> 'pajamas'
'pajamas' -> 'my'
""")


# In[14]:


pdp = nltk.ProjectiveDependencyParser(groucho_dep_grammar)
sent = 'I shot an elephant in my pajamas'.split()
trees = pdp.parse(sent)
for tree in trees:
    print (tree)


# In[20]:


nltk.data.show_cfg('grammars/book_grammars/feat0.fcfg')

 
from nltk import load_parser 

sent7="all girls disappeared".split()
sent8="the girl disappears".split()

grammar2 = nltk.data.load('grammars/book_grammars/feat0.fcfg')
cp_tr = load_parser('grammars/book_grammars/feat0.fcfg', trace=2)  
cp = load_parser('grammars/book_grammars/feat0.fcfg')  
trees = cp.parse(sent7)


# In[16]:


from nltk.book import *


# In[24]:


zd='kot szedl'

for p in grammar1.productions(): 
    print (p)

s='a dog barks'.split()
sp = load_parser('gr-ang-sem.fcfg',trace=2)  
trees = sp.parse(s)
for tree in trees:
	print (tree)
	
s='Irene walks'.split()
	
s='Angus gives a bone to every dog'.split()


# In[45]:


os.chdir("C:\\Users\\s10552\\Desktop")
gram2 = nltk.data.load("file:feat0.fcfg")
print(gram2)

sent50 = "a young girl disappeared".split()
sent51 = "the very angry boy cried".split()
sent52 = "the happy young girl walks".split()


# In[46]:


sp = load_parser('feat0.fcfg',trace=2)  
trees = sp.parse(sent50)
for tree in trees:
	print (tree)


# In[49]:


sp = load_parser('feat0.fcfg',trace=2)  
trees = sp.parse(sent51)
for tree in trees:
	print (tree)

