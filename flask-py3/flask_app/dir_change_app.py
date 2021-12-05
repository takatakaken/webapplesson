import os
from flask import Flask

# flask標準実行
app = Flask(__name__)
# 相対パスで指定
# app = Flask(__name__, static_folder='resources')
# 絶対パスで指定（ディレクトリは/）
# app = Flask(__name__, static_folder='C:/tmp/www')
# 絶対パスで指定（ディレクトリは\\）
# app = Flask(__name__, static_folder='C:\\tmp\\www')

# main
if __name__ == "__main__":
    # Flaskのマッピング情報を表示
    print (app.url_map)
    app.run(host=os.getenv("APP_ADDRESS", 'localhost'), \
    port=os.getenv("APP_PORT", 3000))
