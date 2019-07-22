import music21

message = "love kali"

mappingsDictionary = {# letter : pitch
    "i" : "A3",
    "l": "B3",
    "o": "C4",
    "v": "D4",
    "e": "E4",
    "k": "F4",
    "a": "G4",
    "l": "G#4",
    "i": "A4"

}

keys = mappingsDictionary.keys()
# print(list(mappingsDictionary.values()))
# print(mappingsDictionary["v"])

harp = music21.instrument.Harp()
# print(harp)

noteLength = 1

# print("note length:", noteLength)

# from music21 import AcousticBass
#
# music21.instrument.AcousticBass

characterList = list( message )
# print(characterList)

s = music21.stream.Stream()
# print(s.show('text'))
p = music21.stream.Part()
# print(p.show('text'))
p.insert(0, harp)
# print( p.show('text'))

for letter in characterList:
    if letter in list(keys):
        pitch = mappingsDictionary[letter]
        nextNote = music21.note.Note(pitchName=pitch, quarterLength=noteLength)
        print(letter, pitch, nextNote)
    else:
        nextNote = music21.note.Rest(quarterLength = noteLength)
        print(letter, nextNote)

    p.append(nextNote)

p.show('text')
s.append(p)
print("\n Stream \n")
p.show('text')
s.write('midi', fp="lovekali.mid")



