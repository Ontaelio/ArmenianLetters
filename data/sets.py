from typing import List
from pydantic import BaseModel

from data.letters import *


class LettersSet(BaseModel):
    name: str
    contents: dict
    front_name: str
    title: str
    offset: bool = False


class SetResponse(BaseModel):
    name: str
    front_name: str
    title: str
    offset: bool


class BookSet(BaseModel):
    id: int
    name: str
    contents: List[LettersSet]
    columns: set = ()


class BookResponse(BaseModel):
    id: int
    name: str
    contents: List[SetResponse]
    columns: set = ()


# this function can be used to provide values for LettersSet.title
# may be used right in the set, but after it's better to run the main() below to produce a ready string
def create_title(letters: dict) -> str:
    res_dict = {}
    res_list = []
    for key, value in letters.items():
        ru_letter = key.upper() + key.lower()
        if ru_letter not in res_dict.keys():
            res_dict[ru_letter] = value.upper() + value.lower()
            res_list.append(ru_letter + ' ' + value.upper() + value.lower())
    return ' | '.join(res_list)


# check if all Armenian letters are included
def check_set(book: BookSet) -> list:
    s1 = set()
    for c in book.contents:
        for b in c.contents.values():
            # print(b)
            s1.add(b)
    s2 = set(l for l in ARMENIAN_ALPHABET.values())
    return list(s2-s1)


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
    'lesson_1a': LESSON_1A,
    'lesson_1b': LESSON_1B,
    'lesson_1c': LESSON_1C,
    'lesson_1d': LESSON_1D,
    'lesson_2a': LESSON_2A,
    'lesson_2b': LESSON_2B,
    'lesson_2c': LESSON_2C,
    'lesson_2d': LESSON_2D,

    'par_man_1a': PAR_MAN_1A,
    'par_man_1b': PAR_MAN_1B,
    'par_man_1c': PAR_MAN_1C,
    'par_man_1d': PAR_MAN_1D,
    'par_man_2a': PAR_MAN_2A,
    'par_man_2b': PAR_MAN_2B,
    'par_man_2c': PAR_MAN_2C,
    'par_man_2d': PAR_MAN_2D,
    'par_man_3a': PAR_MAN_3A,
    'par_man_3b': PAR_MAN_3B,
    'par_man_3c': PAR_MAN_3C,
    'par_man_3d': PAR_MAN_3D,
    'par_man_4a': PAR_MAN_4A,
    'par_man_4b': PAR_MAN_4B,
    'par_man_4c': PAR_MAN_4C,
    'par_man_5a': PAR_MAN_5A,
    'par_man_5b': PAR_MAN_5B,
    'par_man_5c': PAR_MAN_5C,

    'vowels': VOWELS,
    'vowels_auye': VOWELS_AUYE,
    'vowels_ieo': VOWELS_IEO,
    'vowels_j': VOWELS_ADD_J,
    'vowels_vojev': VOWELS_ADD_VOEV,
    'vowels_bI': VOWELS_ADD_,
    'consonants': CONSONANTS,
    'consonants_bp': CONSONANTS_BP,
    'consonants_gk': CONSONANTS_GK,
    'consonants_dt': CONSONANTS_DT,
    'consonants_jrh': CONSONANTS_JRH,
    'consonants_lmn': CONSONANTS_LMN,
    'consonants_vzh': CONSONANTS_VZH,
    'consonants_zch': CONSONANTS_ZCH,
    'consonants_fsh': CONSONANTS_FSH,
    'consonants_sc': CONSONANTS_SC,
    'consonants_altr': CONSONANTS_ALTR,
    'consonants_altg': CONSONANTS_ALTG,
    'consonants_alth': CONSONANTS_ALTH,
    'consonants_altpkt': CONSONANTS_ALTPKT,
    'consonants_softt': CONSONANTS_SOFTT,
    'consonants_dzs': CONSONANTS_DZS,
    'consonants_tsch': CONSONANTS_TSCH,
    'consonants_both_rs': CONSONANTS_BOTH_RS,
    'consonants_vowel_pkt': CONSONANTS_VOWEL_PKT,
}


TIOYAN = BookSet(
    id=1,
    name='Самоучитель Сусанна Тиоян et al.',
    contents=[
        LettersSet(
            name="Урок 1 - Աա ՈՒու Բբ Պպ Գգ Կկ Դդ Տտ Րր Լլ Մմ Նն",
            contents=LESSON_1,
            front_name='lesson_1',
            title="Аа Աա | Уу ՈՒու | Бб Բբ | Пп Պպ | Гг Գգ | Кк Կկ | Дд Դդ | Тт Տտ | Рр Րր | Лл Լլ | Мм Մմ | Нн Նն"
        ),
        LettersSet(
            name="Только Աա ՈՒու",
            contents=LESSON_1A,
            front_name='lesson_1a',
            title="Аа Աա | Уу ՈՒու",
            offset=True
        ),
        LettersSet(
            name="Только Բբ Գգ Դդ",
            contents=LESSON_1B,
            front_name='lesson_1b',
            title="Бб Բբ | Гг Գգ | Дд Դդ",
            offset=True
        ),
        LettersSet(
            name="Только Պպ Կկ Տտ",
            contents=LESSON_1C,
            front_name='lesson_1c',
            title="Пп Պպ | Кк Կկ | Тт Տտ",
            offset=True
        ),
        LettersSet(
            name="Только Րր Լլ Մմ Նն",
            contents=LESSON_1D,
            front_name='lesson_1d',
            title="Рр Րր | Лл Լլ | Мм Մմ | Нн Նն",
            offset=True
        ),
        LettersSet(
            name="Урок 2 - Իի Յյ Խխ Շշ Ժժ Չչ Սս Զզ Ցց Ֆֆ Վվ",
            contents=LESSON_2,
            front_name='lesson_2',
            title="Ии Իի | Йй Յյ | Хх Խխ | Шш Շշ | Жж Ժժ | Чч Չչ | Сс Սս | Зз Զզ | Цц Ցց | Фф Ֆֆ | Вв Վվ"
        ),
        LettersSet(
            name="Только Իի Յյ",
            contents=LESSON_2A,
            front_name='lesson_2a',
            title="Ии Իի | Йй Յյ",
            offset=True
        ),
        LettersSet(
            name="Только Խխ Շշ Չչ Ցց",
            contents=LESSON_2B,
            front_name='lesson_2b',
            title="Хх Խխ | Шш Շշ | Чч Չչ | Цц Ցց",
            offset=True
        ),
        LettersSet(
            name="Только Ժժ Սս Զզ",
            contents=LESSON_2C,
            front_name='lesson_2c',
            title="Жж Ժժ | Сс Սս | Зз Զզ",
            offset=True
        ),
        LettersSet(
            name="Только Ֆֆ Վվ",
            contents=LESSON_2D,
            front_name='lesson_2d',
            title="Фф Ֆֆ | Вв Վվ",
            offset=True
        ),
        LettersSet(
            name="Урок 3 - Եե Էէ",
            contents=LESSON_3,
            front_name='lesson_3',
            title="Ээ Էէ | Ее Եե"
        ),
        LettersSet(
            name="Урок 4 - և Օօ Ոո",
            contents=LESSON_4,
            front_name='lesson_4',
            title="ЕВ/ев ԵՒ/և | Во. Ոո | О. Օօ | .о./.о Ոո"
        ),
        LettersSet(
            name="Урок 5 - Հհ Ղղ Ռռ",
            contents=LESSON_5,
            front_name='lesson_5',
            title="Хх Հհ | Гг Ղղ | Рр Ռռ"
        ),
        LettersSet(
            name="Урок 6 - Ըը (Ы)",
            contents=LESSON_6,
            front_name='lesson_6',
            title="Ыы Ըը"
        ),
        LettersSet(
            name="Урок 7 - Փփ",
            contents=LESSON_7,
            front_name='lesson_7',
            title="Пп Փփ"
        ),
        LettersSet(
            name="Урок 8 - Քք",
            contents=LESSON_8,
            front_name='lesson_8',
            title="Кк Քք"
        ),
        LettersSet(
            name="Урок 9 - Թթ",
            contents=LESSON_9,
            front_name='lesson_9',
            title="Тт Թթ"
        ),
        LettersSet(
            name="Урок 10 - Ձձ Ծծ (ДЗ, ТЬ)",
            contents=LESSON_10,
            front_name='lesson_10',
            title="ДЗдз Ձձ | Т'т' Ծծ"
        ),
        LettersSet(
            name="Урок 11 - Ջջ Ճճ (ДЖ, Ч)",
            contents=LESSON_11,
            front_name='lesson_11',
            title="ДЖдж Ջջ | Чч Ճճ"
        ),
    ],
    columns=('lesson_3',)
)

