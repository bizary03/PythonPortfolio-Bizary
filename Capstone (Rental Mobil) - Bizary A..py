#Capstone Porject rental mobil



#Stok Mobil in Listed Dictionary :[{'Kode','Merk','Type','Tahun','Kategori','Stok','Harga'}]
stokMobil = [
    {'Kode Mobil':'HD1',
     'Merk':'Honda',
     'Type':'CRV',
     'Tahun':2021,
     'Kategori':'SUV',
     'Stok':2,
     'Harga':900000},

     {'Kode Mobil':'TY1',
     'Merk':'Toyota',
     'Type':'Innova',
     'Tahun':2022,
     'Kategori':'SUV',
     'Stok':1,
     'Harga':800000},
     
     {'Kode Mobil':'KA1',
     'Merk':'Kia',
     'Type':'Sonet',
     'Tahun':2022,
     'Kategori':'MPV',
     'Stok':3,
     'Harga':650000},
     
     {'Kode Mobil':'HD2',
     'Merk':'Honda',
     'Type':'Brio',
     'Tahun':2020,
     'Kategori':'City',
     'Stok':3,
     'Harga':450000},]


# Main Menu
def MainMenu(): # Input menu (1-5)
    global menu
    menu = int(input('''
    ----------Rental Mobil Capstone---------
    ________________________________________
    Menu:
    1. Daftar Stok Mobil
    2. Tambah Daftar Mobil
    3. Hapus Daftar Mobil
    4. Update Stok dan Harga Mobil
    5. Keluar Program
    
    Pilihan Menu : '''))
    return menu


# Sub Menu
def SubMenu(): # Input sub menu (1-3)
    global subMbenu
    subMbenu = int(input('''
    1] Daftar Lengkap
    2] Daftar Stok
    3] Kembali ke Menu Utama

    Masukan Sub-Menu Daftar Stok : '''))
    return subMbenu


# Daftar Mobil Lengkap Print
def PrintLengkap():
    print('''
--------------------------Daftar Lengkap Stok Mobil Rental-----------------------
_________________________________________________________________________________''')
    print('|KODE MOBIL\t|MERK\t|TYPE\t|TAHUN\t|KATEGORI\t|STOK\t|HARGA SEWA\t|')
    for i in range(len(stokMobil)):
        print(f"|{stokMobil[i]['Kode Mobil']}\t\t|{stokMobil[i]['Merk']}\t|{stokMobil[i]['Type']}\t|{stokMobil[i]['Tahun']}\t|{stokMobil[i]['Kategori']}\t\t|{stokMobil[i]['Stok']}\t|{stokMobil[i]['Harga']}\t\t|")
    print('\n')


# Sort harga descending
def PrintSortHargaDesc():
    sortedHargaMobil = sorted(stokMobil, key=lambda k: k['Harga'], reverse=True)
    print('''
--------------------------Daftar Lengkap Stok Mobil Rental-----------------------
_________________________________________________________________________________''')
    print('|KODE MOBIL\t|MERK\t|TYPE\t|TAHUN\t|KATEGORI\t|STOK\t|HARGA SEWA\t|')
    for i in range(len(sortedHargaMobil)):
        print(f"|{sortedHargaMobil[i]['Kode Mobil']}\t\t|{sortedHargaMobil[i]['Merk']}\t|{sortedHargaMobil[i]['Type']}\t|{sortedHargaMobil[i]['Tahun']}\t|{sortedHargaMobil[i]['Kategori']}\t\t|{sortedHargaMobil[i]['Stok']}\t|{sortedHargaMobil[i]['Harga']}\t\t|")
    print('\n')

# Sort harga ascending
def sortHargaAsc(h):
    return h['Harga']

# Daftar stok saja
def PrintStok():
    print('''
---------Daftar Stok Mobil Rental--------
_________________________________________''')
    print('|KODE MOBIL\t|MERK\t|TYPE\t|STOK\t|')
    for i in range(len(stokMobil)):
        print(f"|{stokMobil[i]['Kode Mobil']}\t\t|{stokMobil[i]['Merk']}\t|{stokMobil[i]['Type']}\t|{stokMobil[i]['Stok']}\t|")
    print('\n')

# Sort stok descending
def PrintSortStokDesc():
    sortedStokMobil = sorted(stokMobil, key=lambda k: k['Stok'], reverse=True)
    print('''
---------Daftar Stok Mobil Rental--------
_________________________________________''')
    print('|KODE MOBIL\t|MERK\t|TYPE\t|STOK\t|')
    for i in range(len(sortedStokMobil)):
        print(f"|{sortedStokMobil[i]['Kode Mobil']}\t\t|{sortedStokMobil[i]['Merk']}\t|{sortedStokMobil[i]['Type']}\t|{sortedStokMobil[i]['Stok']}\t|")
    print('\n')

