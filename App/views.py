from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from .utils import searchBestPlantes
import os

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        img_send = request.files["img_send"]
        img_send_name = secure_filename(img_send.filename)
        if img_send_name.split(".")[1] in app.config['ALLOWED_EXTENSIONS']:
            img_send_name = secure_filename(img_send_name)
            for f in os.listdir(app.config['UPLOAD_FOLDER']):
                os.remove(os.path.join(app.config['UPLOAD_FOLDER'], f))
            img_send.save(os.path.join(app.config['UPLOAD_FOLDER'], img_send_name))
            bestPlantes = searchBestPlantes(app.config["PLANTES_DICT"], os.path.join(app.config['UPLOAD_FOLDER'], img_send_name))
            return render_template('index.html', img_send_name=img_send_name, description=bestPlantes["description"],
                                   best_img_name=bestPlantes["imgName"], latin_name=bestPlantes["latinName"])
    return render_template('index.html')


if __name__ == "__main__":
    app.run()