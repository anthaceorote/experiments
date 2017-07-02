import requests
from itertools import product
from string import ascii_lowercase
import time
import csv
from tqdm import tqdm
import json
import pickle
import re

# Get Mashape Key
secrets_file = 'secret_keys.txt'
api_keys = dict()
with open(secrets_file, 'r') as f:
    api_keys = json.loads(f.read())

# Set header for request
headers = {
    "X-Mashape-Key": api_keys["X-Mashape-Key"],
    "Accept": "text/plain"
}


# Using Urban Dictionary API on Marketplace - https://market.mashape.com/community/urban-dictionary
def get_acronym(word):
    ''' Get definition for 'word' by using Urban Dictionary API on Mashape
        Returns a response for the request of type --
            "https://mashape-community-urban-dictionary.p.mashape.com/define?term={word}".format(word=word)
    '''
    url = "https://mashape-community-urban-dictionary.p.mashape.com/define?term={word}".format(word=word)
    resp = requests.get(url, headers=headers)
    return resp


def main():
    no_results = set()
    exact = []
    had_result = []
    words_missed = set()

    # 3-letter combinations of all lowercase letters
    words = product(ascii_lowercase, repeat=3)

    for i in tqdm(range(17576)):    # Using tqdm to track progress
        word = next(words)
        regex_to_match = r"[%s][\w'-]*[ .-]?[%s][\w'-]*[ .-]?[%s][\w'-]*" % (word[0], word[1], word[2])
        word = ''.join(word)
        # print(word)

        try:
            resp = get_acronym(word)
            resp.raise_for_status()     # In case of 404 (HTTPError) (Site is down or similar)
        except requests.exceptions.RequestException as e:   # Too many requests; sleep for a while
            print('Some error occured while processing  - {}'.format(word))
            print(e)
            words_missed.add(word)
            time.sleep(2000)
        except requests.exceptions.HTTPError as h:
            print('HTTP error while processing - {}'.format(word))
            print(h)
        else:
            result_type = resp.json()['result_type']
            if result_type == 'no_results':
                no_results.add(word)
            else:
                for i in range(len(resp.json()['list'])):   # Checking every possible definition for exact match
                    definition = resp.json()['list'][i]['definition']
                    definition = definition.lower().replace("\r\n", " ")
                    try:
                        possible_acronym = re.findall(re.compile(regex_to_match), definition)[0]
                        if possible_acronym == word:    # In case description contains the acronym first -- e.g. "ABS is short for Anti-lock Breaking System"
                            possible_acronym = re.findall(re.compile(regex_to_match), definition)[1]
                    except IndexError:
                        words_missed.add(word)
                    else:
                        possible_acronym = possible_acronym.title()
                        if len(possible_acronym) <= 5:
                            had_result.append((word, possible_acronym, definition))
                        else:
                            exact.append((word, possible_acronym, definition))
                        if word in words_missed:
                            words_missed.remove(word)
                        break

        time.sleep(1)                   # Sleep for a second after each request; can be avoided if ideal request acceptance rate is matched
        if i % 900 == 0 and i > 0:      # Rate limit mentioned on API page is 1000; but sleeping after 900 just to be safe
            time.sleep(60)

    no_results = sorted(no_results)
    words_missed = sorted(words_missed)

    # Pickling results just for safety
    with open('pickle_exact.p', 'wb') as pickle_out:
        pickle.dump(exact, pickle_out)

    with open('pickle_no_res.p', 'wb') as pickle_no_res:
        pickle.dump(no_results, pickle_no_res)

    with open('pickle_poss_res.p', 'wb') as pickle_poss_res:
        pickle.dump(had_result, pickle_poss_res)

    # Stats
    print("-" * 100)
    print("Total Possible Permutations (with repetition allowed): {}".format(17576))
    print("Total Acronyms Found: {}".format(len(exact) + len(had_result)))
    print("Words missed due to some error: {}".format(len(words_missed)))
    print("Words without acronyms (Yet): {}".format(len(no_results)))

    print("-" * 100)

    with open('existing_acronyms.csv', 'w', newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(exact)

    with open('had_result.csv', 'w', newline="", encoding="utf-8") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(had_result)

    with open('no_results.txt', 'w') as f:
        f.write("\n".join(no_results))

    with open('missed.txt', 'w') as f:
        f.write("\n".join(words_missed))


if __name__ == '__main__':
    main()
