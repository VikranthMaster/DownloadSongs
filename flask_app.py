from flask import Flask, render_template, request, redirect, url_for
from music import DownloadSongs

app = Flask("__name__")
formData = {}

@app.route("/", methods = ["POST","GET"])
def home():
    if request.method == 'POST':
        song_name = request.form['song_name']
        formData['song_name'] = song_name
        with open('text.txt',"w") as f:
            f.write(formData['song_name'])
            f.close()
        return redirect(url_for('home'))
    else:
        return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
    DownloadSongs("text.txt","Songs")
