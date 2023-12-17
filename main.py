""" Klas Main se klas prensipal pwogram nan. """

from os import system
from app.verifye_done_antre import VerifyeDoneAntre
from mesaj.mesaj_meni import MesajMeni
from app.fonksyonalite import Fonksyonalite

class Main:
    
    """ Meni kap la pou afiche tt fonksyonalite pwogram nan genyen. """
    def meni_prensipal(self):
        tes_input = True
        
        while tes_input:
            system("cls")
            MesajMeni.meni_prensipal(self)
            
            chwa = input("Chwazi chif ki korespon'n ak operasyon ou vle fe an: ").strip()
            chwa_tounen = VerifyeDoneAntre.verifye_nonb_menu(chwa)
            while chwa_tounen == False:
                chwa = input("Chwazi chif ki korespon'n ak operasyon ou vle fe an: ").strip()
                chwa_tounen = VerifyeDoneAntre.verifye_nonb_menu(chwa)
                
            chwa = int(chwa)
            match(chwa):
                case 0:
                    system("cls")
                    tes_input = False
                    print("\nMesi paskew te itilize pwogram nan. \n")
                case 1:
                    system("cls")
                    Fonksyonalite.akselere(self)
                case 2:
                    system("cls")
                    Fonksyonalite.frennen(self)
                case 3:
                    system("cls")
                    non_pwopriyete = input("Antre nouvo non pwopriyete a :").strip()
                    VerifyeDoneAntre.verifye_nouvo_pwopriyete(non_pwopriyete)
                    while non_pwopriyete == False:
                        non_pwopriyete = input("Antre nouvo non pwopriyete a :").strip()
                        VerifyeDoneAntre.verifye_nouvo_pwopriyete(non_pwopriyete)
                    system("cls")
                    Fonksyonalite.vann_machin(self,non_pwopriyete)
                case 4:
                    system("cls")
                    douko = input("Antre koule wap douko machin lan :").strip()
                    VerifyeDoneAntre.verifye_nouvo_pwopriyete(douko)
                    while douko == False:
                        douko = input("Antre koule wap douko machin lan :").strip()
                        VerifyeDoneAntre.verifye_nouvo_pwopriyete(douko)
                    system("cls")
                    Fonksyonalite.douko_machin(self,douko)
                case 5:
                    system("cls")
                    print("\Galon gaz lan vann 750 HTG")
                    gaz = input("Antre kantite galon gaz wap achte an :").strip()
                    VerifyeDoneAntre.verifye_antre_gaz(gaz)
                    while gaz == False:
                        gaz = input("Antre kantite galon gaz wap achte an :").strip()
                        VerifyeDoneAntre.verifye_antre_gaz(gaz)
                    system("cls")
                    Fonksyonalite.fe_gaz(self,gaz)
        
        
        
        
        
Main().meni_prensipal()
