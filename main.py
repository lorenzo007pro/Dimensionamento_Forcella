#Dimensioniamo un terminale a forcella
import math

Forza = float(input('Inserisci la forza applicata sulla forcella [N]: '))

Sigma_Forcella = float(input('Inserisci la tensione di snervamento della forcella [MPa]: '))
Sigma_Perno = float(input('Inserisci la tensione di snervamento del perno [Mpa]: '))

gs = float(input('Inserisci il grado di sicurezza da usare  nel dimensionamento: '))

Sigma_Ammissibile_Forcella = Sigma_Forcella / gs
Sigma_Ammissibile_Perno = Sigma_Perno / gs

rad3 = math.sqrt(3)

Tau_Ammissibile_Forcella = Sigma_Ammissibile_Forcella / rad3
Tau_Ammissibile_Perno = Sigma_Ammissibile_Perno / rad3

diametro_perno = math.sqrt((8*Forza) / (3 * math.pi * Tau_Ammissibile_Perno))

altezza_perno = Forza / (Sigma_Ammissibile_Perno * diametro_perno)

t = altezza_perno / 2

Area_Resistente_Strappo = Forza / Sigma_Ammissibile_Forcella
Raggio_Forcella = (Area_Resistente_Strappo / (4 * t)) + (diametro_perno / 2)

Area_Resistente_Tranciamento = 2 * (2 * t * (math.sqrt(Raggio_Forcella - (diametro_perno / 2))))

Tau_massima_tranciamento = 1.5 * (Forza / Area_Resistente_Tranciamento)

diametro_perno_intero = diametro_perno // 1
print(diametro_perno_intero)

verifica = False
step = 0.5

while not verifica:
    if Tau_massima_tranciamento <= Tau_Ammissibile_Forcella:
            verificato = True
    else:
            # 🔧 aumenta diametro perno e riprova
        diametro_perno += step


if verifica:
     print('ciao')
