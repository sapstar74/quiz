import json
import os
import random

COUNTRIES_JSON = '../world_flags_project/data/countries.json'
FLAGS_DIR = '../world_flags_project/data/flags/'
OUTPUT_FILE = 'topics/zaszlok_all_questions.py'

# Load country codes and names
def load_countries():
    with open(COUNTRIES_JSON, encoding='utf-8') as f:
        return json.load(f)

def get_flag_file(code, country):
    # Try different filename patterns
    patterns = [
        f"{code}_{country.replace(' ', '_').replace('(', '').replace(')', '').replace('.', '').replace(',', '').replace('-', '_')}.png",
        f"{code}_{country.replace(' ', '_')}.png",
        f"{code}.png"
    ]
    for pattern in patterns:
        if os.path.exists(os.path.join(FLAGS_DIR, pattern)):
            return os.path.join(FLAGS_DIR, pattern)
    return None

def main():
    countries = load_countries()
    # UN member states ISO codes (alpha-2) - 193 countries
    un_member_iso = [
        'af','al','dz','ad','ao','ag','ar','am','au','at','az','bs','bh','bd','bb','by','be','bz','bj','bt','bo','ba','bw','br','bn','bg','bf','bi','cv','kh','cm','ca','cf','td','cl','cn','co','km','cd','cg','cr','ci','hr','cu','cy','cz','dk','dj','dm','do','ec','eg','sv','gq','er','ee','sz','et','fj','fi','fr','ga','gm','ge','de','gh','gr','gd','gt','gn','gw','gy','ht','hn','hu','is','in','id','ir','iq','ie','il','it','jm','jp','jo','kz','ke','ki','kr','kw','kg','la','lv','lb','ls','lr','ly','li','lt','lu','mg','mw','my','mv','ml','mt','mh','mr','mu','mx','fm','md','mc','mn','me','ma','mz','mm','na','nr','np','nl','nz','ni','ne','ng','mk','no','om','pk','pw','ps','pa','pg','py','pe','ph','pl','pt','qa','ro','ru','rw','kn','lc','vc','ws','sm','st','sa','sn','rs','sc','sl','sg','sk','si','sb','so','za','ss','es','lk','sd','sr','se','ch','sy','tw','tj','tz','th','tl','tg','to','tt','tn','tr','tm','tv','ug','ua','ae','gb','us','uy','uz','vu','ve','vn','ye','zm','zw'
    ]
    all_codes = [code for code in un_member_iso if code in countries]
    questions = []
    for code in all_codes:
        country = countries[code]
        flag_file = get_flag_file(code, country)
        if not flag_file:
            print(f"Warning: No flag file found for {country} ({code})")
            continue
        # logo_path should be relative to quiz app (assume ../world_flags_project/data/flags/...)
        rel_flag_file = os.path.relpath(flag_file, start=os.path.dirname(OUTPUT_FILE))
        # Pick 3 random other countries
        others = [countries[c] for c in all_codes if c != code]
        options = random.sample(others, 3) + [country]
        random.shuffle(options)
        correct = options.index(country)
        questions.append({
            'question': 'Ez a zászló melyik országhoz tartozik?',
            'logo_path': rel_flag_file,
            'options': options,
            'correct': correct,
            'explanation': f"Ez {country} zászlaja."
        })
    # Write to output file
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write('# AUTO-GENERATED: Minden ENSZ-tagország zászlója\n')
        f.write('ZASZLOK_QUESTIONS_ALL = [\n')
        for q in questions:
            f.write('    ' + repr(q) + ',\n')
        f.write(']\n')
    print(f"Generated {len(questions)} questions.")
    print(f"Output file: {OUTPUT_FILE}")

if __name__ == "__main__":
    main() 