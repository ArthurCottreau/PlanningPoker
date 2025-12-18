class DictOperations:
    """
    @author COTTREAU Arthur
    @class DictOperations
    @brief Classe dédiée aux opérations dictionnaire nécessaire pour le Planning Poker
    """
    @staticmethod
    def dict_avg(dict):
        """
        @brief Fonction qui calcule la moyenne des valeurs du dictionnaire
        @param dict: Dictionnaire contenant les valeurs
        @return La moyenne des valeurs du dictionnaire
        """
        sum_result = 0
        for value in dict.values():
            sum_result += int(value)
        
        return sum_result / len(dict)

    @staticmethod
    def is_dict_unanimous(dict):
        """
        @brief Fonction qui vérifie si toutes les valeurs dans le dictionnaire sont identiques ou pas
        @param dict: Dictionnaire contenant les valeurs
        @return True ou False dépendant de si toutes les valeurs dans le dictionnaire sont identiques ou pas
        """
        return len(set(dict.values())) == 1
