# -*- coding: utf-8 -*-
import threading
import time

from flask import Flask, jsonify, render_template, send_file
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import RPi.GPIO as GPIO

from A4988.A4988 import A4988

app = Flask(__name__,
            static_folder='./dist',
            template_folder='./dist')
api = Api(app)
CORS(app, supports_credentials=True)


# get_parse = reqparse.RequestParser()
# get_parse.add_argument('rotation_dir',type=int)
# get_parse.add_argument('stepper_num',type=int)
# get_parse.add_argument('speed',type = int)
# get_parse.add_argument('speed',type = float)

# GPIO 20:STEP; GPIO 21:DIR


class CommonResult:
    @staticmethod
    def result_ok(code=200, message="OK", result=None):
        return jsonify({"code": code, "message": message, "result": result})

    @staticmethod
    def result_fail(code=500, message="Fail", result=None):
        return jsonify({"code": code, "message": message, "result": result})


stepper = A4988(20, 21)
# 继电器电源控制
GPIO.setup(19, GPIO.OUT)
# 避免驱动烧坏  开始关闭19 GPIO
GPIO.setup(19, GPIO.HIGH)

@app.route('/')
def index():
    return render_template('index.html')


class A4988Control(Resource):
    def get(self, rotation_dir, stepper_num, speed):

        # rotation_dir
        # clockwise = 1
        # anticlockwise = 0
        try:
            # print("方向（１开,顺时针）：" + rotation_dir +"步进步数（１Ｘ1.8°）：" + stepper_num+ "步进延迟速度：" + speed)
            stepper.RotationStep(stepper_num, rotation_dir, speed)
            return CommonResult.result_ok()
        except Exception as e:
            print(e)
            return CommonResult.result_fail(result=e)


class PowerSwitch(Resource):


    def get(self, switch):
        if (switch == 1):
            GPIO.setup(19, GPIO.LOW)
        else:
            GPIO.setup(19, GPIO.HIGH)


api.add_resource(PowerSwitch, '/A4988/power/<int:switch>')
api.add_resource(A4988Control, '/A4988/stepper/<int:rotation_dir>/<int:stepper_num>/<float:speed>')

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=88,
        debug=True)
