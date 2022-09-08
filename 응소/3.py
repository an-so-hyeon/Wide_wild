def k2c(x):
    return k * 273.15

def mi2km(mi):
    return  mi * 1.6

def main():
    k = 285.3
    mile = 300

    print("{:.if)x => {:.if}c".format(k, k2c(k)))
    print("{:.if)mi => {:.if}km").format(mile, mi2km(mile)))