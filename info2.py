

def longest(dag,currentNode):
    path=[]
    def allpath(currentNode,currentCost):
        if(len(dag[currentNode])==0):
            path.append(currentCost)
        else:
            for i in dag[currentNode]:
                allpath(i,currentCost+1)
    allpath(currentNode,0) #per il caso nostro che va messo sui livelli dipende da dove iniziamo a contare
    return max(path)


def newmax(candidati, n,etichettatura):
    locale=[]
    for i in candidati:
        locale.append(i)
    result=[]
    while(len(result)<n):
        max=0
        for i in locale:
            if etichettatura[i]>max:
                max=etichettatura[i]
                key=i
        result.append(key)
        locale.remove(key)
    return result



#fase1
def CoffmanGraham(dag):
    app = {}
    dag2 = {}
    for i in dag:
        dag2[i] = []
        app[i] = []
    for i in dag:
        if dag[i] != None:
            for a in dag[i]:
                dag2[a].append(i)
                app[a].append(i)
    etichettatura={}
    label=1
    while len(etichettatura) < len(dag):
        candidati = []
        for i in app:
            if len(app[i]) == 0:
                candidati.append(i)
        if label == 1:
            scelto = candidati.pop(0)
        else:
            min2 = len(dag)
            key = 0
            for aa in candidati:
                if len(dag2[aa]) == 0:
                    min2 = 0
                    key = aa
                else:
                    lista = dag2[aa]
                    for k in etichettatura:
                        if k in lista:
                            if etichettatura[k] < min2:
                                min2 = etichettatura[k]
                                key = aa
            scelto = key
        etichettatura[scelto] = label
        label += 1
        for eliminare in app:
            if scelto in app[eliminare]:
                app[eliminare].remove(scelto)
        app.pop(scelto)

#fase2 coffman


    app2 = {}
    for i in dag:
        app2[i] = dag[i]

    candidati = []
    contatore = 0
    w = 3
    sistemazione = {}
    layering = {}
    livello = 0

    while contatore < len(dag):
        candidati = []
        for i in app2:
            if len(app2[i]) == 0:
                candidati.append(i)
        if len(candidati) <= w:
            layering[livello] = []
            for i in candidati:
                sistemazione[i] = livello
                layering[livello].append(i)
                app2.pop(i)
                for eliminare in app2:
                    if i in app2[eliminare]:
                        app2[eliminare].remove(i)
            livello += 1
            contatore += len(candidati)

        else:
            while len(candidati) > w:
                cand2 = newmax(candidati, w,etichettatura)
                layering[livello] = []
                for cand in cand2:
                    layering[livello].append(cand)
                    sistemazione[cand] = livello
                    candidati.remove(cand)
                    app2.pop(cand)
                    for eliminare in app2:
                        if i in app2[eliminare]:
                            app2[eliminare].remove(i)
                livello += 1
                contatore += len(cand2)
            layering[livello] = []
            for i in candidati:
                sistemazione[i] = livello
                layering[livello].append(i)
                app2.pop(i)
                for eliminare in app2:
                    if i in app2[eliminare]:
                        app2[eliminare].remove(i)
            livello += 1
            contatore += len(candidati)
    return layering







dag={}
dag['a']=['b','c']
dag['b']=['f','d']
dag['c']=['d','e','g']
dag['f']=['d']
dag['g']=['e']
dag['e']=[]
dag['d']=[]

a=CoffmanGraham(dag)
print(a)

