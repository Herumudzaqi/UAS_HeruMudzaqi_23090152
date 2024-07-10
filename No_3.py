class RestaurantQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, order):
        """Menambahkan pesanan baru ke dalam antrian."""
        self.queue.append(order)
        print(f"Pesanan '{order}' telah ditambahkan ke dalam antrian.")

    def dequeue(self):
        """Menghapus pesanan dari depan antrian."""
        if len(self.queue) > 0:
            removed_order = self.queue.pop(0)
            print(f"Pesanan '{removed_order}' telah dihapus dari antrian.")
            return removed_order
        else:
            print("Antrian kosong, tidak ada pesanan yang dapat dihapus.")
            return None

    def display_queue(self):
        """Menampilkan semua pesanan dalam antrian."""
        if len(self.queue) > 0:
            print("Pesanan dalam antrian:")
            for order in self.queue:
                print(f"- {order}")
        else:
            print("Antrian kosong.")

# Main program
if __name__ == "__main__":
    queue = RestaurantQueue()

    queue.enqueue("Nasi lengko")
    queue.enqueue("Nasi campur")
    queue.enqueue("soto")

    queue.display_queue()

    queue.dequeue()
    queue.dequeue()

    queue.display_queue()

    queue.dequeue()
    queue.dequeue()
