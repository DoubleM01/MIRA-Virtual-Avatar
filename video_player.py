import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
import os

class VideoPlayer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MIRA - Video Player")
        self.setGeometry(200, 100, 800, 500)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        videoWidget = QVideoWidget()

        self.openBtn = QPushButton("Play Generated Video")

        self.openBtn.clicked.connect(self.play_video)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addWidget(self.openBtn)

        self.setLayout(layout)
        self.mediaPlayer.setVideoOutput(videoWidget)
        self.play_video()

    def play_video(self):
        self.openBtn.setEnabled(False)
        video_path = "output/results.mp4"
        os.remove(video_path.replace("results.mp4","converted.avi")) if os.path.exists(video_path.replace("results.mp4","converted.avi")) else None  # Remove old converted file if exists
        os.chdir(os.path.dirname(video_path))  # Change to the directory of the video file
        
        os.system("ffmpeg -i results.mp4 -vcodec msmpeg4 -acodec mp2 converted.avi")
        self.mediaPlayer.setMedia(QMediaContent(QUrl.fromLocalFile(video_path.replace("results.mp4","converted.avi"))))
        self.mediaPlayer.setVolume(100)
        self.mediaPlayer.play()
        os.chdir('..')
        #os.chdir(os.path.dirname() + os.path.abspath(__file__))  # Change back to the original directory
        print(os.getcwd())
        self.openBtn.setEnabled(True)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())
