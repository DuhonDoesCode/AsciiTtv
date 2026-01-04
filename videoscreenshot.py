import queue
from threading import Thread
import cv2
from ascii import Ascii
import json
from rich.live import Live
from rich.console import Console
from rich.text import Text
import time
from chafaDisplay import ChafaDisplay


class Display(object):
    def __init__(self, src=0):
        self.colored = json.loads(open('config.json', 'r+', encoding='utf-8').read())['colored']
        # Create a VideoCapture object
        self.capture = cv2.VideoCapture(src, cv2.CAP_FFMPEG)
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.capture.set(cv2.CAP_PROP_FPS, 60)

        self.frame_queue = queue.Queue(maxsize=100)
        self.latestTime = 0

        # Default resolutions of the frame are obtained (system dependent)
        self.frame_width = int(self.capture.get(3))
        self.frame_height = int(self.capture.get(4))

        # Start the thread to read frames from the video stream
        self.thread = Thread(target=self.update, args=())
        self.thread.daemon = True
        self.thread.start()
        self.asciiQ = queue.Queue(maxsize=100)
        self.status = None

        # Chafa
        self.display = None
        self.chafaQueue = queue.Queue(maxsize=100)

    def update(self):
        while self.capture.isOpened():
            self.capture.grab()
            now = time.monotonic()
            if now - self.latestTime >= 1/30:
                ret, frame = self.capture.retrieve()
                self.status = ret
                if ret:
                    self.frame = frame
                    self.latestTime = now
                    self.frame_queue.put_nowait(self.frame)
            
            if self.frame_queue.qsize() > 50:
                for i in range(20):
                    self.frame_queue.get()
                

    def renderToAscii(self, colors):
        while self.capture.isOpened():
            qframe = self.frame_queue.get()
            frame = Ascii(img=qframe, colors=colors)
            frame = frame.imgToAscii(self.colored)
            if self.asciiQ.qsize() < 100:
                self.asciiQ.put_nowait(frame)

    def prep_frame(self):
        usechafa = int(json.loads(open('config.json', 'r', encoding='utf-8').read())['usechafa'])
        res = int(json.dumps(json.loads(open("config.json", "r", encoding='utf-8').read())["resolution"]))
        colors = json.loads(open("config.json", "r", encoding='utf-8').read())["tileset"]
        if usechafa:
            self.chafaThread = Thread(target=self.chafaDisplay, args=(res,))
            self.chafaThread.daemon = True
            self.chafaThread.start()
        else:
            self.asciiThread = Thread(target=self.renderToAscii, args=(colors,))
            self.asciiThread.daemon = True
            self.asciiThread.start()

    def show_frame(self):
        console = Console(
            force_terminal=True,
            markup=False,
            highlight=False,
            emoji=False
        )
        
        usechafa = int(json.loads(open('config.json', 'r+', encoding='utf-8').read())['usechafa'])
        try:
            if not usechafa:
                with Live("", console=console, refresh_per_second=24, screen=True) as live:
                    while True:
                        if self.status:
                            if self.asciiQ.qsize() > 0:
                                self.display = self.asciiQ.get()
                                if self.colored:
                                    live.update(Text.from_ansi(self.display))
                                else:
                                    live.update(self.display)
            else:
                with Live("", console=console, refresh_per_second=24, screen=True) as live:
                    amount = 0
                    while True:
                        if self.status:
                            if self.chafaQueue.qsize() > 0:
                                self.display = self.chafaQueue.get_nowait()
                                amount += 1
                                live.update(Text.from_ansi(self.display))

        except queue.Empty:
            print("Queue empty!")

    def chafaDisplay(self, res):
        while self.capture.isOpened():
            frame = self.frame_queue.get()
            if self.chafaQueue.qsize() < 100:
                self.chafaQueue.put_nowait(ChafaDisplay(frame, res).draw())
        