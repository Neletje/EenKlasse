'''
Created on 31-jul.-2013

@author: Ellen
'''

class eenKlasse:
    links='L'
    rechts='R'
    mid=490
    def __init__(self):
        self.dic = {self.links : -1, self.rechts:1}
        self.huidigeSnelheid=self.mid
        self.huidigeRichting=self.links
        
        
    #eenvoudig aanpassen    
    def draailinks(self, nieuweSnelheid=None):
        if nieuweSnelheid==None:
            self.pasAan(self.mid + (self.huidigeSnelheid*self.dic[self.huidigeRichting] - self.mid * self.dic[self.huidigeRichting]  )   , self.rechts)
        else:
            self.pasAan(self.mid+( nieuweSnelheid* self.dic[self.links]), self.links)
 
    def draairechts(self, nieuweSnelheid=None):
        if nieuweSnelheid==None:
            self.pasAan(self.mid + (self.huidigeSnelheid*self.dic[self.huidigeRichting] - self.mid * self.dic[self.huidigeRichting]  )   , self.rechts)
        else:
            self.pasAan(self.mid+( nieuweSnelheid* self.dic[self.rechts]) , self.rechts)
 
 
 
    def versnel(self, versnelling=None):
        if versnelling == None :
            versnelling = 10
        self.pasAan( self.huidigeSnelheid   +   (versnelling * self.dic[self.huidigeRichting])  )
        
    def verTraag(self, vertraging=None):
        if vertraging == None:
            vertraging = 10
        self.pasAan( self.huidigeSnelheid    -  (vertraging * self.dic[self.huidigeRichting])   )

        
    
    
    def stop(self):
        self.pasAan(self.mid)
        
    def nieuweSnelheid(self, snelheid):
        self.pasAan(self.mid+snelheid)
        
        
    #specifiek aanpassen met juiste waarde   
    def pasAan(self, nieuweSnelheid=None, richting=None):
        #controleer snelheid
        if nieuweSnelheid == None :
            nieuweSnelheid = self.huidigeSnelheid
        elif not isinstance( nieuweSnelheid, int ) or nieuweSnelheid <0:
            raise ValueError('nieuweSnelheid moet een possitieve int zijn!')
        print('snelheid is ok')
        #controleer richting
        if richting == None:
            richting = self.huidigeRichting
        elif richting not in self.dic:
            raise ValueError('Richting niet gedefineerd, moet zijn ' + self.__maakzin())
        print('richting is ok')
        
        #houd bij
        self.huidigeRichting=richting
        self.huidigeSnelheid=nieuweSnelheid
        
        #verander
        self.__verander( nieuweSnelheid )
        
        
        
    #getters
    def getRichting(self):
        return self.huidigeRichting
    
    def getSnelheid(self):
        return ( self.huidigeSnelheid + self.mid*self.dic[self.huidigeRichting] ) *self.dic[self.huidigeRichting]
        
        
    #private methods    
    def __verander(self, snelheid):
        print (snelheid)
        #hier komt dat regeltje om dat ding zijn snelheid te veranderen :)

    def __maakzin(self):
        zin = ''
        for k, v in self.dic.items():
            zin = zin + str(k) + (' / ')
        
        return zin[:-2]

                