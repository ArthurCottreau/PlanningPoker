from misc.save_data import SaveData

def test():
    save_data_tests()

def save_data_tests():
    mySD = SaveData()

    data = {'users': 'Bob'}
    mySD.file_data = data
    assert (mySD.get_element('users') == 'Bob')

    mySD.set_element('users','Jim')
    assert (mySD.get_element('users') == 'Jim')

    mySD.set_element('task','Faire la vaiselle')
    assert (mySD.get_element('task') == 'Faire la vaiselle')