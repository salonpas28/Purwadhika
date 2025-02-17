from tabulate import tabulate

daftar_mobil = [
    { 
        'id': '2',
        'manufakturer': 'Honda',
        'nama_mobil': 'Crv',
        'tahun': '2015',
        'penggerak_roda' : 'ban depan',
        'jumlah_jok': '5',
        'status': 'tersedia'
    },
    { 
        'id': '1',
        'manufakturer': 'Toyota',
        'nama_mobil': 'Avanza',
        'tahun': '2017',
        'penggerak_roda' : 'ban belakang',
        'jumlah_jok': '7',
        'status': 'disewa'
    },
    { 
        'id': '3',
        'manufakturer': 'Nissan',
        'nama_mobil': 'X-Trail',
        'tahun': '2019',
        'penggerak_roda' : 'ban depan',
        'jumlah_jok': '7',
        'status': 'tersedia'
    },
    { 
        'id': '4',
        'manufakturer': 'Ford',
        'nama_mobil': 'Escape',
        'tahun': '2020',
        'penggerak_roda' : 'semua ban',
        'jumlah_jok': '5',
        'status': 'disewa'
    },
    { 
        'id': '5',
        'manufakturer': 'Mazda',
        'nama_mobil': 'Cx-5',
        'tahun': '2022',
        'penggerak_roda' : 'ban depan',
        'jumlah_jok': '5',
        'status': 'tersedia'
    },
    { 
        'id': '6',
        'manufakturer': 'Kia',
        'nama_mobil': 'Sportage',
        'tahun': '2018',
        'penggerak_roda' : 'semua ban',
        'jumlah_jok': '5',
        'status': 'disewa'
    },
    { 
        'id': '7',
        'manufakturer': 'Hyundai',
        'nama_mobil': 'Tucson',
        'tahun': '2021',
        'penggerak_roda' : 'ban depan',
        'jumlah_jok': '5',
        'status': 'tersedia'
    },
    { 
        'id': '8',
        'manufakturer': 'Chevrolet',
        'nama_mobil': 'Trailblazer',
        'tahun': '2023',
        'penggerak_roda':'semua ban',
        'jumlah_jok': '7',
        'status': 'disewa'
    },
    { 
        'id': '9',
        'manufakturer': 'Subaru',
        'nama_mobil': 'Forester',
        'tahun': '2016',
        'penggerak_roda' : 'semua ban',
        'jumlah_jok': '5',
        'status': 'tersedia'
    },
    { 
        'id': '10',
        'manufakturer': 'Volkswagen',
        'nama_mobil': 'Tiguan',
        'tahun': '2025',
        'penggerak_roda' : 'ban depan',
        'jumlah_jok': '5',
        'status': 'tersedia'
    }
]

daftar_mobil_hapus = []

def guard_int(x, min, max):
    if not x.isdigit():
            print('')
            print('Input salah, anda tidak memasukkan angka!.')
    elif x.isdigit():
        x = int(x)
        if x < min or x > max:
            print('')
            print('Anda memasukkan angka yang tidak ada di sistem!')
        else:
            return x
 
def keluar():
    print('Sampai jumpa kembali di Rent-all!')
    print('')

def menu_utama():
        print('Selamat datang di rental mobil, Rent-all!')
        while True:
            print('')
            print('Main Menu:')
            print('1. Lihat daftar mobil')
            print('2. Penambahan daftar mobil')
            print('3. Pembaruan daftar mobil')
            print('4. Penghapusan daftar mobil')
            print('5. Keluar program')
            print('')
            opsi_main = input('Silahkan masukkan nomor opsi main menu (1-5): ')
            opsi_main = guard_int(opsi_main, 1, 5)
            if opsi_main == 1:
                tampil_daftar_mobil()
            elif opsi_main == 2:
                tambah_daftar_mobil()
            elif opsi_main == 3:
                pembaruan_daftar_mobil()
            elif opsi_main == 4:
                penghapusan_daftar_mobil()
            elif opsi_main == 5:
                keluar()
                break

