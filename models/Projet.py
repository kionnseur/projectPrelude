class Projet:

    def __init__(self, folder, type, nom):
        self.__folder = folder
        self.__type = type
        self.__nom= nom

    def get_position(self):
        return self.__folder

    def get_type(self):
        return self.__type

    def get_nom(self):
        return self.__nom

    def __str__(self) -> str:
        return "Projet "+self.__type+" du nom de "+self.__nom+" dans "+self.__folder

