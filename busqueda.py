from abc import ABC,abstractmethod

## Esta es una clase para el ambiente de un problema
class ambiente:
    def __init__(self,grafo,hs=None):
        self.grafo=grafo
        self.hs=hs
    def getGrafo(self):
        return self.grafo
    def getHs(self):
        return self.hs
    def setHs(self,hs):
        self.hs=hs

## Una clase muy general y abstracta para una tecnica de busqUeda
class busqueda(ABC):
    def __init__(self,proble):
        self.ini=None
        self.meta=None
        self.Abiertos=None
        self.Cerrados=None
        self.Soln=[]
        self.proble=proble
        super().__init__()
    def getIni(self):
        return self.ini
    def getMeta(self):
        return self.meta
    def setIni(self,ini):
        self.ini=ini
    def setMeta(self,meta):
        self.meta=meta
    def getProble(self):
        return self.proble
    def getHijos(self,nodo):
        resp=self.proble.getGrafo()[nodo]
        return resp
    @abstractmethod
    def siguiente(self):
        pass
    @abstractmethod
    def agregar(self,nodos):
        pass
    @abstractmethod
    def buscar(self):
        pass
    @abstractmethod
    def getSoln(self):
        pass

## Una clase de busqueda ciega
class ciega(busqueda):
    def __init__(self,proble):
        super().__init__(proble)
        self.Abiertos=[]
        self.Cerrados=[]
    @abstractmethod
    def siguiente(self):
        pass
    def agregar(self,nodos):
        for nodo in nodos:
            if nodo not in self.Abiertos and nodo not in self.Cerrados:
                self.Abiertos.append(nodo)
    def getSoln(self):
        return self.Soln
    def buscar(self):
        self.Abiertos.append(self.ini)
        listo=False
        while not listo:
            actual=self.siguiente()
            if actual==self.meta:
                listo=True
            else:
                hijos=self.getHijos(actual)
                self.agregar(hijos)
            self.Cerrados.append(actual)
        self.Soln=self.Cerrados

## Esta es una clase para una busqueda primero en amplitud
class amplitud(ciega):
    def __init__(self,proble):
        super().__init__(proble)
    def siguiente(self):
        resp=self.Abiertos[0]
        del self.Abiertos[0]
        return resp

## Esta es una clase para una busqueda primero en profundidad
class profund(ciega):
    def __init__(self,proble):
        super().__init__(proble)
    def siguiente(self):
        resp=self.Abiertos[-1]
        del self.Abiertos[-1]
        return resp

## Una clase para busquedas informadas
class informada(busqueda):
    def __init__(self,proble):
        super().__init__(proble)
        self.Abiertos={}
        self.Cerrados={}
    @abstractmethod
    def siguiente(self):
        pass
    @abstractmethod
    def agregar(self,nodos,padre):
        pass
    def getSoln(self):
        return self.Soln
    @abstractmethod
    def buscar(self):
        pass
    def formaSoln(self):
        resp=[]
        actual=self.meta
        listo=False
        while not listo:
            if actual==self.ini:
                listo=True
                resp.append(actual)
            else:
                resp.append(actual)
                actual=self.Cerrados[actual][1]
        return resp

## Una clase para la busqueda preferente por lo mejor
class prefmej(informada):
    def __init__(self,proble):
        super().__init__(proble)
    def siguiente(self):
        gmejor=100
        for nodo in self.Abiertos:
            if gmejor>self.Abiertos[nodo][0]:
                mejor=nodo
        gmejor=self.Abiertos[mejor][0]
        pmejor=self.Abiertos[mejor][1]
        del self.Abiertos[nodo]
        return mejor,gmejor,pmejor
    def agregar(self,nodos,padre,gpadre):
        for nodo in nodos:
            gnueva=gpadre+nodos[nodo]
            if nodo not in self.Cerrados:
                if nodo in self.Abiertos:
                    if gnueva<=self.Abiertos[nodo][0]:
                        self.Abiertos[nodo]=[gnueva,padre]
                else:
                    self.Abiertos[nodo]=[gnueva,padre]
    def buscar(self):
        self.Abiertos[self.ini]=[0,self.ini]
        listo=False
        while not listo:
            actual,gactual,pactual=self.siguiente()
            if actual==self.meta:
                listo=True
                self.Cerrados[actual]=[gactual,pactual]
            else:
                hijos=self.getHijos(actual)
                self.agregar(hijos,actual,gactual)
                self.Cerrados[actual]=[gactual,pactual]
        self.Soln=self.formaSoln()

## Esto implementa una busqueda en ascenso de colina
class avara(informada):
    def __init__(self,proble):
        super().__init__(proble)
    def siguiente(self):
        hmejor=1000
        for nodo in self.Abiertos:
            if self.Abiertos[nodo][0]<=hmejor:
                mejor=nodo
                hmejor=self.Abiertos[nodo][0]
        hmejor=self.Abiertos[mejor][0]
        pmejor=self.Abiertos[mejor][1]
        del self.Abiertos[mejor]
        return mejor,hmejor,pmejor
    def agregar(self,nodos,padre):
        for nodo in nodos:
            if nodo not in self.Cerrados and nodo not in self.Abiertos:
                self.Abiertos[nodo]=[self.proble.getHs()[nodo][self.meta],padre]
    def buscar(self):
        self.Abiertos[self.ini]=[self.proble.getHs()[self.ini][self.meta],self.ini]
        listo=False
        while not listo:
            actual,hactual,padre=self.siguiente()
            if actual==self.meta:
                listo=True
            else:
                hijos=self.getHijos(actual)
                self.agregar(hijos,actual)
            self.Cerrados[actual]=[hactual,padre]
        self.Soln=self.formaSoln()
        
## Una clase para busqeda a-estrella
class astar(informada):
    def __init__(self,proble):
        super().__init__(proble)
    def siguiente(self):
        fmejor=1000
        for nodo in self.Abiertos:
            fnodo=self.Abiertos[nodo][0]+self.proble.getHs()[nodo][self.meta]
            if fnodo<=fmejor:
                mejor=nodo
                fmejor=fnodo
        fmejor=self.Abiertos[mejor][0]
        pmejor=self.Abiertos[mejor][1]
        del self.Abiertos[mejor]
        return mejor,fmejor,pmejor
    def agregar(self,nodos,padre,gpadre):
        for nodo in nodos:
            gnodo=nodos[nodo]+gpadre
            fnodo=gnodo+self.proble.getHs()[nodo][self.meta]
            if nodo not in self.Cerrados:
                if nodo in self.Abiertos:
                    if fnodo<=self.Abiertos[nodo][0]:
                        self.Abiertos[nodo]=[gnodo,padre]
                else:
                    self.Abiertos[nodo]=[gnodo,padre]
    def buscar(self):
        self.Abiertos[self.ini]=[0+self.proble.getHs()[self.ini][self.meta],self.ini]
        listo=False
        while not listo:
            actual,gactual,pactual=self.siguiente()
            if actual==self.meta:
                listo=True
            else:
                hijos=self.getHijos(actual)
                self.agregar(hijos,actual,gactual)
            self.Cerrados[actual]=[gactual,pactual]
        self.Soln=self.formaSoln()

## Una clase para agentes inteligentes
class agente:
    def __init__(self,busque):
        self.busque=busque
    def buscar(self,ini,meta):
        self.busque.setIni(ini)
        self.busque.setMeta(meta)
        self.busque.buscar()
        print('EL ORDEN DE VISITA ES:')
        print(self.busque.getSoln())
        