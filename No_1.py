def main():
    students = []

    while True:
        nim = input("Masukkan NIM: ")
        nama = input("Masukkan Nama: ")
        
        students.append({"NIM": nim, "Nama": nama})

        tambah_lagi = input("Ingin tambah lagi? (YA/TIDAK): ").strip().lower()
        if tambah_lagi != 'ya':
            break

    print("Data Mahasiswa:")
    for student in students:
        print(f"NIM: {student['NIM']}, Nama: {student['Nama']}")

if __name__ == "__main__":
    main()
