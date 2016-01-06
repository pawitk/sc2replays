import sys
import argparse
import pprint
import json
import os

sys.path.insert(0, './s2protocol')

from mpyq import mpyq
import protocol15405

def load_data(filepath):
    archive = mpyq.MPQArchive(filepath)
    contents = archive.header['user_data_header']['content']
    header = protocol15405.decode_replay_header(contents)
    baseBuild = header['m_version']['m_baseBuild']
    print 'Basebuild',baseBuild
    protocol = __import__('protocol%s' % (baseBuild,))
    # contents = archive.read_file('replay.details')
    # details = protocol.decode_replay_details(contents)
    # contents = archive.read_file('replay.initData')
    # initdata = protocol.decode_replay_initdata(contents)
    contents = archive.read_file('replay.game.events')
    events = list(protocol.decode_replay_game_events(contents))
    contents = archive.read_file('replay.message.events')
    messages = list(protocol.decode_replay_message_events(contents))
    # if hasattr(protocol, 'decode_replay_tracker_events'):
    #     contents = archive.read_file('replay.tracker.events')
    #     tracker_events = protocol.decode_replay_tracker_events(contents)
    # contents = archive.read_file('replay.attributes.events')
    # attributes = protocol.decode_replay_attributes_events(contents)
    return [events,messages]

def main():
    # path = sys.argv[1]
    path = os.path.dirname(os.path.abspath(__file__)) + '/replays/ggtracker_6376199.SC2Replay'
    print path
    events,messages = load_data(path)
    with open('events.json', 'w') as outfile:
        json.dump(events, outfile)
    with open('messages.json', 'w') as outfile:
        json.dump(messages, outfile)

if __name__ == '__main__':
    main()