#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask

def create_app():
    app = Flask(__name__)
    @app.route('/')
    def hello():
        return "Hello Flask init !!"
    
    @app.route('/main')
    def main():
        return "Main init !!"
    
    return app

