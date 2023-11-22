# Jawaban no 1
def profile(nama, alamat, gender, umur):
    print("nama saya adalah", nama)
    print("alamat saya adalah", alamat)
    print("gender saya adalah", gender)
    print("umur saya adalah", umur)

profile("Arifki","Bogor","Laki-Laki",22)

# Jawaban no 2
def kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif nilai >= 61 and nilai <= 70:
        return "Baik"
    elif nilai >= 71 and nilai <= 80:
        return "Sangat baik"
    elif nilai >= 81 and nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai Tidak Valid"
    
print(kelulusan(70))

# Jawaban no 3
def ganjil(n):
    for i in range(1,n+1,2):
        print(i)
# pemanggilan
ganjil(100)