# Sort stok ascending
def sortStokAsc(s):
    return s['Stok']

# Validasi Menu 2 alphanumeric
def validasiKodeNew(in1):
    if in1[1].isalpha() and in1[-1].isdigit():
        return True
    else:
        print('Masukan hanya alphanumerik')

# Validasi Menu 2 duplikasi kode
def validasiKodeMobilBaru(in1):
    for i in range(len(stokMobil)):
        checker = stokMobil[i]['Kode Mobil']
        if checker == in1:
            print('Kode mobil sudah dipakai, masukan kode yang berbeda!')
            return False
    return True

# Tambah stok mobil
def TambahDaftar():
    print('-------------------------------------Before--------------------------------------')
    PrintLengkap()

    while True:    
        kodeNew = input('Masukan kode mobil baru : ').upper()
        if validasiKodeMobilBaru(kodeNew):
            if validasiKodeNew(kodeNew):
                break
    merkNew = input('Masukan merk mobil baru : ')
    typeNew = input('Masukan type mobil baru : ')
    tahunNew = input('Masukan tahun mobil baru : ')
    while True:
        try:
            kategoriNew = int(input('''Kategori Mobil:
    1] MPV
    2] SUV
    3] Sedan
    4] City
    5] Sport
    Masukan kategori mobil baru : '''))
            if kategoriNew == 1:
                kategoriNew = 'MPV'
                break
            elif kategoriNew == 2:
                kategoriNew = 'SUV'
                break
            elif kategoriNew == 3:
                kategoriNew = 'Sedan'
                break
            elif kategoriNew == 4:
                kategoriNew = 'City'
                break
            elif kategoriNew == 5:
                kategoriNew = 'Sport'
                break
            else:
                print('Masukan angka sesuai pilihan kategori')
        except ValueError:
            print('Masukan hanya angka!')
    stokNew = int(input('Masukan stok mobil baru : '))
    hargaNew = int(input('Masukan harga sewa mobil baru : '))
    print('\nPenambahan daftar mobil berhasil!')

    #Append into main list
    stokMobil.append({'Kode Mobil':kodeNew,'Merk':merkNew,'Type':typeNew,'Tahun':tahunNew,'Kategori':kategoriNew,'Stok':stokNew,'Harga':hargaNew})
    
    #Daftar setelah penambahan
    print('--------------------------------------After--------------------------------------')
    PrintLengkap()

# Validasi duplikasi hapus menu 3
def ValidasiDupDel(in1):
    for i in stokMobil:
        if i['Kode Mobil'] == in1:
            break
    else:
        print('Kode mobil tidak ada dalam daftar')
        return True
            

# Hapus daftar mobil
def HapusDaftar(in1):
    for i in range(len(stokMobil)):
        checker = stokMobil[i]['Kode Mobil']
        if checker == in1:
            finalDel = i
            while True:
                delConfirmation = input('Apakah anda yakin ingin menghapus mobil? (Y/N): ').upper()
                if delConfirmation == 'N':
                    print('Penghapusan data dibatalkan')
                    break
                elif delConfirmation == 'Y':
                    del stokMobil[finalDel]
                    print(f'Penghapusan kode mobil {in1} berhasil\n')
                    #Daftar setelah penghapusan daftar
                    print('--------------------------------------After--------------------------------------')
                    PrintLengkap()
                    break
                else:
                    print('Hanya masukan jawaban Y/N')
            break

# Validasi duplikasi hapus menu 4.1 dan 4.2
def ValidasiDupUpd(in1):
    for i in stokMobil:
        if i['Kode Mobil'] == in1:
            break
    else:
        print('Kode mobil tidak ada dalam daftar')
        return True

# Update stok mobil menu 4.1
def UpdateStok(in1,in2):
    ValidasiDupUpd(in1)
    for i in range(len(stokMobil)):
        checker = stokMobil[i]['Kode Mobil']
        if checker == in1:
            finalUpdS = i
            while True:
                delConfirmation = input('Apakah anda yakin ingin update stok mobil? (Y/N): ').upper()
                if delConfirmation == 'N':
                    print('Update stok dibatalkan')
                    break
                elif delConfirmation == 'Y':
                    stokMobil[finalUpdS]['Stok'] = in2
                    print(f'Update stok kode mobil {in1} berhasil\n')
                    #Daftar setelah update stok
                    print('--------------------------------------After--------------------------------------')
                    PrintLengkap()
                    break
                else:
                    print('Hanya masukan jawaban Y/N')
            break


