from dataclasses import dataclass

from scipy.integrate import odeint

from numpy import log, linspace

from pandas import DataFrame

@dataclass
class ModeloISR:
    
    gamma: float
    
    beta: float
    
    N : int = 1000
    
    I0 : int = 1
    
    R0 : int = 0
    
    t_max: int = 160
    
    @property
    def S0(self):
        
        return self.N - self.I0 - self.R0
    
    def tasa_susceptibles(self, susceptibles, infectados):
        """
        Tasa de infectados
        dS/dt = -beta * S * I / N
        """
        return -self.beta * susceptibles * infectados / self.N
        
    
    def tasa_infectados(self, susceptibles, infectados, c=0):
        """
        Tasa de infectados
        dI/dt = beta * S * I / N - gamma * I
        """
        return self.beta * susceptibles * infectados / self.N - self.gamma * infectados

    
    def tasa_recuperados(self, infectados):
        """
        Tasa de infectados
        dR/dt =  gamma * I
        """
        return self.gamma * infectados
    
    def intervalo_tiempo(self):
        
        return linspace(0, self.t_max, self.t_max)
    
    def derivadas(self, y, t):
        susceptibles, infectados, _ = y
        
        dSdt = self.tasa_susceptibles(susceptibles, infectados)
        
        dIdt = self.tasa_infectados(susceptibles, infectados)
        
        dRdt = self.tasa_recuperados(infectados)
        
        return dSdt, dIdt, dRdt
    
    
    def modelo(self):
        def deriv(y, t):
            susceptibles, infectados, _ = y
            dSdt = self.tasa_susceptibles(susceptibles, infectados)
            dIdt = self.tasa_infectados(susceptibles, infectados)
            dRdt = self.tasa_recuperados(infectados)
            
            return dSdt, dIdt, dRdt
        
        condiciones_iniciales = self.S0, self.I0, self.R0
        
        res = odeint(deriv,
                     condiciones_iniciales,
                     self.intervalo_tiempo())
        
        susceptibles, infectados, recuperados = res.T
        
        datos_modelo = DataFrame({'susceptibles': susceptibles/self.N,
                                  'infectados': infectados/self.N,
                                  'recuperados': recuperados/self.N})
        
        return datos_modelo
        
        
        
    
    
        
    
    
    