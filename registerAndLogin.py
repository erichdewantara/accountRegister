database = {}

dictGender = {
    1: "Pria",
    2: "Wanita"
}

def validate_userid(user_id):
    if len(user_id) < 6 or len(user_id) > 20:
        print("UserID harus terdiri dari 6-20 karakter!")
        return False
    
    if not any(char.isdigit() for char in user_id) or not any(char.isalpha() for char in user_id):
        print("UserID harus kombinasi huruf dan angka!")
        return False
    
    for char in user_id:
        if not char.isalnum():
            print("UserID hanya boleh berisi huruf dan angka!")
            return False
    
    if user_id in database:
        print("UserID sudah terdaftar!")
        return False
    
    return True

def validate_password(password):
    if len(password) < 8:
        print("Password minimal 8 karakter!")
        return False
    
    has_upper = has_lower = has_digit = has_special = False
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in "/.,@#$%":
            has_special = True

    if not has_upper:
        print("Password harus mengandung huruf kapital!")
        return False
    if not has_lower:
        print("Password harus mengandung huruf kecil!")
        return False
    if not has_digit:
        print("Password harus mengandung angka!")
        return False
    if not has_special:
        print("Password harus mengandung karakter khusus!\ne.g. /.,@#$%)")
        return False
    
    return True

def validate_email(email):
    def username():
        store = ""
        # split by "@", get element[0]
        name = email.split("@")[0]

        # condition2; user diawali alfanumerik
        if name[0].isalnum():
            for char in name:
                # condition1; user adalah huruf, angka, underscore, dot
                if char.isalnum() or char == "_" or char == ".":
                    store += char
                else:
                    return f"Format username salah, mengandung \"{char}\"!"
        else:
            return "Format username salah, harus diawali huruf atau angka!"
        
        return store

    def hosting():
        # condition6; @ hanya 1
        if email.count("@") != 1:
            return "Format email salah, masukkan hosting dan/atau hosting hanya boleh 1!"
        else:
            store = "@"
            # split by "@", get element[1]; split by ".", get element[0]
            host = email.split("@")[1].split(".")[0]

            # condition3; hosting alfanumerik
            for char in host:
                if char.isalnum():
                    store += char
                else:
                    return f"Format hosting salah, mengandung \"{char}\"!"
                
            return store
    
    def extension():
        store = "."
        # split by "@", get element[0]
        fullExtension = email.split("@")[1].split(".")[1:]
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        if len(fullExtension) == 0 or fullExtension[0] == "":
            return "Format email salah, masukkan ekstensi!"
        # condition78; 2 ekstensi
        elif len(fullExtension) > 2:
            return "Format ekstensi salah, maksimal 2 ekstensi!"
        else:
            # extension pertama
            extension1 = fullExtension[0]

            #condition4; varchar(5)
            if len(extension1) <= 5:
                for char in extension1:
                    #condition4; ekstensi alfa
                    if char in alphabet:
                        store += char
                    else:
                        return f"Format ekstensi salah, mengandung \"{char}\"!"
            else:
                return "Format ekstensi salah, melebihi 5 karakter!"

            # extension kedua
            if len(fullExtension) > 1:
                store += "."
                extension2 = fullExtension[1]
                if len(extension2) <= 5:
                    for char in extension2:
                        if char in alphabet:
                            store += char
                        else:
                            return f"Format ekstensi salah, mengandung \"{char}\"!"
                else:
                    return "Format ekstensi salah, melebihi 5 karakter!"
            
            return store
    
    a = username()
    aValue = email.split("@")[0]
    b = hosting()
    bValue = "@" + email.split("@")[1].split(".")[0]
    c = extension()
    cValue = "." + ".".join(email.split("@")[1].split(".")[1:])

    if a != aValue:
        print(a)
    elif b != bValue:
        print(b)
    elif c != cValue:
        print(c)
    
    return True

def validate_name(name):
    if not all(char.isalpha() or char == " " for char in name):
        print("Nama hanya boleh berisi alfabet!")
        return False
    return True

def validate_age(age):
    if not age.isdigit():
        print("Usia harus berupa angka!")
        return False
    
    if not (17 <= int(age) <= 80):
        print("Usia harus antara 17 hingga 80 tahun!")
        return False
    
    return True

def validate_job(job):
    if not all(char.isalpha() or char == " " for char in job):
        print("Pekerjaan hanya boleh berisi alfabet!")
        return False
    return True

def validate_hobby(hobby):
    hobbies = [item.strip() for item in hobby.split(",")]

    if len(hobbies) < 2:
        print("Hobi harus lebih dari satu!")
        return False
    
    for word in hobbies:
        if not all(char.isalpha() or char.isspace() for char in word):
            print("Hobi hanya boleh berisi alfabet!")
            return False
        
    return True

def validate_address_city(city):
    if not all(char.isalpha() or char == " " for char in city):
        print("Nama kota hanya boleh berisi alfabet!")
        return False
    return True

