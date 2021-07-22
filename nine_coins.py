#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
class Nine_Coins:
    # 初始函數，dec_num儲存十進位數字
    def __init__(self, dec_num):
        self.dec_num = dec_num
        
    # 呼叫toss()時，dec_num變為隨機數字
    def toss(self):
        self.dec_num = random.randint(0, 511)
        return
    
    # 呼叫此class時會列印
    def __repr__(self):        
        text = ''        
        HT_list = []  
        
        # f-string格式，09表示共9位數，空格由0補上，b表示二進位
        HT_list.extend(f'{self.dec_num:09b}')
        
        # 從頭到尾檢查
        for i in HT_list[::1]:
            if i == '0':
                i = 'H'
            if i == '1':
                i = 'T'
            text += i
            
        return f'Nine_Coins: {text}'
    
    # print此class時會列印
    def __str__(self):
        return f'binary: {self.dec_num:09b} and decimal: {self.dec_num}'


# In[2]:


get_ipython().system('jupyter nbconvert --to script nine_coins.ipynb')


# In[ ]:




