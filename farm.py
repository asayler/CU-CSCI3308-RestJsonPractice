import shelve

DATAFILE = "server_data"
ANIMALS = 'animals'
VALID_TYPES = ['horses', 'pigs', 'sheep', 'cows', 'humans']

def setup():
    shv = shelve.open(DATAFILE)
    if ANIMALS not in shv:
        shv[ANIMALS] = {}
    shv.close()

def list_animal_types():
    shv = shelve.open(DATAFILE)
    anm = shv[ANIMALS]
    shv.close()
    return {'types': anm.keys()}

def create_animal_type(animal):
    shv = shelve.open(DATAFILE)
    anm = shv[ANIMALS]
    anm[animal] = {}
    shv[ANIMALS] = anm
    shv.close()
    return {'types': anm.keys()}

def remove_animal_type(animal):
    shv = shelve.open(DATAFILE)
    anm = shv[ANIMALS]
    if animal in anm:
        del(anm[animal])
    shv[ANIMALS] = anm
    shv.close()
    return {'types': anm.keys()}

def list_animals(animal):
    shv = shelve.open(DATAFILE)
    anm = shv[ANIMALS]
    shv.close()
    if animal in anm:
        nms = anm[animal].keys()
    else:
        nms = None
    return {animal: nms}

def create_animal(animal, name):
    shv = shelve.open(DATAFILE)
    anm = shv[ANIMALS]
    if animal in anm:
        anm[animal][name] = {}
        nms = anm[animal].keys()
    else:
        nms = None
    shv[ANIMALS] = anm
    shv.close()
    return {animal: nms}

def remove_animal(animal, name):
    shv = shelve.open(DATAFILE)
    anm = shv[ANIMALS]
    if animal in anm:
        del(anm[animal][name])
        nms = anm[animal].keys()
    else:
        nms = None
    shv[ANIMALS] = anm
    shv.close()
    return {animal: nms}
