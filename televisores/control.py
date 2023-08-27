class Control:
    def __init__(self):
        self._tv = None

    def turnOn(self):
        self._tv.estado = True
    def turnOff(self):
        self._tv.estado = False

    def canalUp(self):
        if (self._tv.estado == True) and (self._tv.canal < 120):
            self._tv.canal += 1
    def canalDown(self):
        if (self._tv.estado == True) and (self._tv.canal > 1):
            self._tv.canal -= 1

    def volumenUp(self):
        if (self._tv.estado == True) and (self._tv.volumen < 7):
            self._tv.volumen += 1
    def volumenDown(self):
        if (self._tv.estado == True) and (self._tv.volumen > 0):
            self._tv.volumen -= 1

    def setCanal(self, canal):
        if (self._tv.estado == True) and (canal >= 1 and canal <= 120):
            self._tv.canal = canal

    def setVolumen(self, volumen):
        if (self._tv.estado == True) and (volumen >= 0 and volumen <= 7):
            self._tv.volumen = volumen

    def enlazar(self, tv):
        self._tv = tv
        tv.control = self

    def setTv(self, tv):
        self._tv = tv
    def getTv(self):
        return self._tv
