#https://github.com/mohshawky5193/dog-breed-classifier/blob/master/web-app/web-app-classifier.py
#deployed at https://dog-breed-classifier-udacity.herokuapp.com/

import os
from flask import Flask,request,jsonify,render_template
from fastai.vision.all import *
from fastai.vision.widgets import *
from utils import *

app = Flask(__name__, static_url_path='/static')

def predict_board(img):
    h,w = img.shape
    item_list = []
    for y in range(8):
        for x in range(8):
            box = (x*w/8, y*h/8, (x+1)*w/8, (y+1)*h/8) # left, top, right, bottom
            cropped = img.crop(box)
            square = PILImage.create(cropped.to_bytes_format())
            item_list.append(square) 

    learner = load_learner('latest.pkl')
    classes = learner.dls.vocab
    dl = learner.dls.test_dl(item_list)
    _, __, preds = learner.get_preds(dl=dl, with_decoded=True)
    preds = [classes[p] for p in preds]
    labels = ''.join([label_lib[p] for p in preds])
    fen = label2fen(labels)
    
    return fen

@app.route('/')
def render_page():
    return render_template('cat-breed-detector.html')

@app.route('/uploadajax',methods=['POST'])
def upload_file():
    """
    retrieve the image uploaded and make sure it is an image file
    """
    file = request.files['file']
    image_extensions=['jpg', 'jpeg', 'png']
    
    if file.filename.split('.')[-1] not in image_extensions:
        return jsonify('Please upload an appropriate image file')
    
    """
    Perform prediction
    """
    img = Image.open(file)
    fen = predict_board(img)
    
    return jsonify(fen)
    
if __name__ == '__main__':
    app.run(debug=False,port=os.getenv('PORT',5000))


