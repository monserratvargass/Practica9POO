#una clase para representar un conjunto disjunto
class DisjointSet:
    parent={}
    #realiza la operacion MakeSet
    def makeSet(self,n):
        #crear n 
        for i in range(n):
            self.parent[i]=i
    def find(self,k):
        if self.parent[k]==k:
            return k
        
        return self.find(self.parent[k])
    
    def union(self,a,b):
        #encontar la raiz de los conjuntos a los que perteneven los elementos x e y
        x=self.find(a)
        y=self.find(b)

        self.parent[x]=y
#FUNCION para construuir mst usando el algoritmo de Kruskal
def run_Kruskal_Algorithm(edges,n):
        
    MST=[]

        #inicializar la clase dijs
        #crea un conjunto singleton para cada elemneto del universo
    ds=DisjointSet()
    ds.makeSet(n)
    index=0
        #ordena los bordes aunmentando el peso

    edges.sort(key=lambda x: x[2])

#MST contiene exactamente aristas v-1

    while len(MST) !=n -1:
        #considerar el borde el siguiente con peso minimo del graph
        (src,dest,weight)=edges[index]
        index = index + 1

        #encontrar la raiz de los c onjuntos a los que se unen dos extremos
        #vertices de  la sigbuiente aruista pertenecen

        x=ds.find(src)
        y=ds.find(dest)

        #si amnbos extremos tiene diferentes oadres, pertenecen a 
        #diferentes componentes conectados y se pueden incluir en MST

        if x !=y:
            MST.append((src,dest,weight))
            ds.union(x,y)
    return MST

if __name__=='__main__':

    #u,v,w el tiprete representa un borde no dirigido desde
    #vertice u a vertice v con peso w


    edges = [(1,2,3),(1,3,7),(1,4,2),(1,8,10),
             (2,3,5),(2,4,6),(2,5,5),(2,5,9),(2,7,9),(3,5,3),(3,6,5),
    (5,6,9),(4,7,3),(7,6,5)
    ]

        #numero total de nodo en el grafo(etiquetaso de 0 a 6)
    n=7

        #grafo de constrccuin
    e=run_Kruskal_Algorithm(edges,n)

    print(e)

