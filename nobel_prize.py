def load_nobel_prizes(filename='prize.json'):
    with open(filename) as f:
        return json.load(f)  # load in the json file


def main(year, category):
    data = load_nobel_prizes()
    prizes = data['prizes']  #  Enter the first array labeled prizes to see the category and year

    for prize in prizes:  # repeatively check to see if the data matches, if not move-on
        if 'laureates' not in prize:
            continue
        if category and prize['category'].lower() != category.lower():
            continue
        if year and prize['year'] != year:
            continue

        print(f"{prize['year']} Nobel Prize in {prize['category'].title()}")  # when a match is found print the information
        for laureate in prize['laureates']:
            firstname = laureate['firstname']
            surname = laureate.get('surname', '')
            print(f"{firstname} {surname}: {laureate['motivation']}")
