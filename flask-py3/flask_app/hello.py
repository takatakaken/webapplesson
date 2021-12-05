# import requests
# import json
from types import GetSetDescriptorType
from flask import Flask, request, render_template, jsonify


app = Flask(__name__)
# 日本語化対応
app.config['JSON_AS_ASCII'] = False

# api = "自分が叩きたいAPI" # https://xxx
api = "https://localhost:5000/" # https://xxx

@app.route('/', methods=["GET"])
def hello():
    # URLクエリパラメータの取得
    # search = request.args.get("search")
    html = render_template('index.html')
    return html

@app.route('/', methods=[ "POST"])
def post_hello():
#  res = requests.get(api)
#  data = json.loads(res.text)
    #formデータの受け取り
    test_data = request.form.get('test1')
    html = render_template('index.html', text = test_data)
    return html


@app.route("/name", methods=["GET", "POST"])
def namepage():
    return render_template("name.html", name = 'def_name')


@app.route('/api', methods=["GET", "POST"])
def getpost_hello_api():
    # RESTAPIは全部GetなのでRequestはこんな風に取る
    # q_offset = request.args.get('offset', default=0, type=int)

    #POSTでJSONデータが飛んでくるならこんな感じ？
    # data = request.data  # 取り方が古い模様
    #JdataDict = json.loads(data)
    # json = request.get_json()
    # test_data = json('test1')
    # jsonレスポンス返却
    # jsonifyにdict型オブジェクトを設定するとjsonデータのレスポンスが生成される
    info = {"name":"test1",
            "age":25}
    return jsonify(info)


# エラーのハンドリング errorhandler(xxx)を指定、複数指定可能
# ここでは400,404をハンドリングする
# @app.errorhandler(400)
# @app.errorhandler(404)
# def error_handler(error):
    # error.code: HTTPステータスコード
    # error.description: abortで設定したdict型
#     return jsonify({'error': {
#         'code': error.description['code'],
#         'message': error.description['message']
#     }}), error.code
