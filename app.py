# 첫 번째 Flask Server
from flask import Flask, render_template
from flask_restx import Api, Resource  # Api 구현을 위한 Api 객체 import
# from kisok.mufiKiosk import kiosk
# from web.mufiWeb import mufiweb

app = Flask(__name__)  # Flask 객체 선언, 파라미터로 어플리케이션 패키지의 이름을 넣어줌.
api = Api(app)  # Flask 객체에 Api 객체 등록


# api.add_namespace(kiosk,'/kiosk')

# api.add_namespace(web,'/web')

# api.add_namespace(page,'/page')



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)