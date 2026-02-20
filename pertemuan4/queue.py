#=================================================
#Nama   : Euwlipin Natanoel Saudale
#Nim    : J0403251016
#Kelas  : A1
#=================================================

#=================================================
#Implementasi dasar : Queue 
#=================================================


class Node:
    # Konstruktor yang dijalankan secara otomatis ketika class Node dipanggil / diinstansiasi
    def __init__(self, data):
        # Menyimpan nilai atau data pada list
        self.data = data
        # Pointer ini menunjuk ke note berikutnya (awal = None)
        self.next = None


class Queue:
    # Buat konstruktor untuk inisialisasi variabel front dan rear
    def __init__(self):
        self.front = None  # Node paling depan
        self.rear = None  # Node paling belakang

    def is_empty(self):
        return self.front is None

    # Membuat fungsi untuk menambahkan data baru
    def enqueue(self, data):
        nodeBaru = Node(data)

        # Jika Queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        # Jika Queue tidak kosong, maka letakkan data baru ke setelah rear, dan jadikan data baru sebagai rear
        self.rear.next = nodeBaru  # Letakkan data baru pada setelahnya rear
        self.rear = nodeBaru  # Jadikan data baru sebagai rear

    def dequeue(self):
        # Menghapus data dari depan / front
        data_terhapus = self.front.data  # Lihat data paling depan

        # Geser front ke node berikutnya
        self.front = self.front.next

        # Jika setelah geser front menjadi None, maka Queue kosong
        if self.front is None:
            self.rear = None

        return data_terhapus

    def tampilkan(self):
        current = self.front
        print("Front ->", end=" ")
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print(" Rear")


# Instansiasi class Queue
q = Queue()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()
q.dequeue()
q.tampilkan()
q.dequeue()
q.tampilkan()