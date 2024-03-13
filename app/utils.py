

def trans_list_to_str(list_of_spell):
    '''['o', 'wo'] -> o, wo'''
    return str(list_of_spell).replace("[", "").replace("]", "").replace("'", "").replace(" ", "")


def trans_str_to_list(str_of_spell):
    ''' o, wo -> ['o', 'wo'] '''
    return str_of_spell.split(',') if ',' in str_of_spell else [str_of_spell]


def clean_the_input_data(data):
    ''' 
        "ka  " -> "ka"
        "KA" -> "ka"
    '''
    return data.replace(" ", "").lower()

