1) ¿Cuáles son las principales diferencias entre una lista y una tupla?
2) ¿Cuáles son las principales diferencias entre un conjunto y una lista?
3) ¿Cuáles son las principales diferencias entre una pila y una cola?
4) Realizar un cuadro comparativo entre las siguientes estructuras: Listas, Tuplas, Conjuntos,
Diccionarios, Pilas, Colas.

5a) Implementar la clase ContenedorIterable, la cual debe poder agregar números y debe
permitir recorrerlos mediante un iterador. Los números agregados son de un tipo indicado por
un número que se pasa como parámetro, que puede ser 1 o 2. Y deben ser recorridos en el
mismo orden en que fueron agregados, primero todos los tipo 1, y luego todos los tipo 2, es
decir, si se agregan los siguientes números (5, 1), (3, 1), (4, 2), (8, 1), (10, 2) al recorrer deben
retornarse en este orden: 5, 3, 8, 4, 10.

5b) Implementar la clase ContenedorIterable2 igual a la anterior pero usando un generator para
recorrer el contenedor, en vez de retornar un iterador (si ya usaste un generator en el item
anterior, entonces implementá un iterador)

6) Implementar la estructura Pila usando TDD, teniendo en cuenta la siguiente descripción. 

-Una pila soporta una cantidad máxima de elementos. 💹
-El método apilar agrega un elemento a la pila.💹
-Si la pila está llena se debe levantar un error del tipo PilaLlena.💹

-El método desapilar retira un elemento de la pila, y lo retorna.💹
-El elemento desapilado siempre debe ser el último que se apiló.💹

-Si la pila está vacía, se debe levantar un error del tipo PilaVacia.💹

-Se debe poder saber la cantidad de elementos apilados utilizando el operador len(pila).💹
-Se debe poder obtener un iterador a la pila mediante el operador iter(pila). 💹
-Este iterador debe recorrer los elementos de la pila en el mismo orden en que estos serían desapilados, pero sin desapilarlos (es decir, sin modificar la pila).💹

7) Utilizando TDD. Modificar la pila para agregar un método __reversed__(self) el cual devuelva un iterador inverso que permita recorrer la pila en el orden opuesto.

8) Utilizando TDD. Crear una nueva estructura PilaConPrioridad, con funcionalidad similar a la
Pila, respetando las siguientes diferencias. El apilado debe recibir un parámetro de prioridad,
que puede ser 0 o 1. En caso de recibir una prioridad distinta, se debe levantar un error
ValueError. A la hora de desapilar, se debe desapilar siempre el elemento de mayor prioridad. Si
hay más de un elemento de mayor prioridad, se debe desapilar el último de los apilados de esa
prioridad. Por ejemplo, si apilamos los siguientes elementos (5, prioridad 1), (3, prioridad 0), (4,
prioridad 0), (6, prioridad 1), el desapilado debe ser: 6, 5, 4, 3. Antes de implementar este item,
pensar y responder la siguiente pregunta:

b) ¿Cuáles de las siguientes técnicas conviene utilizar a la hora de extender el
comportamiento de Pila para este item, y cuáles no? Justificar en cada caso.

Herencia.
Polimorfismo.
Composición.
Abstracción.
Delegación.

9) Utilizando TDD. Extender la implementación de PilaConPrioridad para que en vez de
solamente soportar las prioridades 0 y 1, la misma se instancie con un parámetro que indique la
máxima prioridad soportada.