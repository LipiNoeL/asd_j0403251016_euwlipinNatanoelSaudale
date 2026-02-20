#=================================================
#Nama   : Euwlipin Natanoel Saudale
#Nim    : J0403251016
#Kelas  : A1
#=================================================

#=================================================
#Implementasi dasar : Node pada linked list
#=================================================

class node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)
        
#1) membuat node dengan instantiasi class node
nodeA = node("A")
nodeB = node("B")
nodeC = node("C")

#2) menghubungkan node : A -> B -> C
head = nodeA
nodeA.next = nodeB
nodeB.next = nodeC

#4) Traversal: menelusuri node dari head sampai ke none
current = head
while current is not None:    
    print(current.data) #menampilkan data pada node saat ini
    current = current.next #pindah ke node berikutnya
    