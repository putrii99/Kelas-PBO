class student():
    
    def nama(self):
        print("Nama :", self.full_name)
    def get_age (self):
        print("Usia :", self.age)
    def get_alamat (self):
        print("alamat :", self.alamat)
    def get_status (self):
        print("status :", self.status)
budi = student()

budi.full_name = "Budi Permana"
budi.age = "21"
budi.alamat = "Purwakarta"
budi.status = "mahasiswa"

budi.nama()
budi.get_age()
budi.get_alamat()
budi.get_status()