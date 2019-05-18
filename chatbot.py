#!/usr/bin/env python
# encoding: utf-8
"""
@author: yueshibin
@license: (C) Copyright 2018, CETCBigData qa_sys_gxz.
@contact: yueshibin@cetcbigdata.com
@software: Pycharm
@file: chatbot.py
@time: 2019-5-18 10:28
@desc:
"""
import json
from flask import request
from flask import jsonify
from flask import Flask
from chatbot_graph import ChatBotGraph

app = Flask(__name__)
handler = ChatBotGraph()


@app.route('/bot', methods=['POST'])
def bot():
    _msg = "成功"
    _code = 200
    try:
        user_input = request.form.get('username')
        bot_answer = handler.chat_main(user_input)
    except:
        _msg = "失败"
        _code = 500
        bot_answer = "您好，医药智能助理还在不断学习之中，您的问题暂时还不知道怎么回答，请您再给我点学习时间。祝您身体棒棒！"

    return jsonify({"_code": _code, "_msg": _msg, "data": bot_answer})