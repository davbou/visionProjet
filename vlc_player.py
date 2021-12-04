import os
from vlc import Instance
from time import sleep


PATH = r"C:\Users\mpbel\Music\20syl"
TIME_BUFFER = 2

class VLCPlayer:
    def __init__(self, path):
        vlc = Instance('--loop')
        liste_lecture = vlc.media_list_new()
        
        tounes = os.listdir(path)
        for t in tounes:
            liste_lecture.add_media(vlc.media_new(os.path.join(path, t)))

        self.player = vlc.media_list_player_new()
        self.player.set_media_list(liste_lecture)
    
    def play(self):
        if not self.player.is_playing():
            self.player.play()
            self.time_buffer()

    def pause(self):
        if self.player.is_playing():
            self.player.pause()
            self.time_buffer()

    def stop(self):
        if self.player.is_playing():
            self.player.stop()
            self.time_buffer()

    def toune_suivante(self):
        self.player.next()
        self.time_buffer()

    def toune_precedente(self):
        self.player.previous()
        self.time_buffer()

    def time_buffer(self):
        sleep(TIME_BUFFER)

if __name__ == "__main__":
    player = VLCPlayer(PATH)
    player.play()
    sleep(2)
    player.pause()
    sleep(1)
    player.toune_suivante()
    player.play()
    sleep(3)
    player.toune_precedente()
    sleep(3)
    player.stop()
    sleep(2)
    print("fini")