def tampil_daftar_mobil():
    while True:
        print('')
        print('Menu tampilan:')
        print('1. Lihat semua daftar mobil')
        print('2. Lihat daftar mobil menggunakan id')
        print('3. Lihat daftar mobil dengan filter lainnya')
        print('4. Lihat daftar mobil hapus')
        print('5. Sortir id daftar mobil')
        print('6. Keluar ke main menu')
        print('')
        opsi_tampil = input('Silahkan masukkan nomor opsi tampilan (1-6): ')
        opsi_tampil = guard_int(opsi_tampil, 1, 6)
        if opsi_tampil == 1:
            print('')
            tampilin_mobil()
        elif opsi_tampil == 2:
            print('')
            tampilin_mobil_id()
        elif opsi_tampil == 3:
            print('')
            tampilin_mobil_filter()
        elif opsi_tampil == 4:
            print('')
            try:
                tampilin_mobil_hapus()
            except ValueError:
                print('Belum ada data dalam daftar mobil hapus!')
        elif opsi_tampil == 5:
            print('')
            sortir_daftar_mobil(daftar_mobil)
        elif opsi_tampil == 6:
            break
    
def tampilin_mobil():
    if not daftar_mobil:
        print('')
        print('+----------------------------------!!!Daftar Mobil Kosong!!!-----------------------------------+')
        print('')
        print(f"{tabulate(daftar_mobil, headers=['id', 'manufakturer', 'nama_mobil', 'tahun', 'penggerak_roda','jumlah_jok', 'status'], tablefmt='grid')}")
    else:
        data = []
        for mobil in daftar_mobil:
            data.append([
                mobil['id'], 
                mobil['manufakturer'],
                mobil['nama_mobil'],  
                mobil['tahun'],
                mobil['penggerak_roda'],
                mobil['jumlah_jok'],
                mobil['status']  
            ])
        print('')
        print('+--------------------------------------- Daftar Mobil ----------------------------------------+')
        print('')
        print(f"{tabulate(data, headers=['id', 'manufakturer', 'nama_mobil', 'tahun', 'penggerak_roda','jumlah_jok', 'status'], tablefmt='grid')}")

def tampilin_mobil_id():
    while True:
        id_choose = input('Silahkan masukkan id yang ingin ditampilkan: ')
        id_choose = str(id_choose)
        for mobil in daftar_mobil:
            if id_choose == mobil['id']:
                data_1  = []
                data_1.append([
                mobil['id'],    
                mobil['manufakturer'],
                mobil['nama_mobil'],  
                mobil['tahun'],
                mobil['penggerak_roda'],
                mobil['jumlah_jok'],
                mobil['status']   
                ])
                print('')
                print('+--------------------------------------- Daftar Mobil ----------------------------------------+')
                print('')
                print(f"{tabulate(data_1, headers=['id', 'manufakturer', 'nama_mobil', 'tahun', 'penggerak_roda','jumlah_jok', 'status'], tablefmt='grid')}")
                print()
                break
        else:
            print('')
            print('data tidak ditemukan')
            break
        break

def tampilin_mobil_filter():
    while True:
        print('')
        print('Menu Opsi Filter:')
        print('1. Filter berdasarkan jumlah jok')
        print('2. Filter berdasarkan mobil yang tersedia')
        print('3. Filter berdasarkan tahun')
        print('4. Filter berdasarkan ban penggerak')
        print('')
        opsi_filter = input('Masukkan pilihan opsi filter mobil (1-4): ')
        opsi_filter = guard_int(opsi_filter, 1, 4)
        if opsi_filter == 1:
            tampilin_mobil_filter_jok()
            break
        elif opsi_filter == 2:
            tampilin_mobil_filter_tersedia()
            break
        elif opsi_filter == 3:
            tampilin_mobil_filter_tahun()
            break
        elif opsi_filter == 4:
                tampilin_mobil_filter_ban_penggerak()
                break
                    
