from midiutil import MIDIFile

# 1. 创建一个MIDI文件，1个音轨
midi = MIDIFile(1)
track = 0
time = 0
channel = 0
volume = 100

midi.addTrackName(track, time, "Code to Music")
midi.addTempo(track, time, 120)

# 2. 将文本映射成音符 (C大调音阶)
code_string = "HELLO_WORLD_I_LOVE_MUSIC"
note_map = {'H': 60, 'E': 62, 'L': 64, 'O': 65, '_': 67, 'W': 69, 'R': 71, 'D': 72, 'I': 74, 'V': 76, 'M': 77, 'U': 79, 'S': 81, 'C': 83}

for char in code_string:
    if char in note_map:
        pitch = note_map[char]
        midi.addNote(track, channel, pitch, time, 1, volume)
        time += 1

# 3. 保存文件
with open("output.mid", "wb") as output_file:
    midi.writeFile(output_file)
print("🎵 音乐生成完毕！")
