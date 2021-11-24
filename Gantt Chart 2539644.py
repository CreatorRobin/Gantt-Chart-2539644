#!/usr/bin/env python
# coding: utf-8

# In[56]:


import plotly as py
import plotly.figure_factory as ff


# In[57]:


pyplt = py.offline.plot


# In[58]:


df3 = [dict(Task="Market Research", Start='2021-10-08', Finish='2021-10-15', Complete=100),
      dict(Task="Identify consumer 'pain points'", Start='2021-10-13', Finish='2021-10-17', Complete=100),
      dict(Task="User interface design", Start='2021-10-17', Finish='2021-10-24', Complete=80),
      dict(Task="Sign in & up, modify profile (code)", Start='2021-10-24', Finish='2021-10-31', Complete=90),     
      dict(Task="Chat (code)", Start='2021-11-01', Finish='2021-11-05', Complete=100), 
      dict(Task="Friend & file management (code)", Start='2021-11-08', Finish='2021-11-15', Complete=90),
      dict(Task="Bluetooth (code)", Start='2021-11-22', Finish='2021-11-27', Complete=30),
      dict(Task="Thesis(chpt1 & abstract)", Start='2021-11-05', Finish='2021-11-26', Complete=50),
      dict(Task="Thesis(chpt2 & 3)", Start='2021-11-16', Finish='2021-11-20', Complete=90),
      dict(Task="Deploy, Test & run", Start='2021-11-14', Finish='2021-11-30', Complete=100),
      dict(Task="Improve and modify", Start='2021-11-20', Finish='2021-11-30', Complete=60)]


# In[59]:


fig = ff.create_gantt(df3, index_col='Complete', show_colorbar=True)
pyplt(fig, filename='C:/Users/1/Desktop/PGT IT/Semester3/2.html')


# 1. Market research
# 2. Identify consumer "pain points" and the characteristics of the software
# 3. User interface design
# 4. Chat function (code)
# 5. Friend management and file management functions (code)
# 6. Login, register function, modify personal data function (code)
# 7. Deploy using cloud services
# 7. Test and run on different phones
# 8. Improve and modify the application

# In[ ]:




