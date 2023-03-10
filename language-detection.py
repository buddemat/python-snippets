from langdetect import detect_langs
from langdetect import DetectorFactory

iso_codes = {
        'af': 'Afrikaans',
        'ar': 'Arabic',
        'bg': 'Bulgarian',
        'bn': 'Bengali',
        'ca': 'Catalan',
        'cs': 'Czech',
        'cy': 'Welsh',
        'da': 'Danish',
        'de': 'German',
        'el': 'Greek (modern)',
        'en': 'English',
        'es': 'Spanish',
        'et': 'Estonian',
        'fa': 'Persian / Farsi',
        'fi': 'Finnish',
        'fr': 'French',
        'gu': 'Gujarati',
        'he': 'Hebrew',
        'hi': 'Hindi',
        'hr': 'Croatian',
        'hu': 'Hungarian',
        'id': 'Indonesian',
        'it': 'Italian',
        'ja': 'Japanese',
        'kn': 'Kannada',# no typo ;)
        'ko': 'Korean',
        'lt': 'Lithuanian',
        'lv': 'Latvian',
        'mk': 'Macedonian',
        'ml': 'Malayalam',
        'mr': 'Marathi',
        'ne': 'Nepali',
        'nl': 'Dutch',
        'no': 'Norwegian',
        'pa': 'Punjabi',
        'pl': 'Polish',
        'pt': 'Portuguese',
        'ro': 'Romanian / Moldavian',
        'ru': 'Russian',
        'sk': 'Slovak',
        'sl': 'Slovenian',
        'so': 'Somali',
        'sq': 'Amharic',
        'sv': 'Swedish',
        'sw': 'Swahili',
        'ta': 'Tamil',
        'te': 'Telugu',
        'th': 'Thai',
        'tl': 'Tagalog',
        'tr': 'Turkish',
        'uk': 'Ukrainian',
        'ur': 'Urdu',
        'vi': 'Vietnamese',
        'zh-cn': 'Chinese (China)',
        'zh-tw': 'Chinese (Taiwan)'
        }

DetectorFactory.seed = 42

sentences = [
    "Ik glaub ik spinne",
    "Ich glaub ich spinne",
    "Non, je ne regrette rien",
    "Non, rien de rien. Non, je ne regrette rien",
    "Non, rien de rien.  Non, je ne regrette rien. Ni le bien qu'on m'a fait. Ni le mal. Tout ça m'est bien égal.",
    "Wo bu shuo zhong wen, zhe shuo ying wen hua de wen",
    "我不说中文，说英文",
    "Blankenberghe, blankenberghe wondermooie stad, ik wou dat ik in m'n achtertuin zo'n Blankenberge had.",
    "مدت زمان زيادي است که شما را نديده ام",
    "moddate ziadi ast ke shoma ra nadideh am"
]

for s in sentences:
    result = detect_langs(s)
    print(f'\nInput: "{s}"')
    for r in result:
        print(f'    Detected: {r.lang:5} {iso_codes.get(r.lang):20} (confidence: {r.prob})')