def validate_address_zipcode(zipcode):
    if not zipcode.isdigit():
        print("Kode pos harus berupa angka!")
        return False
    
    if len(zipcode) != 5:
        print("Kode pos harus 5 digit!")
        return False
    
    return True

def validate_phone(phone):
    if not phone.isdigit():
        print("Nomor HP harus berupa angka!")
        return False
    
    if not (11 <= len(phone) <= 13):
        print("Nomor HP harus berisi 11-13 angka!")
        return False
    
    return True

def register():
    print('Masukkan data Anda...')
    while True: # user id
        user_id = input('Masukkan User ID: ')
        if validate_userid(user_id):
            break

    while True: # password
        password = input("Masukkan password: ")
        if validate_password(password):
            break

    while True: # email
        email = input("Masukkan email: ").lower()
        if validate_email(email):
            break

    while True: # nama
        name = input("Masukkan nama: ").title()
        if validate_name(name):
            break
    
    while True: # jenis kelamin
        try:
            print("Gender:\n1. Pria\n2. Wanita")
            gender = int(input("Masukkan gender: "))
            for key, val in dictGender.items():
                if key == gender:
                    gender = val
            break
        except ValueError:
            print("Hanya menerima input angka")

    while True: # umur
        age = input("Masukkan usia: ")
        if validate_age(age):
            break

    while True: # pekerjaan
        job = input("Masukkan pekerjaan: ").title()
        if validate_job(job):
            break

    while True: # hobi
        hobby = input("Masukkan hobi: ").capitalize()
        if validate_hobby(hobby):
            break

    print("Alamat: ")
    while True: # kota
        city = input("Masukkan nama kota: ").title()
        if validate_address_city(city):
            break
        
    while True: # rt
        try:
            rt = int(input("Masukkan RT: "))
            break
        except ValueError:
            print("RT harus berupa integer")

    while True: # rw
        try:
            rw = int(input("Masukkan RW: "))
            break
        except ValueError:
            print("RW harus berupa integer")

    while True: # kode pos
        zipcode = input("Masukkan kode pos: ")
        if validate_address_zipcode(zipcode):
            break

    print("Geo: ")
    while True: # latitude
        try:
            lat = float(input("Masukkan latitude: "))
            break
        except ValueError:
            print("Latitude harus berupa float")

    while True: # longitude
        try:
            long = float(input("Masukkan longitude: "))
            break
        except ValueError:
            print("Longitude harus berupa float")

    while True: # nomor hp
        phone = input("Masukkan nomor HP: ")
        if validate_phone(phone):
            break

    while True:
        save = input("Simpan data? (Y/N) ").lower()
        if save == "n":
            print("Data tidak disimpan")
            main_menu()
        elif save == "y":
            database[user_id] = {
                'password': password,
                'email': email,
                'name': name,
                'gender': gender,
                'age': int(age),
                'job': job,
                'hobby': hobby,
                'address': {
                    'city': city,
                    'rt': rt,
                    'rw': rw,
                    'zipcode': zipcode,
                    'geo': {
                        'lat': lat,
                        'long': long
                    }
                },
                'phone': phone
            }
            print("Data berhasil disimpan!")
            main_menu()
        else:
            print("Hanya menerima input Y/N")

def login():
    while True:
        user_id = input("Masukkan User ID: ")
        if user_id not in database:
            print("User ID tidak terdaftar!")
        else:
            attempts = 0
            while attempts < 6:
                password = input("Masukkan password: ")
                if database[user_id]['password'] == password:
                    print("\nAnda Berhasil Login!\n")

                    user_data = database[user_id]
                    print(f"Nama: {user_data['name']}")
                    print(f"Email: {user_data['email']}")
                    print(f"Gender: {user_data['gender']}")
                    print(f"Usia: {user_data['age']}")
                    print(f"Pekerjaan: {user_data['job']}")
                    print(f"Hobi: {user_data['hobby']}")
                    print(f"Alamat: {user_data['address']['city']}")
                    print(f"RT: {user_data['address']['rt']}")
                    print(f"RW: {user_data['address']['rw']}")
                    print(f"Kode Pos: {user_data['address']['zipcode']}")
                    print(f"Geo:\nLat {user_data['address']['geo']['lat']}, Long {user_data['address']['geo']['long']}")
                    print(f"Nomor HP: {user_data['phone']}")

                    main_menu()
                else:
                    print("Password salah!")
                    print(f"Sisa percobaan: {4 - attempts}")
                    attempts += 1
                    if attempts == 5:
                        print("Percobaan habis! Gagal login.")
                        main_menu()


def main_menu():
    while True:
        try:
            print('### Selamat datang di Team 4 Apps ###')
            print('1. Register')
            print('2. Login')
            print('3. Exit')
            choice = int(input('Masukkan pilihan: '))

            if choice == 1:
                register()
            elif choice == 2:
                login()
            elif choice == 3:
                print('Terima kasih, bye-bye~')
                exit()
            else:
                print('Input Anda tidak valid!')
        except ValueError:
            print('Input Ada tidak valid!')

main_menu()