PARNASIAN = BookSet(
    id=3,
    name='Самоучитель Парнасян Н.А., Манукян Ж.К.',
    contents=[
            LettersSet(
                name="Урок 1 - Աա Իի ՈՒու",
                contents=PAR_MAN_1A,
                front_name='par_man_1a',
                title="Аа Աա | Ии Իի | Уу ՈՒու"
            ),
            LettersSet(
                name="Урок 1 - Էէ Եե",
                contents=PAR_MAN_1B,
                front_name='par_man_1b',
                title="Ээ Էէ | Ее Եե"
            ),
            LettersSet(
                name="Урок 1 - Զզ Սս Ժժ Շշ",
                contents=PAR_MAN_1C,
                front_name='par_man_1c',
                title="Зз Զզ | Сс Սս | Жж Ժժ | Шш Շշ"
            ),
            LettersSet(
                name="Урок 1 - Լլ Մմ Նն",
                contents=PAR_MAN_1D,
                front_name='par_man_1d',
                title="Лл Լլ | Мм Մմ | Нн Նն"
            ),
            LettersSet(
                name="Урок 2 - Ոո Օօ",
                contents=PAR_MAN_2A,
                front_name='par_man_2a',
                title="Оо Ոո | О... Օօ | Во... Ոո"
            ),
            LettersSet(
                name="Урок 2 - Ըը (Ы)",
                contents=PAR_MAN_2B,
                front_name='par_man_2b',
                title="Ыы Ըը"
            ),
            LettersSet(
                name="Урок 2 - Յյ",
                contents=PAR_MAN_2C,
                front_name='par_man_2c',
                title="Йй Յյ"
            ),
            LettersSet(
                name="Урок 2 - Րր Ռռ",
                contents=PAR_MAN_2D,
                front_name='par_man_2d',
                title="Р'р' Րր | Рр Ռռ"
            ),
            LettersSet(
                name="Урок 3 - Ֆֆ Վվ",
                contents=PAR_MAN_3A,
                front_name='par_man_3a',
                title="Фф Ֆֆ | Вв Վվ"
            ),
            LettersSet(
                name="Урок 3 - և",
                contents=PAR_MAN_3B,
                front_name='par_man_3b',
                title="ев և"
            ),
            LettersSet(
                name="Урок 3 - Գգ Խխ",
                contents=PAR_MAN_3C,
                front_name='par_man_3c',
                title="Гг Գգ | Хх Խխ"
            ),
            LettersSet(
                name="Урок 3 - Հհ (Х)",
                contents=PAR_MAN_3D,
                front_name='par_man_3d',
                title="Хх Հհ"
            ),
            LettersSet(
                name="Урок 4 - Բբ Գգ Դդ",
                contents=PAR_MAN_4A,
                front_name='par_man_4a',
                title="Бб Բբ | Гг Գգ | Дд Դդ"
            ),
            LettersSet(
                name="Урок 4 - Պպ Կկ Տտ",
                contents=PAR_MAN_4B,
                front_name='par_man_4b',
                title="Пп Պպ | Кк Կկ | Тт Տտ"
            ),
            LettersSet(
                name="Урок 4 - Փփ Քք Թթ",
                contents=PAR_MAN_4C,
                front_name='par_man_4c',
                title="Пп Փփ | Кк Քք | Тт Թթ"
            ),
            LettersSet(
                name="Урок 5 - Ձձ Ծծ Ցց",
                contents=PAR_MAN_5A,
                front_name='par_man_5a',
                title="ДЗдз Ձձ | Т'т' Ծծ | Цц Ցց"
            ),
            LettersSet(
                name="Урок 5 - Ջջ Չչ",
                contents=PAR_MAN_5B,
                front_name='par_man_5b',
                title="ДЖдж Ջջ | Чч Չչ"
            ),
            LettersSet(
                name="Урок 5 - Ճճ (Ч)",
                contents=PAR_MAN_5C,
                front_name='par_man_5c',
                title="Чч Ճճ"
            ),
    ],
    columns=('par_man_2c', 'par_man_4a')
)

JUST_LETTERS = BookSet(
    id=2,
    name='Наборы букв',
    contents=[
        LettersSet(
            name="Гласные",
            contents=VOWELS,
            front_name='vowels',
            title="Аа Աա | Уу ՈՒու | Ии Իի | Ээ Էէ | Ее Եե | О... Օօ | Оо Ոո"
        ),
        LettersSet(
            name="Ա, ՈՒ, Ե",
            contents=VOWELS_AUYE,
            front_name='vowels_auye',
            title="Аа Աա | Уу ՈՒու | Ее Եե",
            offset=True
        ),
        LettersSet(
            name="Ի, Է, Ո, Օ",
            contents=VOWELS_IEO,
            front_name='vowels_ieo',
            title="Ии Իի | Ээ Էէ | О... Օօ | Оо Ոո",
            offset=True
        ),
        LettersSet(
            name="Я, Ё, Ю с Յ",
            contents=VOWELS_ADD_J,
            front_name='vowels_j',
            title="Яя ՅԱ/յա | Ёё ՅՈ/յո | Юю ՅՈՒ/յու"
        ),
        LettersSet(
            name='Ո как "во" в начале слова, և',
            contents=VOWELS_ADD_VOEV,
            front_name='vowels_vojev',
            title="ЕВ/ев ԵՒ/և | Во... Ոո"
        ),
        LettersSet(
            name='Ы -> Ըը',
            contents=VOWELS_ADD_,
            front_name='vowels_bI',
            title="Ыы Ըը"
        ),

        LettersSet(
            name="Согласные",
            contents=CONSONANTS,
            front_name='consonants',
            title="Бб Բբ | Пп Պպ | Гг Գգ | Кк Կկ | Дд Դդ | Тт Տտ | Рр Րր | Лл Լլ | Мм Մմ | Нн Նն | Йй Յյ | Хх Խխ | Шш Շշ | Жж Ժժ | Чч Չչ | Сс Սս | Зз Զզ | Цц Ցց | Фф Ֆֆ | Вв Վվ"
        ),
        LettersSet(
            name="Բ, Պ",
            contents=CONSONANTS_BP,
            front_name='consonants_bp',
            title="Бб Բբ | Пп Պպ",
            offset=True
        ),
        LettersSet(
            name="Գ, Կ",
            contents=CONSONANTS_GK,
            front_name='consonants_gk',
            title="Гг Գգ | Кк Կկ",
            offset=True
        ),
        LettersSet(
            name="Դ, Տ",
            contents=CONSONANTS_DT,
            front_name='consonants_dt',
            title="Дд Դդ | Тт Տտ",
            offset=True
        ),
        LettersSet(
            name="Յ, Ր, Խ",
            contents=CONSONANTS_JRH,
            front_name='consonants_jrh',
            title="Йй Յյ | Рр Րր | Хх Խխ",
            offset=True
        ),
        LettersSet(
            name="Լ, Մ, Ն",
            contents=CONSONANTS_LMN,
            front_name='consonants_lmn',
            title="Лл Լլ | Мм Մմ | Нн Նն",
            offset=True
        ),
        LettersSet(
            name="Վ, Ժ",
            contents=CONSONANTS_VZH,
            front_name='consonants_vzh',
            title="Вв Վվ | Жж Ժժ",
            offset=True
        ),
        LettersSet(
            name="Ֆ, Շ",
            contents=CONSONANTS_FSH,
            front_name='consonants_fsh',
            title="Фф Ֆֆ | Шш Շշ",
            offset=True
        ),
        LettersSet(
            name="Զ, Չ",
            contents=CONSONANTS_ZCH,
            front_name='consonants_zch',
            title="Зз Զզ | Чч Չչ",
            offset=True
        ),
        LettersSet(
            name="Ս, Ց",
            contents=CONSONANTS_SC,
            front_name='consonants_sc',
            title="Сс Սս | Цц Ցց",
            offset=True
        ),

        LettersSet(
            name="Ռռ вместо Րր (ближе к русской Р)",
            contents=CONSONANTS_ALTR,
            front_name='consonants_altr',
            title="Рр Ռռ"
        ),
        LettersSet(
            name="Использовать Րր и Ռռ, Րր для мягкой Р",
            contents=CONSONANTS_BOTH_RS,
            front_name='consonants_both_rs',
            title="Рр Ռռ | Р'р' Րր"
        ),
        LettersSet(
            name="Ղղ вместо Գգ (южный говор!)",
            contents=CONSONANTS_ALTG,
            front_name='consonants_altg',
            title="Гг Ղղ"
        ),
        LettersSet(
            name="Х как Հհ вместо Խխ",
            contents=CONSONANTS_ALTH,
            front_name='consonants_alth',
            title="Хх Հհ"
        ),
        LettersSet(
            name="П, К, Т с придыханием (Փփ Քք Թթ)",
            contents=CONSONANTS_ALTPKT,
            front_name='consonants_altpkt',
            title="Пп Փփ | Кк Քք | Тт Թթ"
        ),
        LettersSet(
            name="Պպ Կկ Տտ перед гласными, иначе Փփ Քք Թթ",
            contents=CONSONANTS_VOWEL_PKT,
            front_name='consonants_vowel_pkt',
            title="Та Տտ | Тр Թթ | Па Պպ | Пр Փփ | Ка Կկ | Кр Քք"
        ),
        LettersSet(
            name="Ծծ для мягкой Т",
            contents=CONSONANTS_SOFTT,
            front_name='consonants_softt',
            title="Т'т' Ծծ"
        ),
        LettersSet(
            name="Ձձ Ջջ (для дж хороши тексты про Джорджа и Джин)",
            contents=CONSONANTS_DZS,
            front_name='consonants_dzs',
            title="ДЗдз Ձձ | ДЖдж Ջջ"
        ),
        LettersSet(
            name="Щ -> Ճ (на самом деле звучит как ТШ!))",
            contents=CONSONANTS_TSCH,
            front_name='consonants_tsch',
            title="Щщ Ճճ"
        ),
    ],
    columns=('consonants', 'consonants_altr')
)

BOOKS_SELECTION = {
    TIOYAN.id: TIOYAN,
    PARNASIAN.id: PARNASIAN,
    JUST_LETTERS.id: JUST_LETTERS,
}

if __name__ == '__main__':
    for _, book in BOOKS_SELECTION.items():
        print(f'\n**** {_} ****')
        for l_set in book.contents:
            print(f'{l_set.front_name}: "{l_set.title}"')

    for book in BOOKS_SELECTION.values():
        print(book.name, check_set(book))
