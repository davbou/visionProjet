import os
from vlc import Instance
from time import sleep


PATH = r"C:\Users\mpbel\Music\20syl"

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
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

    def toune_suivante(self):
        self.player.next()

    def toune_precedente(self):
        self.player.previous()


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
