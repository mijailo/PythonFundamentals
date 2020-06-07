# Conceptos básicos de programación

*Durante esta lectura encontrarás bloques de código, no es necesario que te detengas a copiarlos y ejecutarlos, solo están ahí para fines demostrativos*

Comúnmente cuando queremos aprender a programar lo primero que buscamos es un lenguaje de programación amigable que nos permita introducirnos en el medio de forma sencilla y rápida, sin embargo comenzar de esa forma suele ser como dicen de forma coloquial, empezar con el pie equivocado. 

Programar, sin importar la intención o el lenguaje, es una forma de pensar, un medio a través del cual solucionamos problemas. En programación hay montones de formas de realizar una misma tarea. Pongamos un ejemplo para ejemplificar que antes de  *tirar código* (frase escuchada en la comunidad y motivo de mas de una de mis carcajadas) es necesario tener un problema a solucionar. Muchas veces cuando comenzamos a aprender a programar comenzamos por ver como se declaran las variables, cuál es la sintaxis de los condicionales, etc. No es un mal comienzo, sin embargo no diría que es el mejor, lo mejor es tener un problema a resolver, no necesita ser un problema complejo, sino algo que te haga preguntarte el cómo se puede solucionar a través de la programación, por eso diremos que:

**0.- Antes de programar, busca un problema, algo que puedas solucionar.**

(¿Por qué **0** y no **1**?, porque ya había escrito la primera regla y me quería sentir físico una vez mas.)

Para mostrar que no necesitamos un problema muy difícil para comenzar a programar elegiremos uno del uso común, la respuesta del universo, por lo tanto vamos a construir una función que dadas dos entradas, las que sean, regrese el valor **42**.

Antes de comenzar a plantear algunas soluciones es necesario preguntarnos que es lo que realmente deseamos como respuesta y cuales son nuestras entradas, ya que dependiendo esa combinación es como nos acercaremos a soluciones realmente útiles. Si el caso fuera obtener una salida con formato como *cadena de texto* y las entradas como variables *numéricas* entonces podemos intuir que durante el proceso necesitaremos jugar con el tipo de variable por ejemplo

    def respuesta_universo(entrada1: int, entrada2: int) -> str:
        total = entrada1 + entrada2
        
        # Cambiamos el tipo de variable haciendo un entero 
        # a una cadena a través del método str()
        total_cadena = str(total) 

        return total_cadena


Entonces

    respuesta_universo(20, 22)  
    
    [1]: "42"


**NOTA:**  la notación ***variable: tipo_de_variable*** como ***entrada: int*** solo es para documentar el tipo de variable que se espera en el argumento, así como la notación ***-> str*** refiere al tipo de variable que se pretende regresar al final de la función, sin embargo no existe una utilidad más allá de eso y generalmente no es empleada, la utilizamos en el ejemplo solo con fines didácticos pero no la emplearemos mas a menos de ser realmente necesaria para detallar en los tipo de variables en las entradas y las salidas.

Por otro lado, si la combinación de entrada-salida fuera: enteros (int) -> entero (int), no sería necesaria la trasformación de variables

    def respuesta_universo(entrada1: int, entrada2: int) -> int:
        total = entrada1 + entrada2

        return total_cadena

Entonces

    respuesta_universo(20, 22)  
    
    [1]: 42

Concluyamos el ejemplo con el caso donde la combinación de entrada-salida es del tipo: cadena (str) -> cadena(str)

    def respuesta_universo(entrada1: str, entrada2: str) -> str:
        cadena_final = entrada1 + entrada2

        return cadena_final

Entonces

    respuesta_universo("4", "2")  
    
    [1]: "42"


De lo anterior podemos aprender que:

***1.- Antes de empezar a programar necesitamos conocer nuestras entradas y tener claro que queremos como salida.***

