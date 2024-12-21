# Hocam çalışması için simpleaudio kütüphanesini indirmeyi unutmayınız.

import numpy as np
import simpleaudio as sa

TURKISH_ALPHABET = [
    'A','B','C','Ç','D','E','F','G','Ğ','H','I','İ',
    'J','K','L','M','N','O','Ö','P','R','S','Ş','T',
    'U','Ü','V','Y','Z'
]

LETTER_TO_NOTE = {
    'A': 'C4',   'B': 'D4',   'C': 'E4',   'Ç': 'F4',   'D': 'G4',
    'E': 'A4',   'F': 'B4',   'G': 'C5',   'Ğ': 'D5',   'H': 'E5',
    'I': 'F5',   'İ': 'G5',   'J': 'A5',   'K': 'B5',   'L': 'C6',
    'M': 'D6',   'N': 'E6',   'O': 'F6',   'Ö': 'G6',   'P': 'A6',
    'R': 'B6',   'S': 'C7',   'Ş': 'D7',   'T': 'E7',   'U': 'F7',
    'Ü': 'G7',   'V': 'A7',   'Y': 'B7',   'Z': 'C8'
}

NOTE_FREQUENCIES = {
    'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23, 'G4': 392.00,
    'A4': 440.00, 'B4': 493.88, 'C5': 523.25, 'D5': 587.33, 'E5': 659.25,
    'F5': 698.46, 'G5': 783.99, 'A5': 880.00, 'B5': 987.77, 'C6': 1046.50,
    'D6': 1174.66, 'E6': 1318.51, 'F6': 1396.91, 'G6': 1567.98, 'A6': 1760.00,
    'B6': 1975.53, 'C7': 2093.00, 'D7': 2349.32, 'E7': 2637.02, 'F7': 2793.83,
    'G7': 3135.96, 'A7': 3520.00, 'B7': 3951.07, 'C8': 4186.01
}

def play_tone_combined(freqs, duration=0.25, volume=0.3):
    if not freqs:
        return

    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    combined_wave = np.zeros_like(t)

    individual_volume = volume / max(1, len(freqs))
    
    for f in freqs:
        tone = np.sin(f * 2 * np.pi * t) * individual_volume
        combined_wave += tone

    audio = combined_wave * (2**15 - 1)
    audio = audio.astype(np.int16)
    
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    play_obj.wait_done()

def play_text_from_both_ends(text):
    i = 0
    j = len(text) - 1

    while i <= j:
        char1 = text[i].upper()
        char2 = text[j].upper()

        freqs_to_play = []
        
        if char1 in LETTER_TO_NOTE:
            freq1 = NOTE_FREQUENCIES[LETTER_TO_NOTE[char1]]
            freqs_to_play.append(freq1)
        
        if i != j:
            if char2 in LETTER_TO_NOTE:
                freq2 = NOTE_FREQUENCIES[LETTER_TO_NOTE[char2]]
                freqs_to_play.append(freq2)
        
        play_tone_combined(freqs_to_play, duration=0.15, volume=0.3)
        i += 1
        j -= 1

istiklal_marsi = """
Korkma, sönmez bu şafaklarda yüzen al sancak;
Sönmeden yurdumun üstünde tüten en son ocak.
O benim milletimin yıldızıdır, parlayacak;
O benimdir, o benim milletimindir ancak.
"""

play_text_from_both_ends(istiklal_marsi)