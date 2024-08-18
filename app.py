# # from flask import Flask, render_template, request, send_file
# # from pytubefix import YouTube # type: ignore
# # import os
# # from moviepy.video.io.ffmpeg_tools import ffmpeg_merge_video_audio
# # import tempfile

# # app = Flask(__name__)

# # @app.route('/', methods=['GET', 'POST'])
# # def index():
# #     if request.method == 'POST':
# #         video_url = request.form['url']
# #         try:
# #             # Create a YouTube object with the provided URL
# #             yt = YouTube(video_url)

# #             # Select the highest resolution video stream (video-only)
# #             video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()

# #             # Select the highest quality audio stream (audio-only)
# #             audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()

# #             if not video_stream or not audio_stream:
# #                 return "No suitable video/audio stream found."

# #             # Create a temporary directory for files
# #             with tempfile.TemporaryDirectory() as temp_dir:
# #                 video_path = os.path.join(temp_dir, "video.mp4")
# #                 audio_path = os.path.join(temp_dir, "audio.mp4")
# #                 output_path = os.path.join(temp_dir, "output.mp4")

# #                 # Download video and audio streams to the temporary directory
# #                 video_file = video_stream.download(output_path=temp_dir, filename="video.mp4")
# #                 audio_file = audio_stream.download(output_path=temp_dir, filename="audio.mp4")

# #                 # Debugging: Print paths to ensure files are downloaded
# #                 print(f"Video file downloaded to: {video_file}")
# #                 print(f"Audio file downloaded to: {audio_file}")

# #                 # Ensure ffmpeg_merge_video_audio receives correct file paths
# #                 if os.path.isfile(video_file) and os.path.isfile(audio_file):
# #                     # Merge video and audio using ffmpeg
# #                     ffmpeg_merge_video_audio(video_file, audio_file, output_path, vcodec='copy', acodec='copy')

# #                     # Stream the combined file to the user
# #                     return send_file(output_path, as_attachment=True)
# #                 else:
# #                     return "Error: Video or audio file not found after download."

# #         except Exception as e:
# #             # Handle exceptions and provide feedback
# #             return f"An error occurred: {str(e)}"

# #     # Render the HTML form for GET requests
# #     return render_template('index.html')


# # if __name__ == '__main__':
# #     app.run(host='0.0.0.0', port=8000)

# from flask import Flask, render_template, request, send_file
# from pytubefix import YouTube # type: ignore
# import os
# from moviepy.video.io.ffmpeg_tools import ffmpeg_merge_video_audio
# import tempfile

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         video_url = request.form['url']
#         try:
#             # Create a YouTube object with the provided URL
#             yt = YouTube(video_url)

#             # Select the highest resolution video stream (video-only)
#             video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()

#             # Select the highest quality audio stream (audio-only)
#             audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()

#             if not video_stream or not audio_stream:
#                 return "No suitable video/audio stream found."

#             # Create a temporary directory for files
#             with tempfile.TemporaryDirectory() as temp_dir:
#                 video_path = os.path.join(temp_dir, "video.mp4")
#                 audio_path = os.path.join(temp_dir, "audio.mp4")
#                 output_path = os.path.join(temp_dir, "output.mp4")

#                 # Download video and audio streams to the temporary directory
#                 video_file = video_stream.download(output_path=temp_dir, filename="video.mp4")
#                 audio_file = audio_stream.download(output_path=temp_dir, filename="audio.mp4")

#                 # Debugging: Print paths to ensure files are downloaded
#                 print(f"Video file downloaded to: {video_file}")
#                 print(f"Audio file downloaded to: {audio_file}")

#                 # Ensure ffmpeg_merge_video_audio receives correct file paths
#                 if os.path.isfile(video_file) and os.path.isfile(audio_file):
#                     # Merge video and audio using ffmpeg
#                     ffmpeg_merge_video_audio(video_file, audio_file, output_path, vcodec='copy', acodec='copy')

#                     # Stream the combined file to the user
#                     return send_file(output_path, as_attachment=True)
#                 else:
#                     return "Error: Video or audio file not found after download."

#         except Exception as e:
#             # Handle exceptions and provide feedback
#             return f"An error occurred: {str(e)}"

#     # Render the HTML form for GET requests
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)
from flask import Flask, render_template, request, send_file
from pytubefix import YouTube # type: ignore
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_merge_video_audio
import tempfile

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['url']
        try:
            # Create a YouTube object with the provided URL
            yt = YouTube(video_url)

            # Select the highest resolution video stream (video-only)
            video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()

            # Select the highest quality audio stream (audio-only)
            audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()

            if not video_stream or not audio_stream:
                return "No suitable video/audio stream found."

            # Create a temporary directory for files
            with tempfile.TemporaryDirectory() as temp_dir:
                video_path = os.path.join(temp_dir, "video.mp4")
                audio_path = os.path.join(temp_dir, "audio.mp4")
                output_path = os.path.join(temp_dir, "output.mp4")

                # Download video and audio streams to the temporary directory
                video_file = video_stream.download(output_path=temp_dir, filename="video.mp4")
                audio_file = audio_stream.download(output_path=temp_dir, filename="audio.mp4")

                # Debugging: Print paths to ensure files are downloaded
                print(f"Video file downloaded to: {video_file}")
                print(f"Audio file downloaded to: {audio_file}")

                # Ensure ffmpeg_merge_video_audio receives correct file paths
                if os.path.isfile(video_file) and os.path.isfile(audio_file):
                    # Merge video and audio using ffmpeg
                    ffmpeg_merge_video_audio(video_file, audio_file, output_path, vcodec='copy', acodec='copy')

                    # Stream the combined file to the user
                    return send_file(output_path, as_attachment=True)
                else:
                    return "Error: Video or audio file not found after download."

        except Exception as e:
            # Handle exceptions and provide feedback
            return f"An error occurred: {str(e)}"

    # Render the HTML form for GET requests
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) # Adjust port if needed