def tampilin_mobil_filter_jok():
    while True:
        print('')
        print('Daftar jumlah jok:')
        print('1. 5 seater')
        print('2. 7 seater')
        print('')
        opsi_jok = input('Silahkan pilih jumlah jok yang diinginkan (1-2): ')
        opsi_jok = guard_int(opsi_jok, 1, 2)
        if opsi_jok == 1:
            data = []
            for mobil in daftar_mobil:
                if mobil['jumlah_jok'] == '5':
                    data.append([
                    mobil['id'], 
                    mobil['manufakturer'],
                    mobil['nama_mobil'],  
                    mobil['tahun'],
                    mobil['penggerak_roda'],
                    mobil['jumlah_jok'],
                    mobil['status']   
                    ])
            print('')
            print('+--------------------------------------- Daftar Mobil ----------------------------------------+')
            print('')
            print(f"{tabulate(data, headers=['id', 'manufakturer', 'nama_mobil', 'tahun', 'penggerak_roda','jumlah_jok', 'status'], tablefmt='grid')}")
            print()
            break
        elif opsi_jok == 2:
            data = []
            for mobil in daftar_mobil:
                if mobil['jumlah_jok'] == '7':
                    data.append([
                    mobil['id'], 
                    mobil['manufakturer'],
                    mobil['nama_mobil'],  
                    mobil['tahun'],
                    mobil['penggerak_roda'],
                    mobil['jumlah_jok'],
                    mobil['status']   
                    ])
            print('')
            print('+--------------------------------------- Daftar Mobil ----------------------------------------+')
            print('')
            print(f"{tabulate(data, headers=['id', 'manufakturer', 'nama_mobil', 'tahun', 'penggerak_roda','jumlah_jok', 'status'], tablefmt='grid')}")
            print()
            break
        else:
            print('Silahkan input ulang kembali.')

def tampilin_mobil_filter_ban_penggerak():
    while True:
        print('')
        print('Daftar ban penggerak:')
        print('1. ban depan')
        print('2. ban belakang')
        print('3. semua ban')
        print('')
        opsi_jok = input('Silahkan pilih jumlah jok yang diinginkan (1-3): ')
        opsi_jok = guard_int(opsi_jok, 1, 3)
        if opsi_jok == 1:
            data = []
            for mobil in daftar_mobil:
                if mobil['penggerak_roda'] == 'ban depan':
                    data.append([
                    mobil['id'], 
                    mobil['manufakturer'],
                    mobil['nama_mobil'],  
                    mobil['tahun'],
                    mobil['penggerak_roda'],
                    mobil['jumlah_jok'],
                    mobil['status']   
                    ])
            print('')
            print('+--------------------------------------- Daftar Mobil ----------------------------------------+')
            print('')
            print(f"{tabulate(data, headers=['id', 'manufakturer', 'nama_mobil', 'tahun', 'penggerak_roda','jumlah_jok', 'status'], tablefmt='grid')}")
            print()
            break
        elif opsi_jok == 2:
            data = []
            for mobil in daftar_mobil:
                if mobil['penggerak_roda'] == 'ban belakang':
                    data.append([
                    mobil['id'], 
                    mobil['manufakturer'],
                    mobil['nama_mobil'],  
                    mobil['tahun'],
                    mobil['penggerak_roda'],
                    mobil['jumlah_jok'],
                    mobil['status']   
                    ])
            print('')
            print('+--------------------------------------- Daftar Mobil ----------------------------------------+')
            print('')
            print(f"{tabulate(data, headers=['id', 'manufakturer', 'nama_mobil', 'tahun', 'penggerak_roda','jumlah_jok', 'status'], tablefmt='grid')}")
            print()
            break
        elif opsi_jok == 3:
            data = []
            for mobil in daftar_mobil:
                if mobil['penggerak_roda'] == 'semua ban':
                    data.append([
                    mobil['id'], 
                    mobil['manufakturer'],
                    mobil['nama_mobil'],  
                    mobil['tahun'],
                    mobil['penggerak_roda'],
                    mobil['jumlah_jok'],
                    mobil['status']   
                    ])
            print('')
            print('+--------------------------------------- Daftar Mobil ----------------------------------------+')
            print('')
            print(f"{tabulate(data, headers=['id', 'manufakturer', 'nama_mobil', 'tahun', 'penggerak_roda','jumlah_jok', 'status'], tablefmt='grid')}")
            print()
            break
        else:
            print('Silahkan input ulang kembali.')

def tampilin_mobil_filter_tersedia():
    data = []
    for mobil in daftar_mobil:
        if mobil['status'] == 'tersedia':
            data.append([
                mobil['id'], 
                mobil['manufakturer'],
                mobil['nama_mobil'],  
                mobil['tahun'],
                mobil['penggerak_roda'],
                mobil['jumlah_jok'],
                mobil['status']  
            ])
    print('')
    print('+--------------------------------------- Daftar Mobil ----------------------------------------+')
    print('')
    print(f"{tabulate(data, headers=['id', 'manufakturer', 'nama_mobil', 'tahun', 'penggerak_roda','jumlah_jok', 'status'], tablefmt='grid')}")
    print()

