

from dataclasses import dataclass

from typing import Any

from proyecto.graficos.historicos import histograma, burbujas

from proyecto.utils.datos import (leer_datos,
                                  datos_totales)

from proyecto.sir.sir import ModeloISR



@dataclass
class Covid19:
    
    fuente: str = 'confirmados'
    
    def histograma_poblacion(self, x='nombre', **kwargs):
        
        datos = leer_datos(self.fuente)
        
        fig = histograma(datos, x, self.fuente, **kwargs)
        
        fig.show()
        
    def histograma_casos(self):
        
        registros = leer_datos(self.fuente)
        
        fig = histograma(registros,
                         x='nombre',
                         y=self.fuente,
                         titulo=f'Registros {self.fuente}',
                         color=self.fuente)
        
        fig.show()
        
    
    def burbujas(self, fuente2, fuente3):
        
        datos = datos_totales()
        
        fig = burbujas(datos, self.fuente, fuente2, fuente3)
        
        fig.show()
        
    def modelo_sir(self, gamma, beta):
        
        modelo_sir = ModeloISR(gamma=gamma, beta=beta)
        
        return modelo_sir.modelo()
        
        
        
        
        
        
        
        
        