Ya tenemos definido nuestro problema, y digamos que la relación entrada-salida es **int->int**, por lo tanto ahora debemos plantear una solución. Hemos dicho que existen montones de soluciones, sin embargo tomaremos el tercer mandamiento del [Python Zen](https://www.python.org/dev/peps/pep-0020/): *Simple es mejor que complejo*. Este mandamiento nos ayuda a evitar la pérdida de muchas horas en el futuro tratando de entender o mantener una solución compleja. Vamos a ejemplificar lo anterior con dos posibles soluciones: la primera, compleja, que seguro encontramos navegando en [stackoverflow](https://stackoverflow.com/) y que hemos copiado sin antes entenderla

    def respuesta_universo(*args, **kwargs):
        # Regresa la respuesta del universo o levanta un error
        
        
        suma_args = sum([_ for _ in args if type(_) is int])

        suma_kwargs = sum([v for k,v in kwargs.items() if v is int])

        suma_total = suma_args + suma_kwargs

        if suma_total == 42:
            return suma_total
        
        else:
            raise Execption("El universo no tiene respuesta")


Ahora plantearemos la segunda más simple

    def respuesta_universo(entrada1, entrada2):
        # Regresa la suma de las entradas

        respuesta = respuesta1 + respuesta2

        return respuesta

Estas soluciones nos enseñan lo siguiente:

***2.- Nunca copies código de internet sin entender que es lo que realmente hace***

Las soluciones muestran algo más de fondo. La primera restringe la respuesta al valor correcto del universo mientras que la segunda en realidad puede devolver cualquier valor entero aunque sea distinto de **42**, lo que nos lleva al siguiente punto:

***3.- Nunca esperes casos innecesarios.***

El punto **3** es de suma importancia cuando comenzamos a desarrollar ya que nos evitará perder tiempo codificando casos que nunca sucederán, también hará que nuestro código sea más limpio y sea más fácil de mantener. Cuando comenzamos a desarrollar, ya sea para nosotros o para usuarios ajenos, pensamos que el sujeto que interactúe con nuestro código introducirá valores tan extraños que ni a nosotros se nos hubieran ocurrido, por lo que comenzamos a cubrir todos los casos que se nos vengan a la mente previniendo una catástrofe en el universo, sin embargo no debe ser así. Si ya hemos definido el tipo de variable o el valor de entrada, entonces debes garantizar que siempre se cumpla, por lo tanto es necesario siempre validar la información que nos es entregada. Mostremos un ejemplo de como podríamos hacerlo.

    def validar_entradas(entradas1, entrada2):
        """
        Verificamos de dos formas equivalentes
        si las entradas son del tipo cadenas.
        La partícula assert actúa como una compuerta,
        en caso de que la respuesta sea falsa entonces levantará un error,
        previniendo que se siga ejecutando el resto del código.
        """

        assert type(entradas1) is str
        assert isinstance(entrada2, str)


Notemos que hemos creado una función independiente para realizar las validaciones y no lo hemos hecho dentro de nuestra función *respuesta_universo*, esta práctica es conocida como factorización y debe ser utilizada si o si, por lo tanto nuestro proceso para obtener la respuesta del universo la haríamos en dos partes, la primera validando y la segunda solicitando la respuesta

    entrada1 = 21
    entrada2 = 21
    validar_entradas(entrada1, entrada2)
    respuesta_universo(entrada1, entrada2)

Podríamos hacer la validación dentro de la función *respuesta_universo* sin embargo mantenerla después puede resultar complicado, entonces, la siguiente regla sería:

***4.- No construyas funciones demasiado largas.***


Vamos a cerrar esta introducción con un concepto que en lo personal me encanta:

***5.- Una entrada una salida, si funciona, avanzamos.***

Uno de los errores más comunes cuando empezamos, vamos a medio camino o incluso cuando ya estamos medio curtidos es querer resolver todo de una sola sentada, esto suele ser una pérdida de tiempo pues vamos a pasar horas arreglando una cantidad innecesaria de bugs, así que siempre, verifica un flujo feliz, si funciona entonces avanza. 


Todos los consejos anteriores los llamo como la filosofía de **Pensar en cajitas**, si los sigues de forma recurrente verás que ningún lenguaje de programación será difícil de aprender, mucho menos **Python** ques es muy amable.