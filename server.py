#!/usr/bin/env python3

import pandas as pd
from flask import Flask
from flask import request
from flask import jsonify
import argparse
from flask import send_file
import numpy as np
import cv2
from PIL import Image
import uuid
import matplotlib.pyplot as plt

app = Flask(__name__)
file_path = "data/img.csv"
print('loding file')
img_file = pd.read_csv(file_path)


@app.route('/getFrame')
def getFrame():
    depth_min = int(request.args.get('depth_min'))
    depth_max = int(request.args.get('depth_max'))
    cmap_val = request.args.get('cmap')
    if not cmap_val:
        cmap_val = 'gray'

    if depth_min != depth_max and depth_min > 0 and depth_max > 0:
        # Image will be sent
        df = img_file.iloc[depth_min:depth_max, 1:]
        x = cv2.resize(df.to_numpy(), (150,150))
        img = Image.fromarray(x)
        filename = "/tmp/"+str(uuid.uuid1())+".gif"
        plt.imsave(filename, img, cmap=cmap_val)
        return send_file(filename, mimetype='image/gif')
    else:
        # send black image as error
        df = img_file.iloc[1:20, :]
        x = cv2.resize(df.to_numpy(), (150,150))
        img = Image.fromarray(x)
        plt.imsave("/tmp/error.gif", img, cmap="gray")
        return send_file("/tmp/error.gif", mimetype='image/gif')



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=9090, help='the port to run the server')
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port, debug=True)
