class Card:

    def __init__(self, value, suit):
        """Setting the global parameters"""
        if type(suit)!=int:
            raise TypeError('Argument suit must be int')
        if type(value)!=int:
            raise TypeError('Argument value must be int')
        if value<1 or value>13:
            raise ValueError('Argument value must be a value between 1-13')
        if suit<1 or suit>4:
            raise ValueError('Argument suit must be a value between 1-4')
        self.value=value
        self.suit=suit


    def __gt__(self, other):
        """ """
        if self.value==1 and other.value!=1:
            return True
        if self.value!=1 and other.value==1:
            return False
        if self.value == other.value and self.suit>other.suit:
            return True
        if type(other)!=Card:
            raise TypeError('Can compare only between cards')
        if self.value > other.value:
            return True
        else:
            return False

    def __eq__(self, other):
        if self.value == other.value and self.suit == other.suit:
            return True
        return False

    def __repr__(self):
        dic={1:'Ace', 11:'Jack', 12:'Queen', 13:'King'}
        dic2= {1:'Diamond', 2:'Spade', 3:'Heart', 4:'Club'}
        for i in dic:
            if i==self.value:
                v=dic[i]
                break
        else:
            v=self.value
        for j in dic2:
            s=dic2[self.suit]
        return f'{v}:{s}'


