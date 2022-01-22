#Import Brython
from browser import document, alert

# Deklarasi Variable
input1 = document['input1']
button = document['btn']
output = document['output']
selectType = document['pilih-tipe']
selectCalculated = document['select-calculated']

#Rumus uang
type1 = {'Dolar': {'Dolar': {'Current': lambda uang: uang, 'input1': 'Masukkan uang'},
                           'Rupiah': {'Current': lambda uang: uang * 14316.05, 'input1': 'Masukkan uang'},
                           'Riyal': {'Current': lambda uang: uang * 3.75, 'input1': 'Masukkan uang'},
                           'Won': {'Current': lambda uang: uang * 1188.98, 'input1': 'Masukkan uang'},
                           'Ringgit': {'Current': lambda uang: uang * 4.19, 'input1': 'Masukkan uang'},
                           'Yen': {'Current': lambda uang: uang * 113.67, 'input1': 'Masukkan uang'}},
        'Rupiah': {'Dolar': {'Current': lambda uang: uang * 0.000070 , 'input1': 'Masukkan uang'},
                           'Rupiah': {'Current': lambda uang: uang , 'input1': 'Masukkan uang'},
                           'Riyal': {'Current': lambda uang: uang * 0.00026, 'input1': 'Masukkan uang'},
                           'Won': {'Current': lambda uang: uang * 0.083, 'input1': 'Masukkan uang'},
                           'Ringgit': {'Current': lambda uang: uang * 0.00029, 'input1': 'Masukkan uang'},
                           'Yen': {'Current': lambda uang: uang * 0.0079, 'input1': 'Masukkan uang'}},
        'Riyal': {'Dolar': {'Current': lambda uang: uang * 0.27, 'input1': 'Masukkan uang'},
                           'Rupiah': {'Current': lambda uang: uang * 3815.21, 'input1': 'Masukkan uang'},
                           'Riyal': {'Current': lambda uang: uang , 'input1': 'Masukkan uang'},
                           'Won': {'Current': lambda uang: uang * 316.73, 'input1': 'Masukkan uang'},
                           'Ringgit': {'Current': lambda uang: uang * 1.12, 'input1': 'Masukkan uang'},
                           'Yen': {'Current': lambda uang: uang * 30.30, 'input1': 'Masukkan uang'}},
        'Won': {'Dolar': {'Current': lambda uang: uang * 0.00084, 'input1': 'Masukkan uang'},
                           'Rupiah': {'Current': lambda uang: uang * 12.04, 'input1': 'Masukkan uang'},
                           'Riyal': {'Current': lambda uang: uang * 0.0032, 'input1': 'Masukkan uang'},
                           'Won': {'Current': lambda uang: uang, 'input1': 'Masukkan uang'},
                           'Ringgit': {'Current': lambda uang: uang * 0.0035, 'input1': 'Masukkan uang'},
                           'Yen': {'Current': lambda uang: uang * 0.095, 'input1': 'Masukkan uang'}},
        'Ringgit': {'Dolar': {'Current': lambda uang: uang * 0.24, 'input1': 'Masukkan uang'},
                           'Rupiah': {'Current': lambda uang: uang * 3422.85, 'input1': 'Masukkan uang'},
                           'Riyal': {'Current': lambda uang: uang * 0.90, 'input1': 'Masukkan uang'},
                           'Won': {'Current': lambda uang: uang * 284.87, 'input1': 'Masukkan uang'},
                           'Ringgit': {'Current': lambda uang: uang, 'input1': 'Masukkan uang'},
                           'Yen': {'Current': lambda uang: uang * 27.19, 'input1': 'Masukkan uang'}},
        'Yen': {'Dolar': {'Current': lambda uang: uang * 0.0088, 'input1': 'Masukkan uang'},
                           'Rupiah': {'Current': lambda uang: uang * 126.04, 'input1': 'Masukkan uang'},
                           'Riyal': {'Current': lambda uang: uang * 0.033, 'input1': 'Masukkan uang'},
                           'Won': {'Current': lambda uang: uang * 10.49, 'input1': 'Masukkan uang'},
                           'Ringgit': {'Current': lambda uang: uang * 0.037, 'input1': 'Masukkan uang'},
                           'Yen': {'Current': lambda uang: uang, 'input1': 'Masukkan uang'}}}

#Fungsi untuk mengubah tipe data
def getNum(x):
    temp = x
    try:
        temp = int(x)
    except ValueError:
        temp = float(x)
    finally:
        if temp != '' and type(temp) is str:
            alert('Harap masukkan jumlah uang')
            temp = ''
            input1.value = temp
            return temp
        else:
            return temp

#Berjalan ketika pilihan mata uang diubah
def Action(ev):
    x = selectType.value
    for i in range(1, 5):
        input[str(i)].value = ''
        input[str(i)].disabled = False

#Dijalankan ketika button di-click ditekan(fungsi main)
def main(ev):
    num1 = getNum(input1.value)
    result = Current(selectType.value, num1)
    output.textContent = str(result)

#Fungsi untuk memanggil rumus
def Current(x, num1):
    y = selectCalculated.value
    for key in type1.keys():
        if key.find(x) > -1:
            return type1[x][y]['Current'](num1)

#ketika tombol di tekan diarahkan ke fungsi main
def keyEnter(ev):
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

#akan digunakan pilihan di ubah
selectType.bind('change', Action)
#ketikka button di klik maka akan memanggin fungsi main
button.bind('click', main)

# Mengarahakan ke 'Fungsi keyEnter' ketika 'enter' ditekan pada salah satu input field
input1.bind("keypress", keyEnter)