def tampilin_mobil_filter_tahun():
    data = []
    data_tahun = []
    for mobil in daftar_mobil:
        data_tahun.append(mobil['tahun'])
    data_tahun.sort()
    print('')
    print(f'daftar tahun mobil:')
    print('')
    print(*data_tahun)
    print('')
    while True:
        opsi_tahun = input('Silahkan masukkan angka tahun dari daftar mobil kami: ')
        opsi_tahun = guard_int(opsi_tahun, 2015, 2025)
        if type(opsi_tahun) == int:
            opsi_tahun = str(opsi_tahun)
            for mobil in daftar_mobil:
                if opsi_tahun in mobil['tahun']:
                    data.append([
                        mobil['id'], 
                        mobil['manufakturer'],
                        mobil['nama_mobil'],  
                        mobil['tahun'],
                        mobil['penggerak_roda'],
                        mobil['jumlah_jok'],
                        mobil['status']  
                    ])
                    print('')
                    print('+--------------------------------------- Daftar Mobil ----------------------------------------+')
                    print('')
                    print(f"{tabulate(data, headers=['id', 'manufakturer', 'nama_mobil', 'tahun', 'penggerak_roda','jumlah_jok', 'status'], tablefmt='grid')}")
                    print()
                    break
            break

def tampilin_mobil_hapus():
    if not daftar_mobil_hapus:
        print('Daftar mobil hapus kosong!')
    else:
        data = []
        for mobil in daftar_mobil_hapus:
            data.append([
                mobil['id'], 
                mobil['manufakturer'],
                mobil['nama_mobil'],  
                mobil['tahun'],
                mobil['penggerak_roda'],
                mobil['jumlah_jok'],
                mobil['status']  
            ])
        print('')
        print('+------------------------------------ Daftar Mobil Hapus -------------------------------------+')
        print('')
        print(f"{tabulate(data, headers=['id', 'manufakturer', 'nama_mobil', 'tahun', 'penggerak_roda','jumlah_jok', 'status'], tablefmt='grid')}")
        print()

def sortir_daftar_mobil(dict):
    dict.sort(key=lambda x: int(x['id']))
    print('')
    print('Sortir sukses!')
    tampilin_mobil()

