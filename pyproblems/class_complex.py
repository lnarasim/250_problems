'''This class contains a custom made format for printing complex numbers'''
class ComplexCustom(complex):
    '''
    This class contains function for
    a custom made printing format for complex numbers
    '''
    def __format__(self, fmt):
        '''This function creates a custom made format for printing complex numbers'''
        cfmt = "({:" + fmt + "}{:+" + fmt + "}j)"
        return cfmt.format(self.real, self.imag)
