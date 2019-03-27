import busqueda
##3c: Implementado preferente por lo mejor, indicar el camino desde el inicio a la meta

## Una funcion main
def main():
    grafo = {'q0':{'q1':10,'q2':12,'q3':9},
             'q1':{'q0':10,'q2':11,'q4':15},
             'q2':{'q0':12,'q1':11,'q4':10,'q7':17,'q3':11},
             'q3':{'q0':9,'q2':11,'q6':9},
             'q4':{'q1':13,'q2':10,'q7':12},
             'q5':{'q6':10,'q7':9,'q8':10},
             'q6':{'q3':9,'q5':10,'q8':14,'q9':13},
             'q7':{'q2':17,'q4':12,'q5':9,'q10':12},
             'q8':{'q5':10,'q6':14,'q10':14},
             'q9':{'q6':13,'q11':25},
             'q10':{'q7':12,'q8':14,'q11':14},
             'q11':{'q9':25,'q10':14}
            }

    problema = busqueda.ambiente(grafo)
    busque = busqueda.prefmej(problema)
    age = busqueda.agente(busque)
    print('SEGUN PREFERENTE POR LO MEJOR:')
    age.buscar(input("Ingrese el estado de inicio: "),input("Ingrese el estado meta: "))


## Punto de entrada al programa
if __name__=='__main__':
    main()
