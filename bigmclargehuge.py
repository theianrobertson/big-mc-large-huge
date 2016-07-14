import random

firsts = ['Beat',
    'Beef'
    'Big',
    'Blast',
    'Blitz',
    'Body',
    'Bold',
    'Bolt',
    'Brawn'
    'Brick',
    'Brunt',
    'Buck',
    'Buff',
    'Bulge',
    'Bulk',
    'Butch',
    'Cliff',
    'Crag',
    'Crud',
    'Crunch',
    'Dirk',
    'Dick',
    'Fist',
    'Flash',
    'Flex',
    'Flint',
    'Fridge',
    'Girth',
    'Gristle',
    'Hack',
    'Hunk',
    'Lump',
    'Peck',
    'Punch',
    'Punt',
    'Reef',
    'Rip',
    'Rock',
    'Rod',
    'Slab',
    'Slag',
    'Slam',
    'Slate',
    'Smash',
    'Smoke',
    'Squat',
    'Stump',
    'Thick',
    'Trunk',
    'Wedge',
    'Whip']

seconds = ['Vander', 'Mc']

thirds = ['Back',
    'Beef',
    'Big',
    'Blast',
    'Body',
    'Bone',
    'Brave',
    'Brawn',
    'Brunt',
    'Bulk',
    'Cheese',
    'Chest',
    'Chunk',
    'Core',
    'Crunch',
    'Dead',
    'Drink',
    'Face',
    'Fast',
    'Fist',
    'Fizzle',
    'Flank',
    'Flesh',
    'Force',
    'Groin',
    'Hair',
    'Hard',
    'Head',
    'Huge',
    'Jaw',
    'Kick',
    'Large',
    'Lift',
    'Lots',
    'Man',
    'Meal',
    'Meat',
    'Might',
    'Muscle',
    'Neck',
    'Pec',
    'Plank',
    'Pound',
    'Punch',
    'Rod',
    'Rock',
    'Run',
    'Rust',
    'Slab',
    'Slag',
    'Slam',
    'Speed',
    'Squat',
    'Steak',
    'Strike',
    'Strong',
    'Thick',
    'Thorn',
    'Thrust',
    'Vein']

def make_name():
    first = random.choice(firsts)
    if random.random() > 0.9:
        second = random.choice(seconds)
        if second == 'Vander':
            third1 = ''
        else:
            third1 = random.choice([t for t in thirds if t != first])
    else:
        second = ''
        third1 = random.choice([t for t in thirds if t != first])
    third2 = random.choice([t for t in thirds if t != first and t != third1])
    return first + ' ' + second + third1 + third2

if __name__ == '__main__':
    for i in range(10):
        print(make_name() + '!')