# simpel tf-idf implementation:

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from vega_datasets import data
import stopwordsiso as stopwords

books = pd.read_json("output.json")
all_descriptions = books['description'].to_list()

language_codes_list = ['eng', '', 'en-US', 'en-GB', 'spa', 'ger', 'ita', 'fre', 'por', 'ind', 'cze', 'en-CA', 'nl', 'pol', 'tur', 'jpn', 'swe', 'bul', 'fin', 'gre', 'rus', 'dan', 'per', 'rum', 'hun', 'srp', 'slo', 'ara', 'scr', 'tha', 'est', 'nor', 'lav', 'vie', 'lit', 'heb', 'zho', 'ben', 'kor', 'kat', 'nob', 'cat', 'ukr', 'en', 'msa', 'slv', 'pes', 'fil', 'isl', 'nno', 'hin', '--', 'pt-BR', 'mul', 'mal', 'tgl', 'es-MX', 'bos', 'glg', 'nld', 'ang', 'hye', 'mkd', 'che', 'abk', 'tam', 'ale', 'enm', 'gle', 'ast', 'ota', 'urd', 'mon', 'frs', 'grc', 'epo', 'bug', 'sqi', 'div', 'jav', 'guj', 'aus', 'ira', 'vls', 'lat', 'bel', 'aze', 'gla', 'aar']

# Desired language codes
desired_codes = [
    'af', 'ar', 'bg', 'bn', 'br', 'ca', 'cs', 'da', 'de', 'el', 'en', 'eo', 
    'es', 'et', 'eu', 'fa', 'fi', 'fr', 'ga', 'gl', 'gu', 'ha', 'he', 'hi', 
    'hr', 'hu', 'hy', 'id', 'it', 'ja', 'ko', 'ku', 'la', 'lt', 'lv', 'mr', 
    'ms', 'nl', 'no', 'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'so', 'st', 'sv', 
    'sw', 'th', 'tl', 'tr', 'uk', 'ur', 'vi', 'yo', 'zh', 'zu'
]

# Mapping dictionary
mapping = {
    'eng': 'en', 'en-US': 'en', 'en-GB': 'en', 'spa': 'es', 'ger': 'de', 'ita': 'it', 
    'fre': 'fr', 'por': 'pt', 'ind': 'id', 'cze': 'cs', 'en-CA': 'en', 'nl': 'nl', 
    'pol': 'pl', 'tur': 'tr', 'jpn': 'ja', 'swe': 'sv', 'bul': 'bg', 'fin': 'fi', 
    'gre': 'el', 'rus': 'ru', 'dan': 'da', 'per': 'fa', 'rum': 'ro', 'hun': 'hu', 
    'srp': 'sr', 'slo': 'sl', 'ara': 'ar', 'scr': 'hr', 'tha': 'th', 'est': 'et', 
    'nor': 'no', 'lav': 'lv', 'vie': 'vi', 'lit': 'lt', 'heb': 'he', 'zho': 'zh', 
    'ben': 'bn', 'kor': 'ko', 'kat': 'ka', 'nob': 'no', 'cat': 'ca', 'ukr': 'uk', 
    'msa': 'ms', 'slv': 'sl', 'pes': 'fa', 'fil': 'tl', 'isl': 'is', 'nno': 'no', 
    'hin': 'hi', 'pt-BR': 'pt', 'mul': '', 'mal': 'ml', 'tgl': 'tl', 'es-MX': 'es', 
    'bos': 'bs', 'glg': 'gl', 'nld': 'nl', 'ang': 'en', 'hye': 'hy', 'mkd': 'mk', 
    'che': 'ce', 'abk': 'ab', 'tam': 'ta', 'ale': 'ale', 'enm': 'enm', 'gle': 'ga', 
    'ast': 'ast', 'ota': 'ota', 'urd': 'ur', 'mon': 'mn', 'frs': 'fy', 'grc': 'grc', 
    'epo': 'eo', 'bug': 'bug', 'sqi': 'sq', 'div': 'dv', 'jav': 'jv', 'guj': 'gu', 
    'aus': 'aus', 'ira': 'fa', 'vls': 'vls', 'lat': 'la', 'bel': 'be', 'aze': 'az', 
    'gla': 'gd', 'aar': 'aa'
}

# Filter out any empty strings or unwanted codes from the mapping
filtered_language_codes_list = [mapping[code] for code in language_codes_list if code in mapping and mapping[code]]

# Ensure unique values
filtered_language_codes_list = list(set(filtered_language_codes_list))

language_list = '[{}]'.format(', '.join(f'"{code}"' for code in filtered_language_codes_list))
print(language_list)

N = 1000
textRaw = all_descriptions[:N]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(textRaw)
allWords = vectorizer.get_feature_names_out()
dense = X.todense()
XList = dense.tolist()
df = pd.DataFrame(XList, columns=allWords)
dictionary = df.T.sum(axis=1)

pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.expand_frame_repr', False)  # Prevent line-wrapping

sorted_dictionary = dictionary.sort_values(ascending=False)
stopwords_set = set(stopwords.stopwords(["en"]))
#stopwords_set = set(stopwords.stopwords(language_list))

filtered_dictionary = sorted_dictionary[~sorted_dictionary.index.isin(stopwords_set)]

with open("file_words.txt", "w") as output:
     output.write(filtered_dictionary)
     
print(filtered_dictionary[0:20])