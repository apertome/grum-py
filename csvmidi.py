#!/usr/bin/python

import csv
from mido import Message, MidiFile, MidiTrack



mid = MidiFile()
track = MidiTrack()
track2 = MidiTrack()
track3 = MidiTrack()
track4 = MidiTrack()
mid.tracks.append(track)
mid.tracks.append(track2)
mid.tracks.append(track3)
mid.tracks.append(track4)

#track.append(Message('program_change', program=12, time=0))


with open('arrays1_formidi.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print('Column names are', row)
            line_count += 1
        else:
            control = 0
            #print('\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            print('Values are', row);
            print('playing midi note ', row[0]);
            note = int(row[0])
            note2 = int(row[1])
            note3 = int(row[2])
            note4 = int(row[3])
            channel = 0
            control += 1
            #print("line_count", line_count);
            print("control", control);

            track.append(Message('control_change', channel=channel, control=control, value=note, time=0))
            track.append(Message('note_on', channel=channel, note=note, velocity=64, time=0))
            track.append(Message('note_off', channel=channel, note=note, velocity=127, time=32))

            control += 1
            channel += 1

            track2.append(Message('note_on', channel=channel, note=note2, velocity=64, time=64))
            track2.append(Message('note_off', channel=channel, note=note2, velocity=127, time=64))
            track2.append(Message('control_change', channel=channel, control=control, value=note2, time=64))

            control += 1
            channel += 1

            track3.append(Message('note_on', channel=channel, note=note3, velocity=64, time=48))
            track3.append(Message('note_off', channel=channel, note=note3, velocity=64, time=48))
            track3.append(Message('control_change', channel=channel, control=control, value=note4, time=48))

            control += 1
            channel += 1
            track4.append(Message('note_on', channel=channel, note=note4, velocity=64, time=16))
            track4.append(Message('note_off', channel=channel, note=note4, velocity=64, time=256))
            track4.append(Message('control_change', channel=channel, control=control, value=note4, time=16))
            line_count += 1
    print('Processed {line_count} lines.', line_count)


mid.save('new_song.mid')

