class card:
    def __init__(self, rank, suit):
        self.__suit = suit
        self.__rank = rank
    def get_rank(self):
        return self.__rank
    def set_rank(self, rank):
        self.__rank = rank
    def get_suit(self):
        return self.__suit
    def set_suit(self, suit) :
        self.__suit = suit

    def __str__(self):
        return f"""
        rank: {self.__rank}
        suit: {self.__suit}
        """





# __rank: int(1 - 13)@ __suit: str('club', 'spade', 'hearts', 'diamonds') @get_suit('self'):str @get_rank('self'):int @__str__('self'):str

