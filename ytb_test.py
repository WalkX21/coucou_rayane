import webview

def open_youtube_video():
    webview.create_window("YouTube Video Player", "https://open.spotify.com/playlist/52csi3p0Hg2MSk6UopOOFS", width=800, height=600)

if __name__ == '__main__':
    open_youtube_video()
    webview.start()