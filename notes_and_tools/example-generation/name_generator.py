from random import choice, choices
import names

def get_random_name(gender=None):
    emfname = choice(names.english_male_fname)
    effname = choice(names.english_female_fname)
    smfname = choice(names.spanish_male_fname)
    sffname = choice(names.spanish_female_fname)
    elname = choice(names.english_lname)
    slname = choice(names.spanish_lname)
    if gender == 'F':
        return(choices([(effname,elname),(sffname,slname)],weights=[75,25]))
    elif gender == 'M':
        return(choices([(emfname,elname),(smfname,slname)],weights=[75,25]))
    else:
        return(choices([(emfname,elname),(effname,elname),(smfname,slname),(sffname,slname)],weights=[37,37,13,13]))


#This only happens when this module is called directly:
if __name__ == "__main__":
    for i in range(10):
        print(get_random_name())
        print(get_random_name('M'))
        print(get_random_name('F'))