def tambah_daftar_mobil():
    while True:
        print('Menu penambahan:')
        print('1. Tambah daftar mobil baru')
        print('2. keluar ke main menu')
        print('')
        opsi_pembuatan = str(input('Silahkan masukkan pilihan opsi penambahan data mobil: '))
        if opsi_pembuatan == '1':
            print('')
            print('Silahkan masukkan informasi-informasi yang dibutuhkan')
            print('')
            while True:
                id_list = []
                for mobil in daftar_mobil:
                        id_list.append(mobil['id'])
                if not id_list:
                    print('Belum ada id yang terdaftar')
                    print('')
                else:
                    print(f'Id yang sudah terdaftar: {tuple(id_list)}')
                    print('')
                id = input('Silahkan masukkan id yang ingin ditambahkan (angka): ')
                id = guard_int(id,1,100)
                if type(id) == int:
                    id = str(id)
                    if id in id_list:
                        print('')
                        print('Id sudah ada, silahkan input id yang berbeda')
                        break
                    else:
                        print('Data id tersimpan!')
                        print('')    
                    while True:         
                        try:
                            manufakturer = str(input('Silahkan masukkan nama manufakturer mobil: '))
                        except ValueError:
                            print('input tidak valid silahkan coba lagi')
                            print('')
                        finally:
                            manufakturer = manufakturer.capitalize()
                            print('data manufakturer tersimpan!')
                            print('')
                            break
                while True:
                    try:
                        nama_mobil = str(input('Silahkan masukkan nama mobil: '))
                    except ValueError:
                        print('input tidak valid silahkan coba lagi')
                    finally:
                        nama_mobil = nama_mobil.capitalize()
                        print('data nama mobil tersimpan!')
                        print('')
                        break
                while True:
                    tahun = input('Silahkan masukkan tahun mobil (2015-2025): ')
                    tahun = guard_int(tahun, 2015, 2025)
                    if type(tahun) == int:
                        print('data tahun tersimpan!')
                        print('')
                        break
                    else:
                        print('Anda tidak memasukkan angka tahun dengan benar. silahkan masukkan kembai')
                while True:
                    penggerak_roda = str(input('Masukkan penggerak roda mobil (ban depan, ban belakang, atau semua ban): '))
                    if penggerak_roda == 'ban depan' or penggerak_roda == 'ban belakang' or penggerak_roda == 'semua ban':
                        print('data penggerak roda mobil tersimpan!')
                        print('')
                        break
                    else:
                        print('Anda tidak memasukkan penggerak roda mobil dengan benar.')
                while True:
                    jumlah_jok = input('Masukkan jumlah jok (5 atau 7): ')
                    jumlah_jok = guard_int(jumlah_jok, 5, 7)
                    if jumlah_jok == 5 or jumlah_jok == 7:
                        print('data jumlah jok tersimpan!')
                        print('')
                        break
                    elif jumlah_jok == 6:
                        print('')
                        print('Silahkan masukkan angka 5 atau 7')
                        print('')
                while True:
                    try:
                        status = str(input('Masukkan status (tersedia/disewa): '))
                    except ValueError:
                        print('input tidak valid silahkan coba lagi')
                    finally:
                        if status == 'tersedia' or status == 'disewa':
                            print('data status tersimpan!')
                            print('')
                            break
                        else:
                            print('input salah, silahkan ketik tersedia atau disewa.')
                daftar_tambah_mobil = []
                daftar_tambah_mobil.append([
                    id,
                    manufakturer,
                    nama_mobil,
                    tahun,
                    penggerak_roda,
                    jumlah_jok,
                    status
                    ])
                print('')
                print('+--------------------------------------- Daftar Mobil ----------------------------------------+')
                print('')
                print(f"{tabulate(daftar_tambah_mobil, headers=['id', 'manufakturer', 'nama_mobil', 'tahun', 'penggerak_roda','jumlah_jok', 'status'], tablefmt='grid')}")
                print('')

                while True:
                    konfirmasi = str(input('Apakah anda yakin untuk menyimpan data baru ini dalam daftar mobil? y/n: '))
                    print('')
                    if konfirmasi == 'y':
                        daftar_mobil.append({
                            'id':id,
                            'manufakturer':manufakturer,
                            'nama_mobil':nama_mobil,
                            'tahun':tahun,
                            'penggerak_roda':penggerak_roda,
                            'jumlah_jok':jumlah_jok,
                            'status':status
                            })
                        print('')
                        print('Data berhasil di simpan di daftar mobil.')
                        tampilin_mobil()
                        break
                    elif konfirmasi == 'n':
                        print('Penambahan dibatalkan')
                        print('')
                        break
                    elif konfirmasi != 'n' or konfirmasi != 'y':
                        print('Input salah, silahkan ketik y/n')
                break
        elif opsi_pembuatan == '2':
            break

