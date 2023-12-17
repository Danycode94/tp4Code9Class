""" Klass AtribiMachin ki gen tout atribi pou yon mak machin. """

from machin import Machin

class AtribiMachin(Machin):
    vites = 0
    koule = "nwa"
    model = "Toyota"
    pwopriyete = "Dany BADIO"
    gaz = 3500
    _tente = False
    ane = "2012"
    _pri = 170.000
    
    def __init__(self, vites, koule, model, pwopriyete, gaz, _tente, ane, _pri):
        self.vites = vites
        self.koule = koule
        self.model = model
        self.pwopriyete = pwopriyete
        self.gaz = gaz
        self._tente = _tente
        self.ane = ane
        self._pri = _pri
        
    def __repr__(self) -> str:
        return "Ou nan fichye atribi an !"
        
    def getTente(self):
        return self._tente

    def setTente(self, _tente):
        print("Sonje ou dwe gen papye legal DGI poutèt ou tente machin nan.")
        self._tente = _tente
    
    def delTente(self):
        del self._tente
    
    at_tente = property(getTente,setTente,delTente,doc="Atribi protected _tente")
