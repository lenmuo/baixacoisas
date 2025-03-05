from flask import Flask, render_template, request, redirect, url_for, flash
import yt_dlp
import os

app = Flask(__name__)
app.secret_key = "algum_segredo"

DOWNLOAD_FOLDER = "downloads"
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

download_history = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video_url = request.form.get("video_url")
        if not video_url:
            flash("Por favor, insira uma URL válida.", "error")
            return redirect(url_for("index"))

        video_quality = request.form.get("video_quality", "best")
        download_mp3 = request.form.get("download_mp3") == "yes"
        download_thumbnail = request.form.get("download_thumbnail") == "yes"

        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'writethumbnail': download_thumbnail,
            'postprocessors': []
        }

        if download_mp3:
            ydl_opts['format'] = 'bestaudio'
            ydl_opts['postprocessors'].append({
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            })
        else:
            ydl_opts['format'] = f"bestvideo[height={video_quality}]+bestaudio/best[height={video_quality}]"

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(video_url, download=True)
                title = info.get('title', 'Desconhecido')
                uploader = info.get('uploader', 'Canal Desconhecido')
                extension = "MP3" if download_mp3 else "MP4"
                resolution = video_quality if not download_mp3 else "Áudio"
                size = f"{round(info.get('filesize', 0) / (1024 * 1024), 2)} MB" if info.get('filesize') else "Desconhecido"
                thumbnail = info.get('thumbnail', 'https://placehold.co/100x100')

                download_history.append({
                    "title": title,
                    "uploader": uploader,
                    "extension": extension,
                    "resolution": resolution,
                    "size": size,
                    "thumbnail": thumbnail
                })

            flash("Download realizado com sucesso!", "success")
        except Exception as e:
            flash(f"Ocorreu um erro: {str(e)}", "error")

        return redirect(url_for("index"))

    return render_template("index.html", downloads=download_history)

if __name__ == "__main__":
    app.run(debug=True)
