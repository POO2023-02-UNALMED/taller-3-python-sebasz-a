class TV:
    _numTV = 0
    def __init__(self, marca, estado):
        self._marca = marca
        self.estado = estado
        self.canal = 1
        self._precio = 500
        self.volumen = 1
        self.control = None

    def setMarca(self, marca):
        self._marca = marca
    def getMarca(self):
        return self._marca
    
    def setCanal(self, canal):
        if (self.estado == True) and (canal >= 1 and canal <= 120):
            self.canal = canal
    def getCanal(self):
        return self.canal
    
    def setPrecio(self, precio):
        self._precio = precio
    def getPrecio(self):
        return self._precio
    
    def setVolumen(self, volumen):
        if (self.estado == True) and (volumen >= 0 and volumen <= 7):
            self.volumen = volumen
    def getVolumen(self):
        return self.volumen
    
    def setControl(self, control):
        self.control = control
    def getControl(self):
        return self.control
    
    @classmethod
    def setNumTV(cls, numTv):
        cls._numTV = numTv
    @classmethod
    def getNumTV(cls):
        return cls._numTV
    
    def turnOn(self):
        self.estado = True
    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if (self.estado == True) and (self.canal < 120):
            self.canal += 1
    def canalDown(self):
        if (self.estado == True) and (self.canal > 1):
            self.canal -= 1

    def volumenUp(self):
        if (self.estado == True) and (self.volumen < 7):
            self.volumen += 1
    def volumenDown(self):
        if (self.estado == True) and (self.volumen > 0):
            self.volumen -= 1
