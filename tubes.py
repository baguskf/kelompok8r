#Import Library Brython 
from browser import document, alert

# Deklarasi Variable
input1 = document['input1']
button = document['btn']
output = document['output']
selectType = document['select-type']
selectCalculated = document['select-calculated']

# Dictionary uang
type1 = {'Dolar': {'Dolar': {'Current': lambda uang: uang, 'input1': 'Masukkan uang'},
                           'Rupiah': {'Current': lambda uang: uang * 14316.05, 'input1': 'Masukkan uang'},
                           'Riyal': {'Current': lambda uang: uang * 3.75, 'input1': 'Masukkan uang'},
                           'Won': {'Current': lambda uang: uang * 1188.98, 'input1': 'Masukkan uang'}},
        'Rupiah': {'Dolar': {'Current': lambda uang: uang * 0.000070 , 'input1': 'Masukkan uang'},
                           'Rupiah': {'Current': lambda uang: uang , 'input1': 'Masukkan uang'},
                           'Riyal': {'Current': lambda uang: uang * 0.00026, 'input1': 'Masukkan uang'},
                           'Won': {'Current': lambda uang: uang * 0.083, 'input1': 'Masukkan uang'}},
        'Riyal': {'Dolar': {'Current': lambda uang: uang * 0.27, 'input1': 'Masukkan uang'},
                           'Rupiah': {'Current': lambda uang: uang * 3815.21, 'input1': 'Masukkan uang'},
                           'Riyal': {'Current': lambda uang: uang , 'input1': 'Masukkan uang'},
                           'Won': {'Current': lambda uang: uang * 316.73, 'input1': 'Masukkan uang'}},
        'Won': {'Dolar': {'Current': lambda uang: uang, 'input1': 'Masukkan uang'},
                           'Rupiah': {'Current': lambda uang: uang * 12.04, 'input1': 'Masukkan uang'},
                           'Riyal': {'Current': lambda uang: uang * 0.0032, 'input1': 'Masukkan uang'},
                           'Won': {'Current': lambda uang: uang, 'input1': 'Masukkan uang'}}}

# Fungsi yang akan dijalankan ketika pilihan suhu diubah
def selectTypeAction(ev):
    x = selectType.value
    # Reset Input Field
    for i in range(1, 5):
        input[str(i)].value = ''
        input[str(i)].disabled = False

# Fungsi untuk mengubah string dari input ke int atau float
def getNum(x):
    temp = x
    # Convert string ke int
    try:
        temp = int(x)
    # Jika convert string ke int gagal (ValueError), maka convert ke float
    except ValueError:
        temp = float(x)
    finally:
        # Jika input (var temp) masih string (gagal convert ke int dan float), 
        # maka munculkan alert dan return dengan variable kosong ('')
        if temp != '' and type(temp) is str:
            alert('Harap masukkan jumlah uang')
            temp = ''
            input1.value = temp
            return temp
        # Jika salah satu convert berhasil, maka return
        else:
            return temp

# Fungsi untuk memanggil rumus pada dictionary
def Current(x, num1):
    y = selectCalculated.value
    for key in type1.keys():
        if key.find(x) > -1:
            return type1[x][y]['Current'](num1)

# Fungsi Main
# Dijalankan ketika button di-click atau tombol 'enter' ditekan
def main(ev):
    num1 = getNum(input1.value)
    result = Current(selectType.value, num1)
    output.textContent = str(result)

# Fugnsi keyEnter
# Fungsi yang mengarahkan ke 'Fungsi Main' ketika tombol 'enter' ditekan
def keyEnter(ev):
    traceKey = f"{ev.code}"
    if traceKey == 'Enter':
        main(0)

selectType.bind('change', selectTypeAction) # Ketika pilihan suhu berubah, maka akan menjalankan fungsinya
button.bind('click', main) # Memanggil 'Fungsi Main' ketika button di-click

# Mengarahakan ke 'Fungsi keyEnter' ketiak 'enter' ditekan pada salah satu input field
input1.bind("keypress", keyEnter)