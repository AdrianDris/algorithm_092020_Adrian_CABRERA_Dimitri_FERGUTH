class Heap(object):
    """
    Une heap est une structure de données sous forme d'arbre.

    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        pass

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        pass

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def decrease_key(self, current_value: int, new_value :int) -> None:
        """
        Modify une valeur dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        """
        Fusionne deux arbres
        """
        pass        


class FibonacciHeap(Heap):
    """
    Chaque case dans l’arbre est une valeur
    Exemple avec 1 seule valeur par branche (la racine)
    1 - Trouver le minimum dans la liste des racines et retourner la valeur de cette variable
    2 - insertion : insérons un chiffre dans l’arbre (à la suite de la liste) -> append
    3 - Si la valeur ajouté est un nouveau minimum -> mettre à jour le minimum
    4 - fusion de 2 arbres – ajouter le nouvel arbre dans la liste du précédent arbre (merge le 2eme dans le 1er) puis récupérer le minimum de l’arbre 2 et le comparer avec le minimum de l’arbre 1. Si la valeur du 2 n’est pas plus petit que le 1er on peut oublier la valeur minimum du second arbre
    5 - Si le minimum du second arbre est plus petit que celui du 1er, on met à jour la valeur minimum
    """

    def __init__(self):
        self.tree = []

    def insert(self, value: int) -> None:
        self.tree.append(value)

    def find_min(self) -> int:
        return min(self.tree)

    def delete_min(self, value: int) -> int:
        
        pass

    def merge(self,fibonnaci_heap: Heap) -> None:
        if ( len(self.tree) == len(heap2.tree) ) :
            return self.tree + heap2.tree
        else :
            return print('les deux arbres n\'ont pas le même nombre d\'élément')

heap = FibonacciHeap()
heap.insert(2)
heap.insert(5)
heap.insert(8)
heap.insert(4)
print('Arbre 1 : {}\n'.format(heap.tree))
print('Plus petite valeur de Arbre 1 : {}\n'.format(heap.find_min()))
heap.insert(0)
print('Arbre 1 après ajout d\'une valeur: {}\n'.format(heap.tree))
print('Plus petite valeur de Arbre 1 après ajout d\'une valeur: {}\n'.format(heap.find_min()))

heap2 = FibonacciHeap()
heap2.insert(0)
heap2.insert(4)
heap2.insert(8)
heap2.insert(7)
heap2.insert(6)
heap.insert(42)
heap2.insert(0)

print('Arbre 2 : {}\n'.format(heap2.tree))
print('Plus petite valeur de Arbre 2 : {}\n'.format(heap2.find_min()))

print('Arbres fusionnés : {}\n'.format(heap.merge(heap2)))