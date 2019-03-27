import busqueda
##3b Implementado primero en amplitud, indicar como llegar del inicio a la meta

def main():

    grafo = {'q0':['q1','q2','q3'],
             'q1':['q0','q2','q4'],
             'q2':['q0','q1','q3','q4','q7'],
             'q3':['q0','q2','q6'],
             'q4':['q1','q2','q7'],
             'q5':['q6','q7','q8'],
             'q6':['q3','q5','q8','q9'],
             'q7':['q2','q4','q5','q10'],
             'q8':['q5','q6','q10'],
             'q9':['q6','q11'],
             'q10':['q7','q8','q11'],
             'q11':['q9','q10']
            }
    problema = busqueda.ambiente(grafo)
    amplitud = busqueda.amplitud(problema)
    age = busqueda.agente(amplitud)
    print('ORDEN DE VISITA: SEGUN PRIMERO EN AMPLITUD:')
    age.buscar(input("Ingrese el estado de inicio: "),input("Ingrese el estado meta: "))


## Punto de entrada al programa
if __name__=="__main__":
    main()
