#!/usr/bin/env python
# coding: utf-8

# In[3]:


# test_module.py

PI= 3.141592

def number_input():
    output = input("숫자 이력 : ")
    return float(output)

def get_circum(radius):
    return PI * 2 * radius

def get_area(radius):
    return PI * radius * radius

# python test_module.py를 실행할 때만 실행되는 구문
# 함수를 선언한 자기자신만 사용할 수 있다.
if __name__ == "__main__":
    print("test module_name__ 출력 : ", __name__)
    print("test module : ", get_area(10))
    print("test module : ", get_circum(10))
    
if __name__ == "test_module":
    print("main module_name__ 출력 : ", __name__)
    print("main module : ", get_area(10))
    print("main module : ", get_circum(10))


# In[ ]:




