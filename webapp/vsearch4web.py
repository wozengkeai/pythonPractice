# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/17 21:40
@Auth ： zengxiaoyan
@File ：vsearch4web.py
"""
from flask import Flask, render_template,request,escape
# from flask import redirect
from vsearch import search4letters

app = Flask(__name__)

# @app.route('/')
# def hello() -> '302':
#     '''
#     重定向到/entry，避免不想要的错误
#     :return:
#     '''
#     return redirect('/entry')

def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log','a') as log:
        print(req.form,req.remote_addr,req.user_agent, res,file=log, sep="|")  #file指定写入的文件，sep指定分隔符

@app.route('/search4',methods=['POST'])
def do_search() -> str:
    parase = request.form['phrase']
    letters = request.form['letters']
    res = str(search4letters(parase,letters))
    log_request(request,res)
    return render_template('results.html',the_title='Here are your results',the_phrase=parase,the_letters=letters,the_results=res)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    '''
    通过render_template设置你想要的html页面
    :return:
    '''
    return render_template('entry.html',the_title='Welcome to search4letters on the web!')

@app.route('/viewlog')
def view_the_log() -> 'html':
    with open('vsearch.log') as log:
        contents = []
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    title = {'formdata','remote_addr','user_agent','results'}
    return render_template('viewlog.html',the_title='view log',the_row_titles=title,the_data=contents)



if __name__ == '__main__':
    '''
    只有直接执行py文件时才会执行以下命令，通过命令行不会执行
    '''
    app.run(debug=True)