def pembaruan_daftar_mobil():
    while True:
        print('')
        print('Menu Pembaruan:')
        print('1. Pembaruan data')
        print('2. Keluar ke main menu')
        print('')
        pembaruan_opsi = input('Silahkan masukkan nomor opsi pembaruan (1-2): ')
        pembaruan_opsi = guard_int(pembaruan_opsi, 1, 2)
        if len(daftar_mobil) == 0 and pembaruan_opsi == 1:
            print('')
            print('Daftar mobil kosong!')
            break
        elif pembaruan_opsi == 1:
            id_list = []
            for mobil in daftar_mobil:
                id_list.append(mobil['id'])
            continue_pembaruan = None
            confirm = None
            column = None
            print('')
            print(f'Daftar id mobil yang terdaftar: {tuple(id_list)}')
            while True:
                print('')
                id_choose = str(input('Silahkan masukkan nomor id dari mobil yang anda ingin perbarui: '))
                new_val = None
                for mobil in daftar_mobil:
                    if id_choose == mobil['id']:
                        data = []
                        data.append([
                        mobil['id'], 
                        mobil['manufakturer'],
                        mobil['nama_mobil'],  
                        mobil['tahun'],
                        mobil['penggerak_roda'],
                        mobil['jumlah_jok'],
                        mobil['status']   
                        ])
                        print(f"{tabulate(data, headers=['id', 'manufakturer', 'nama_mobil', 'tahun', 'penggerak_roda','jumlah_jok', 'status'], tablefmt='grid')}")
                        print('')
                        while True:
                            continue_pembaruan = str(input('Apakah anda masih ingin melanjutkan untuk pembaruan? y/n: '))
                            if continue_pembaruan == 'n':
                                break
                            elif continue_pembaruan == 'y':
                                print('')
                                while True:
                                    column = str(input('Silahkan ketik kolom yang ingin di perbarui: '))
                                    if column not in mobil:
                                        print('')
                                        column = None
                                        print('Kolom yang anda masukkan tidak ada dalam daftar mobil')
                                        print('')
                                    elif column in mobil and column == 'id':
                                        column = None
                                        print('')
                                        print('Anda tidak bisa merubah id dari daftar mobil')
                                        print('')
                                    elif column in mobil and column != 'id' and mobil['id'] == id_choose:
                                        if column == 'manufakturer':
                                            while True:
                                                print('')
                                                new_val = input(f'Silahkan masukkan manufakturer baru untuk kolom {column}:')
                                                if new_val.isdigit():
                                                    print('manufakturer tidak bisa dalam bentuk angka')
                                                else:
                                                    str(new_val)
                                                    break
                                        elif column == 'nama_mobil':
                                            while True:
                                                print('')
                                                new_val = input(f'Silahkan masukkan nama mobil untuk kolom {column}: ')
                                                if new_val.isdigit():
                                                    print('nama mobil tidak bisa dalam bentuk angka')
                                                else:
                                                    str(new_val)
                                                    break
                                        elif column == 'tahun':
                                            while True:
                                                print('')
                                                new_val = input(f'Silahkan masukkan tahun baru untuk kolom {column}: ')
                                                new_val = guard_int(new_val, 2015, 2025)
                                                if type(new_val) == int: 
                                                    str(new_val)      
                                                    break
                                                else:
                                                    print('')
                                                    print('Tahun hanya bisa dari 2015 ke 2025')
                                        
                                        elif column == 'penggerak_roda':
                                            while True:
                                                print('Daftar penggerak roda:')
                                                print('1. ban depan')
                                                print('2. ban belakang')
                                                print('3. semua ban')
                                                new_val = input(f'Silahkan masukkan penggerak roda baru untuk kolom {column}: ')
                                                if new_val == 'ban depan' or new_val == 'ban belakang' or new_val == 'semua ban':
                                                    str(new_val)
                                                    break
                                                else:
                                                    print('')
                                                    print('Input salah, masukkan penggerak roda dengan benar (cth: ban depan)')  
                                        
                                        elif column == 'jumlah_jok':
                                            while True:
                                                print('')
                                                new_val = input(f'Silahkan masukkan jumlah jok baru untuk kolom {column}: ')
                                                new_val = guard_int(new_val, 5, 7)
                                                if new_val == 5 or new_val == 7:     
                                                    str(new_val)
                                                    break                      
                                                else:
                                                    print('')
                                                    print('Input salah, masukkan angka 5 atau 7')
                                        
                                        elif column == 'status':
                                            while True:
                                                print('')
                                                new_val = input(f'Silahkan masukkan status baru untuk kolom {column}: ')
                                                if new_val == 'tersedia' or new_val == 'disewa': 
                                                    str(new_val)    
                                                    break                      
                                                else:
                                                    print('')
                                                    print('Input salah, ketik: tersedia/disewa (cth: disewa)')
                                        print(f'Konfirmasi pembaruan data id: {id_choose}, kolom: {column}, dan value dari: {mobil[column]}, menjadi: {new_val}?')
                                        confirm = str(input(f'(y/n): '))
                                        print('')
                                        if confirm == 'y':
                                            mobil[column] = str(new_val)
                                            print('')
                                            print('Data updating...')
                                            tampilin_mobil()
                                            break
                                        elif confirm == 'n':
                                            break
                                        else:
                                            print('Input salah, silahkan ketik y atau n')
                                        break
                                    
                                break
                            else:
                                print('')
                                print('tolong masukkan y atau n')
                                print('')
                if (column != None and continue_pembaruan == 'y') or (continue_pembaruan == 'y' and confirm == 'y'):
                    print('')
                    print('Pembaruan selesai!')
                    break
                elif continue_pembaruan == 'y' and confirm == 'n':
                    print('Pembaruan dibatalkan')
                    break
                elif continue_pembaruan == 'n':
                    print('')
                    print('Pembaruan dibatalkan')
                    break
                elif continue_pembaruan != 'y' and continue_pembaruan != 'n' and new_val != None:
                    print('')
                    print('Tolong masukkan y atau n')
                elif not id_choose.isdigit() or new_val == None:
                    print('')
                    print('tolong masukkan id (angka) dengan benar')
        elif pembaruan_opsi == 2:
            break

