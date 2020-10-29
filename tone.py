
x = 2**(1/12)
freq = 130.81278265029934  # c0
notes = ['C ','C#','D ','Eb','E ','F ','F#','G ','Ab','A ','Bb','B ']

for octave in range(0,4):
    print(f'octave {octave}:')
    for note in notes:
        print(f'{note}: {round(freq,1)}')
        freq *= x
    print()