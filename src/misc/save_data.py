import json

from misc.singleton import singleton

@singleton
class SaveData:
    """
    @author COTTREAU Arthur
    @class SaveData
    @brief Classe dédiée à la gestion des sauvegardes de données JSON
    """
    def __init__(self):
        """
        @brief Constructeur de la classe
        """
        self.file_data = ""

    def reset(self):
        """
        @brief Suppression des données en mémoire
        """
        self.file_data = {}

    def is_json(self, myjson):
        """
        @brief Fonction qui vérifie si le fichier est un JSON valide
        @param myjson: Contenu du fichier à vérifier
        @return True ou False dépendant de si le contenu du fichier correspond à celui d'un JSON ou pas
        """
        try:
            json.loads(myjson)
        except ValueError as e:
            print("Error! This file is not structured like a JSON!")
            return False
        return True

    def load_json(self, path):
        """
        @brief Fonction qui charge le fichier JSON
        @param path: Chemin du fichier à charger
        """
        if path:
            try:
                with open(path) as f:
                    file_content = f.read()

                    if self.is_json(file_content):
                        self.file_data = json.loads(file_content)                   
            except Exception as e:
                print("An Error occured while trying to read the JSON!",e)

    def save_json(self, path):
        """
        @brief Fonction qui sauvegarde le fichier JSON
        @param path: Chemin dans lequel sauvegarder le JSON
        """
        if path:
            try:
                with open(path + ".json","w",encoding="utf-8") as f:
                    save_data = json.dumps(self.file_data)
                    f.write(save_data)
            except Exception as e:
                print("An Error occured while trying to save the JSON!",e)

    def set_element(self, element, data):
        """
        @brief Change un élément du JSON
        @param element: Clef JSON à laquelle on assigne une valeur
        @param data: Valeur qu'on souhaite assigner à la clef JSON
        """
        self.file_data[element] = data

    def get_element(self, element):
        """
        @brief Récupère un élément JSON
        @param element: Clef JSON qui nous permet de récupérer une valeur
        @return Retourne la valeur de la Clef
        """
        if element in self.file_data:
            return self.file_data[element]
        else:
            print("Error! This JSON element doesn't exist!")
            return ""