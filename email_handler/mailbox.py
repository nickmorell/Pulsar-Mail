class Mailbox:

    def __init__(self, name, child, no_select):
        self.__name = name
        self.__child = child
        self.__no_select = no_select

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return self.__name

    def get_child(self):
        return self.__child

    def set_child(self, child):
        self.__child = child
        return self.__child

    def get_no_select(self):
        return self.__no_select

    def set_no_select(self, no_select):
        self.__no_select = no_select
        return no_select