def penghapusan_daftar_mobil():
    while True:
        print('')
        print('Menu Penghapusan:')
        print('1. Penghapusan dari daftar mobil')
        print('2. Keluar ke main menu')
        print('')
        opsi_penghapusan = input('Silahkan masukkan nomor opsi menu penghapusan (1-2): ')
        opsi_penghapusan = guard_int(opsi_penghapusan, 1, 2)
        if len(daftar_mobil) == 0 and opsi_penghapusan == 1:
            print('')
            print('Daftar mobil kosong!')
            break
        elif len(daftar_mobil) > 1 and opsi_penghapusan == 1:
            confirm_penghapusan = None
            tampilin_mobil()
            print('')
            penghapusan_id = input('Silahkan masukkan id dari daftar mobil yang akan di penghapusan: ')
            for mobil in daftar_mobil:
                if penghapusan_id == mobil['id']:
                    data = []
                    data.append([
                    mobil['id'], 
                    mobil['manufakturer'],
                    mobil['nama_mobil'],  
                    mobil['tahun'],
                    mobil['penggerak_roda'],
                    mobil['jumlah_jok'],
                    mobil['status']   
                    ])
                    print('')
                    print('Data dari Id yang anda pilih: ')
                    print('')
                    print('+--------------------------------------- Daftar Mobil ----------------------------------------+')
                    print(f"{tabulate(data, headers=['id', 'manufakturer', 'nama_mobil', 'tahun', 'penggerak_roda','jumlah_jok', 'status'], tablefmt='grid')}")
                    print('')   
                    while True:
                        print('Silahkan pilih opsi penghapusan berikut:')
                        print('')
                        print('1. Penghapusan keras (Data akan dihapus secara permanen)')
                        print('2. Penghapusan lembut (Data akan dihapus dari daftar mobil, namun disimpan dalam daftar mobil hapus)')
                        print('')
                        penghapusan_opsi = input('Silahkan masukkan nomor opsi penghapusan (1-2): ')
                        penghapusan_opsi = guard_int(penghapusan_opsi, 1, 2)
                        if penghapusan_opsi == 1:
                            print('')
                            confirm_penghapusan = str(input('Apakah anda yakin untuk menghapus data ini? (y/n): '))
                            if confirm_penghapusan == 'y':
                                daftar_mobil.remove(mobil)
                                print('')
                                print('Data sukses dihapus secara permanen')
                                tampilin_mobil()
                                break
                            elif confirm_penghapusan == 'n':
                                print('')
                                print('Penghapusan data dibatalkan')
                                break
                        elif penghapusan_opsi == 2:
                            print('')
                            while True:
                                confirm_penghapusan = str(input('Apakah anda yakin untuk menghapus data ini? (y/n): '))
                                if confirm_penghapusan == 'y':
                                    daftar_mobil_hapus.append({
                                    'id':mobil['id'],
                                    'manufakturer':mobil['manufakturer'],
                                    'nama_mobil':mobil['nama_mobil'],
                                    'tahun':mobil['tahun'],
                                    'penggerak_roda':mobil['penggerak_roda'],
                                    'jumlah_jok':mobil['jumlah_jok'],
                                    'status':mobil['status']
                                })
                                    daftar_mobil.remove(mobil)
                                    print('')
                                    print('Data sukses dihapus dari daftar mobil, dan dipindahkan ke daftar mobil hapus')
                                    tampilin_mobil()
                                    break
                                elif confirm_penghapusan == 'n':
                                    print('')
                                    print('Penghapusan data dibatalkan')
                                    break
                                else:
                                    print('tolong masukkan y atau n')
                            break
            if penghapusan_id not in mobil['id'] and confirm_penghapusan == None:
                print('')
                print('Id yang anda masukkan tidak ditemukan')
            elif penghapusan_id in mobil['id'] and confirm_penghapusan == 'n':
                print('')
                print('Penghapusan dibatalkan')
                break
        elif opsi_penghapusan == 2:
            break

# Mulai program
menu_utama()