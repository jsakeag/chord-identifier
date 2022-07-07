MAJOR_SPACING = [0, 4, 7]
MINOR_SPACING = [0, 3, 7]

note_equivalent_map = {
    "B#": "C",
    "Db": "C#",
    "Eb": "D#",
    "Fb": "E",
    "E#": "F",
    "Gb": "F#",
    "Ab": "G#",
    "Bb": "A#",
    "Cb": "B"
}
note_index_map = {
    "C": 1,
    "C#": 2,
    "D": 3,
    "D#": 4,
    "E": 5,
    "F": 6,
    "F#": 7,
    "G": 8,
    "G#": 9,
    "A": 10,
    "A#": 11,
    "B": 12
}

# add between notes if less than prev note
# also translation method for different note forms
# function later?


def find_equivalent(chord):
    equivalent_chord = []
    for note in chord:
        if(note_equivalent_map.get(note) != None):
            equivalent_chord.append(note_equivalent_map[note])
        else:
            equivalent_chord.append(note)
    return equivalent_chord


def find_spacing(chord):
    chord_indexes = []
    first_index = note_index_map[chord[0]]
    for note in chord:
        note_index = note_index_map[note]  # .get
        note_index -= first_index
        if note_index < 0:
            note_index += len(note_index_map)  # 12
        chord_indexes.append(note_index)
    return chord_indexes


def invert(chord):
    chord.append(chord.pop(0))
    chord_spacing = find_spacing(chord)
    return chord, chord_spacing


def get_voicing(chord, spacing):
    # Second inversion takes one more inversion to go back to root
    # First takes two
    inversions_to_root = ["Root Chord",
                          "Second Inversion",
                          "First Inversion"]
    for i in range(0, 3):
        if(spacing == MAJOR_SPACING):
            return "Major", chord, inversions_to_root[i]
        elif(spacing == MINOR_SPACING):
            return "Minor", chord, inversions_to_root[i]
        chord, spacing = invert(chord)
    return "Other Voicing", "N/A", "N/A"


print("Enter three notes: ")
input_chord = []
for i in range(0, 3):
    input_note = input("Enter a note: ").capitalize()
    while(note_index_map.get(input_note) == None and note_equivalent_map.get(input_note) == None):  # might be messy
        print("Invalid note")
        input_note = input("Enter a note: ").capitalize()
    input_chord.append(input_note)

equivalent_chord = find_equivalent(input_chord)
chord_spacing = find_spacing(equivalent_chord)
chord_quality, root_chord, inversion = get_voicing(
    equivalent_chord, chord_spacing)
print(root_chord[0] + " " + chord_quality + " (" + inversion + ")")
print(str(root_chord) + " => " + str(input_chord))
