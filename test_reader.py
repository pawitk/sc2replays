import sc2reader
import os

# path = "/replays/ggtracker_6376199.SC2Replay"
path = "/replays/ggtracker_6236138.SC2Replay"
replay = sc2reader.load_replay(os.getcwd() + path)