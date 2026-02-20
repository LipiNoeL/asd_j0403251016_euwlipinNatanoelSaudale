#=================================================
#Nama   : Euwlipin Natanoel Saudale
#Nim    : J0403251016
#Kelas  : A1
#=================================================

#=================================================
#Implementasi dasar : Stack
#=================================================

class node:
    #konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstantiasi
    def __init__(self,data):
        self.data = data #menyimpan nilai atau data pada list
        self.next = None #pointer ini menunjuk ke note berikutnya (awal=none)
        

#stack ada perasi push(memasukkan head baru) dan pop (menghapus head)


class stack:
    def __init__(self):
        self.top = None #top menunjuk ke node paling atas (awalnya kosong)
        
    def is_empty(self):
        return self.top is None #stack kosong jika top = none 
        
    def push(self, data): #memasukkan data baru pada stack
        #1 membuat node baru
        nodeBaru = node(data) #instantiasi?memanggil konstruktor pada class nide
        
        #2 node baru menunjuk ke top yang lama (head lama)
        nodeBaru.next = self.top
        
        #3 geser top pindah ke node baru
        self.top = nodeBaru
        
    def pop(self): #mengambil / menghapus node paling atas (top/head)
        if self.is_empty():
            print("Stack Kosong, tidak bisa Pop")
            return None
        dataTerhapus = self.top.data #soroti bagian top dan simpan di variabel (peek)
        #B -> A => none
        self.top = self.top.next #geser top ke node berikutnya
        return dataTerhapus
    
    def peek(self):
        #melihat data yang paling atas tanpa menghapus
        if self.is_empty():
            return None
        return self.top.data
        
    def tampilkan(self):
        #Top -> A -> B
        current = self.top
        print("Top " , end="->" )
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")
        
#instantiasi class stack
s = stack()
s.push("A")
s.push("B")
s.push("C")
s.tampilkan()
print ("Peek (Lihat Top): ", s.peek())
s.pop()
s.tampilkan()
print ("Peek (Lihat Top): ", s.peek())