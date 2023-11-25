from flask import Flask, render_template, url_for, request, send_file, redirect
from pytube import YouTube

app = Flask(__name__)

def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    return youtubeObject.title, youtubeObject.download(filename="YVideo.mp4", max_retries=3) 
    # try:
    #     return youtubeObject.download()
    # except:
    #     print("An error has occurred")
    # print("Download is completed successfully")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/download", methods = ['POST'])
def download():
    
    if request.method == 'POST': 
        try: 
            titlename, videofilename = Download(request.form['url'])
            print(f"Downloading file path: {videofilename}")
            return send_file(str(videofilename), download_name=titlename + '.mp4', as_attachment=True, mimetype="video/mp4")
        except:
            return redirect(url_for('index'))
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=80)