import plotly.express as px


def histograma(datos, x, y, titulo='', **kwargs):
    
    fig = px.bar(datos, x, y,  **kwargs)
    
    fig.update_traces(texttemplate='%{text:.2s}',
                      textposition='outside',
                      opacity=0.6)
    
    fig.update_layout(uniformtext_minsize=8,
                      uniformtext_mode='hide',
                      title=titulo)
    
    return fig


def burbujas(datos, fuente1, fuente2, fuente3):
    
    return  px.scatter(datos,
                       x=fuente1,
                       y=fuente2,
                       size=fuente3,
                       color='nombre')
    
    