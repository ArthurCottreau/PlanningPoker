from misc.dict_operations import DictOperations
from misc.save_data import SaveData

def test():
    dict_avg_tests() # Teste la fonction qui calcule la moyenne des valeurs d'un dictionnaire
    dict_unanimous_tests() # Teste la fonction qui vérifie si toutes les valeurs dans le dictionnaire sont identiques ou pas
    save_data_tests() # Teste les fonctions set et get de la classe SaveData

def dict_avg_tests():
    dict_data = {'0':50, '1':0}
    assert (DictOperations.dict_avg(dict_data) == 25.0)

    dict_data = {'0':0, '1':0, '2':0, '3':200}
    assert (DictOperations.dict_avg(dict_data) == 50.0)

    dict_data = {'0':-50, '1':50}
    assert (DictOperations.dict_avg(dict_data) == 0.0)

    dict_data = {'0':5}
    assert (DictOperations.dict_avg(dict_data) == 5.0)

def dict_unanimous_tests():
    dict_data = {'0':50, '1':50}
    assert (DictOperations.is_dict_unanimous(dict_data) == True)

    dict_data = {'0':10, '1':50, '2':50}
    assert (DictOperations.is_dict_unanimous(dict_data) == False)

    dict_data = {'0':-5}
    assert (DictOperations.is_dict_unanimous(dict_data) == True)

def save_data_tests():
    mySD = SaveData()

    data = {'users': 'Bob'}
    mySD.file_data = data
    assert (mySD.get_element('users') == 'Bob')

    mySD.set_element('users','Jim')
    assert (mySD.get_element('users') == 'Jim')

    mySD.set_element('task','Faire la vaiselle')
    assert (mySD.get_element('task') == 'Faire la vaiselle')