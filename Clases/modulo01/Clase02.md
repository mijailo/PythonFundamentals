##Presentando el problema

En el momento que escribo esto es el día 86 de mi cuarentena a causa del virus **SARS-CoV-2**, momento en que ya hay suficientes datos para hacer una bonita gráfica aprendiendo a programar en **Python**.

Es por eso que el problema que presento para este curso es realizar un pequeño modelo de predicción sobre los datos existentes por estado en México.

**NOTA:** El objetivo no es un modelo preciso, sino aprender a construir módulos con **Python**

##Sintaxis básica y lenguaje del curso  para comenzar

##### Declarar varibles 
Decimos *declarar variables* cuando asignamos algún valor a una variable a tra´
 de la siguiente notación

    variable = 1

Mencionaremos un par de reglas básicas en la declaración de variables:
*   El nombre de la variable no puede comenzar con número
*   Es permitido iniciar con *_* o *__* sin embargo se reservan estos prefijos para casos especiales

Consejos para la declaración de variables:
*   El nombre de las variables se escriben con minúsculas y las palabras van separadas por guiones bajos, *nombre_variable*
*   El nombre de las variables debe hacer ser explícito haciendo referencia al valor que almacena, *iva = 0.16*
  
Demos una ejemplo donde se muestra la importancia de lo anterior

    def f(x,y):
        z = (1 + x)*y

        return z

Este tipo de funciones es críptica e imposible de saber su propósito

    def pago_total(monto, iva):
        pago = (1 + iva)*monto

        return pago

Ambas funciones hacen exactamente lo mismo, sin embargo solo la segunda nos habla por sí sola de su funcionalidad. 

##### Comentarios

Documentar nuestro código es una inversión de tiempo a futuro, más vale gastar un minuto en documentar el código que pasar horas tratando de entender en el futuro lo que pensamos en el pasado. 

    # Esto es un comentario de una línea

    """
    Esto es
    un comentario
    de varias líneas
    """


##### Indentación

La indentación refiere al espaciado realizado comúnmente por *tabs* o 4 espacios. **Python** es un lenguaje indentado, es decir que jerarquiza las secciones de código según el nivel de indentación que tenga. Diremos que una línea de código está indentada cuando comience con espaciado y esto significa que está sujeta a la última línea de  código prevía a la indentación.

    monto = 999

    if monto > 1000:
        impuesto = 0.16
    else: 
        impuesto = 0.15

    
las líneas donde se declara el valor impuesto están sujetas a las líneas previas a ellas. Esto no solo aplica para condicionales, también aplica para funciones, ciclos, clases, etc. 

La indentación no se limita a un nivel

    monto = 999
    presupuesto = 1200

    if presupuesto > 0:
        if monto > 500:
            impuesto = 0.16
        else:
            impuesto = 0.17

    else:
        print("Sin fondos")



Si existe alguna línea de la cual dependa la siguiente sección de código y esta última no estuviera indentada nos devolverá un error de indentación.

    monto = 999

    # Esto nos regresará un error
    if  monto > 1000:
    impuesto = 0.16