# Update harga sewa mobil menu 4.2
def UpdateHarga(in1,in2):
    ValidasiDupUpd(in1)
    for i in range(len(stokMobil)):
        checker = stokMobil[i]['Kode Mobil']
        if checker == in1:
            finalUpdH = i
            while True:
                delConfirmation = input('Apakah anda yakin ingin update harga sewa mobil? (Y/N): ').upper()
                if delConfirmation == 'N':
                    print('Update harga sewa dibatalkan')
                    break
                elif delConfirmation == 'Y':
                    stokMobil[finalUpdH]['Harga'] = in2
                    print(f'Update harga sewa kode mobil {in1} berhasil\n')
                    #Daftar setelah update harga sewa
                    print('--------------------------------------After--------------------------------------')
                    PrintLengkap()
                    break
                else:
                    print('Hanya masukan jawaban Y/N')
            break

# PROGRAM START
while True:
    try:
        MainMenu()
        if menu == 1:
            while True:    
                try:
                    SubMenu()
                    if subMbenu == 3: # Kembali ke Main menu
                        break
                    elif subMbenu == 2: # Daftar stok saja
                        PrintStok()
                        sortMenu1 = int(input('Sorting Stok:\n1. Tertinggi\n2. Terendah\n3. Kembali\nMasukan menu sorting : '))
                        if sortMenu1 == 2:
                            stokMobil.sort(key=sortStokAsc)
                            PrintStok()
                        elif sortMenu1 == 1:
                            PrintSortStokDesc()
                        elif sortMenu1 == 3:
                            break
                        else:
                            print('Masukan Hanya Angka Menu!') 
                    elif subMbenu == 1: # Daftar mobil lengkap
                        PrintLengkap()
                        sortMenu2 = int(input('Sorting Harga:\n1. Tertinggi\n2. Terendah\n3. Kembali\nMasukan menu sorting : \n'))
                        if sortMenu2 == 2:
                            stokMobil.sort(key=sortHargaAsc)
                            PrintLengkap()
                        elif sortMenu2 == 1:
                            PrintSortHargaDesc()
                        elif sortMenu2 == 3:
                            break
                        else:
                            print('Masukan Hanya Angka Menu!') 
                    else:
                        print('Masukan Hanya Angka Menu!')
                except ValueError:
                    print('Masukan Hanya Angka Menu!')
        elif menu == 2:
            TambahDaftar()
        elif menu == 3:
            #Daftar sebelum penghapusan daftar
            print('-------------------------------------Before--------------------------------------')
            PrintLengkap()
            while True:
                kodeDel = input('Masukan kode mobil yang ingin dihapus : ').upper()
                if ValidasiDupDel(kodeDel):
                    continue
                HapusDaftar(kodeDel)
                break
        elif menu == 4:
            while True:
                try:
                    subMenu4 = int(input('''Submenu Update:
    1] Update Stok Mobil
    2] Update Harga Sewa Mobil
    3] Kembali ke Menu Utama
    Masukan pilihan update : '''))
                    if subMenu4 == 1:
                        #Daftar sebelum update stok mobil
                        print('-------------------------------------Before--------------------------------------')
                        PrintLengkap()
                        while True:
                            kodeUpdateStok = input('Masukan kode mobil : ').upper()
                            stokUpdate = int(input('Masukan update stok : '))
                            if ValidasiDupUpd(kodeUpdateStok):
                                continue
                            UpdateStok(kodeUpdateStok,stokUpdate)
                            break
                    elif subMenu4 == 2:
                        #Daftar sebelum update harga sewa mobil
                        print('-------------------------------------Before--------------------------------------')
                        PrintLengkap()
                        while True:
                            kodeUpdateHarga = input('Masukan kode mobil : ').upper()
                            hargaUpdate = int(input('Masukan update harga : '))
                            if ValidasiDupUpd(kodeUpdateHarga):
                                continue
                            UpdateHarga(kodeUpdateHarga,hargaUpdate)
                            break
                    elif subMenu4 == 3:
                        break
                    else:
                        print('Masukan Hanya Angka Menu!') 
                except ValueError:
                    print ('Masukan Hanya Angka Menu!')
        elif menu == 5:
            break
        elif menu != 1 or menu != 2 or menu != 3 or menu != 4 or menu != 5:
            print('Masukan angka menu yang sesuai!')
    except ValueError:
        print('Masukan Hanya Angka Menu!')


# Note : Masih dalam pengerjaan untuk menu 4 dan fitur lainnya