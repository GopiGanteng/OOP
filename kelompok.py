from abc import ABC, abstractmethod

class BarangElektronik(ABC):
    def __init__(self, nama, harga_dasar, stok):
        self.nama = nama
        self.__harga_dasar = harga_dasar
        self.__stok = stok

    # Getter stok
    def get_stok(self):
        return self.__stok

    # Setter stok (validasi tidak boleh negatif)
    def tambah_stok(self, jumlah):
        if jumlah < 0:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
        else:
            self.__stok += jumlah
            print(f"Berhasil menambahkan stok {self.nama}: {jumlah} unit.")

    # Getter harga dasar (protected usage)
    def _get_harga_dasar(self):
        return self.__harga_dasar

    @abstractmethod
    def tampilkan_detail(self):
        pass

    @abstractmethod
    def hitung_harga_total(self, jumlah):
        pass


class Laptop(BarangElektronik):
    def __init__(self, nama, harga_dasar, stok, processor):
        super().__init__(nama, harga_dasar, stok)
        self.processor = processor

    def tampilkan_detail(self):
        print(f"[LAPTOP] {self.nama} | Proc: {self.processor}")

    def hitung_harga_total(self, jumlah):
        harga = self._get_harga_dasar()
        pajak = harga * 0.10
        subtotal = (harga + pajak) * jumlah
        return harga, pajak, subtotal


class Smartphone(BarangElektronik):
    def __init__(self, nama, harga_dasar, stok, kamera):
        super().__init__(nama, harga_dasar, stok)
        self.kamera = kamera

    def tampilkan_detail(self):
        print(f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}")

    def hitung_harga_total(self, jumlah):
        harga = self._get_harga_dasar()
        pajak = harga * 0.05
        subtotal = (harga + pajak) * jumlah
        return harga, pajak, subtotal


def proses_transaksi(daftar_barang):
    print("\n--- STRUK TRANSAKSI ---")
    total_bayar = 0

    for i, (barang, jumlah) in enumerate(daftar_barang, start=1):
        barang.tampilkan_detail()
        harga, pajak, subtotal = barang.hitung_harga_total(jumlah)

        print(f"Harga Dasar : Rp {harga:,}")
        print(f"Pajak       : Rp {pajak:,}")
        print(f"Beli        : {jumlah} unit | Subtotal: Rp {subtotal:,}\n")

        total_bayar += subtotal

    print("=" * 30)
    print(f"TOTAL TAGIHAN: Rp {total_bayar:,}")
    print("=" * 30)


print("--- SETUP DATA ---")

laptop = Laptop("ROG Zephyrus", 20000000, 10, "Ryzen 9")
iphone = Smartphone("iPhone 13", 15000000, 20, "12MP")

# Coba stok negatif
laptop.tambah_stok(10)
iphone.tambah_stok(-5)
iphone.tambah_stok(20)

# Transaksi user
keranjang = [
    (laptop, 2),
    (iphone, 1)
]

proses_transaksi(keranjang)