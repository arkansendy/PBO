import os
os.system('CLS')


class Sekolah:
    def __init__(self, nama, akreditasi, jurusan):
        self.__nama = nama
        self.__akreditasi = akreditasi
        self.__jurusan = jurusan

    def lihat_jadwal(self):
        print(
            f"Jadwal pelajaran untuk {self.__nama} dengan akreditasi {self.__akreditasi} jurusan {self.__jurusan} adalah B.Indonesia")

    def upacara(self):
        print(
            f"Sekolah yang berakreditasi {self.__akreditasi} yaitu {self.__nama} menugaskan jurusan {self.__jurusan} sebagai petugas upacara.")

    def ekstrakulikuler(self):
        print(
            f"Jurusan {self.__jurusan} mengikuti lomba ekstrakurikuler di {self.__nama} yang berakreditasi {self.__akreditasi}.")

    # Getter methods
    def get_nama(self):
        return self.__nama

    def get_akreditasi(self):
        return self.__akreditasi

    def get_jurusan(self):
        return self.__jurusan

    # Setter methods
    def set_nama(self, nama):
        self.__nama = nama

    def set_akreditasi(self, akreditasi):
        self.__akreditasi = akreditasi

    def set_jurusan(self, jurusan):
        self.__jurusan = jurusan

# Create new objects and access private properties using getter and setter methods
nama_sekolah1 = Sekolah('SMAN 1 Bhakti Pertiwi', 'A', 'IPA & IPS')
nama_sekolah2 = Sekolah('SMK 2 MUHAMMADIYAH', 'A', 'Multimedia')

print()
nama_sekolah1.lihat_jadwal()
print()
nama_sekolah2.upacara()
print()
nama_sekolah2.ekstrakulikuler()

# Access private properties using getter and setter methods
print(nama_sekolah1.get_nama())
nama_sekolah1.set_nama('SMAN 2 Bhakti Pertiwi')
print(nama_sekolah1.get_nama())
print(nama_sekolah2.get_jurusan())
nama_sekolah2.set_jurusan('TKJ')
print(nama_sekolah2.get_jurusan())
