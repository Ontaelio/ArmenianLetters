from dataclasses import dataclass, field

from data.letters import *

SETS = {
    'lesson_1': LESSON_1,
    'lesson_2': LESSON_2,
    'lesson_3': LESSON_3,
    'lesson_4': LESSON_4,
    'lesson_5': LESSON_5,
    'lesson_6': LESSON_6,
    'lesson_7': LESSON_7,
    'lesson_8': LESSON_8,
    'lesson_9': LESSON_9,
    'lesson_10': LESSON_10,
    'lesson_11': LESSON_11,
    'vowels': VOWELS,
    'vowels_j': VOWELS_ADD_J,
    'vowels_vojev': VOWELS_ADD_VOEV,
    'vowels_bI': VOWELS_ADD_,
    'consonants': CONSONANTS,
    'consonants_altr': CONSONANTS_ALTR,
    'consonants_altg': CONSONANTS_ALTG,
    'consonants_alth': CONSONANTS_ALTH,
    'consonants_altpkt': CONSONANTS_ALTPKT,
    'consonants_softt': CONSONANTS_SOFTT,
    'consonants_dzs': CONSONANTS_DZS,
    'consonants_tsch': CONSONANTS_TSCH,
    'consonants_both_rs': CONSONANTS_BOTH_RS,
    'consonants_vowel_pkt': CONSONANTS_VOWEL_PKT,
    'lesson_1a': LESSON_1A,
    'lesson_1b': LESSON_1B,
    'lesson_1c': LESSON_1C,
    'lesson_1d': LESSON_1D,
    'lesson_2a': LESSON_2A,
    'lesson_2b': LESSON_2B,
    'lesson_2c': LESSON_2C,
    'lesson_2d': LESSON_2D,
}


@dataclass
class LettersSet:
    name: str
    contents: dict
    front_name: str
    title: str
    offset: bool = False


def prepare_set(letters: dict) -> str:
    res_dict = {}
    res_list = []
    for key, value in letters.items():
        ru_letter = key.upper()+key.lower()
        if ru_letter not in res_dict.keys():
            res_dict[ru_letter] = value.upper()+value.lower()
            res_list.append(ru_letter + ' ' + value.upper()+value.lower())
    return ' | '.join(res_list)


SETS_SELECTION = {
    'Наборы букв': {
        1: [
            LettersSet(
                name="Согласные",
                contents=CONSONANTS,
                front_name='consonants',
                title=prepare_set(CONSONANTS)
            ),
            LettersSet(
                name="Ռռ вместо Րր (ближе к русской Р)",
                contents=CONSONANTS_ALTR,
                front_name='consonants_altr',
                title=prepare_set(CONSONANTS_ALTR),
                offset=True
            ),
        ],
        2: [
            LettersSet(
                name="Использовать Րր и Ռռ, Րր для мягкой Р",
                contents=CONSONANTS_BOTH_RS,
                front_name='consonants_both_rs',
                title=prepare_set(CONSONANTS_BOTH_RS)
            ),

        ]
    }
}
