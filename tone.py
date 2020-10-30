
x = 2**(1/12)
freq = 130.81278265029934 / 2  # c-1
notes = ['C ','C#','D ','Eb','E ','F ','F#','G ','Ab','A ','Bb','B ']


print()
print('Frequencies of notes:')

for octave in range(-1,4):
    print(f'octave {octave}:')
    for note in notes:
        print(f'{note}: {round(freq,1)}')
        freq *= x
    print()