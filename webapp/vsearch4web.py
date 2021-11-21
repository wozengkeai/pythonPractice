# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/17 21:40
@Auth ： zengxiaoyan
@File ：vsearch4web.py
"""
from flask import Flask, render_template,request,redirect
from vsearch import search4letters

app = Flask(__name__)

# @app.route('/')
# def hello() -> '302':
#     '''
#     重定向到/entry，避免不想要的错误
#     :return:
#     '''
#     return redirect('/entry')

@app.route('/search4',methods=['POST'])
def do_search() -> str:
    parase = request.form['phrase']
    letters = request.form['letters']
    res = str(search4letters(parase,letters))
    return render_template('results.html',the_title='Here are your results',the_phrase=parase,the_letters=letters,the_results=res)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',the_title='Welcome to search4letters on the web!')


if __name__ == '__main__':
    app.run(debug=True)