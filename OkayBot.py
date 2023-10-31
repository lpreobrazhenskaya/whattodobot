#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install pyTelegramBotAPI')


# In[100]:


import telebot
import random
import webbrowser
from telebot import types


# In[94]:


setty = ['Да', 'Нет', 'Возможно да', '50/50', 'Возможно нет', 'Не думай вообще об этом, лучше отдохни']


# In[108]:


bot = telebot.TeleBot('6928117210:AAG1tpjiNznHyP38qsFM6O1phdswfuNl-jQ')


# In[ ]:


@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, f'Здравствуй, {message.from_user.first_name}! \nЯ помогу тебе ответить на вопрос <b>"Да или нет?"</b> Для этого просто напиши мне свой вопрос или "/what". Если тебе грустно, напиши "/sad"', parse_mode = 'html')  #message for videt' vse opzii
     
@bot.message_handler(commands = ['what'])
def main(message):
    bot.send_message(message.chat.id, f'{random.choice(setty)}!')

# @bot.message_handler(commands = ['sad'])
# def sad(message):
#     webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

@bot.message_handler(commands = ['sad'])
def site(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Не грусти дружочек', url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
    bot.reply_to(message, 'click here', reply_markup = markup)
                     

@bot.message_handler()
def last(message):
     bot.send_message(message.chat.id, f'{random.choice(setty)}!')
        
        
# @bot.message_handler()
# def last(message):
#     bot.send_message(message.chat.id, f'ID: {message.from_user.id}')
        
bot.polling(non_stop=True)   #bot.infinity_polling()


# ![image.png](attachment:image.png)

# In[13]:


#html


# ![image.png](attachment:image.png)

# In[89]:





# In[ ]:




