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


@dataclass
class SetResponse:
    name: str
    front_name: str
    title: str
    offset: bool


# this function can be used to provide values for LettersSet.title
# may be used right in the set, but better run the main() below to produce a ready string
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
    'Самоучитель Сусанна Тиоян et al.': {
        1: [
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
        ],
        2: [
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
                name="Урок 11 - Ջջ Ճճ (ДЖ, Щ)",
                contents=LESSON_11,
                front_name='lesson_11',
                title="ДЖдж Ջջ | Щщ Ճճ"
            ),
        ]
    },
    'Наборы букв': {
        1: [
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
        ],
        2: [
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
        ],
        3: [
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
    }
}


if __name__ == '__main__':
    for _, book in SETS_SELECTION.items():
        print(f'\n**** {_} ****')
        for column in book.values():
            for l_set in column:
                print(f'{l_set.front_name}: "{l_set.title}"')
