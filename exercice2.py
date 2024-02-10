class Curve :
    
    def __init__(self, start, stop, nbr_points=5432):
        self.start = start
        self.stop = stop
        self.nbr_points = nbr_points
        
    def __fonction(self, x):
        '''
            name - fonction
            type method: private
            arg: real
            return: real
        '''
        return x**(5)
    
    def courbe(self):
        '''
            name - courbe
            type method: public
            arg: -
            return: curve
        '''
        import numpy as np
        import matplotlib.pyplot as plt
        x = np.linspace(self.start, self.stop, self.nbr_points)
        y = self.__fonction(x)
        plt.plot(x, y)
        return plt.show()
    
    
    
