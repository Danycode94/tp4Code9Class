""" Klas sa gen tout metod ki pou manipile pwogram lan. """

from atribi_machin import AtribiMachin

class Fonksyonalite:
    
    """ Metod kap pemet nus akselere machin lan pi retire nan gaz lan. """
    def akselere(self):
        
        if AtribiMachin.gaz >= 14:
            AtribiMachin.gaz -= 14
            AtribiMachin.vites += 34
            print(f"\nOu akselere eu itilize 14 lit gaz ou rete :{AtribiMachin.gaz} lit")
        else:
            print(f"\nOu paka akselere koz gaz ou two piti - ou rete :{AtribiMachin.gaz} lit")
        
        input("\nTape Enter sou klavye an puw kontinye")
        
    """ Metod kap pemet nus frennen machin lan. """
    def frennen(self):
        if AtribiMachin.gaz >= 7:
            if AtribiMachin.vites <= 0:
                print("\nOu paka frennen koz ou pat akselere")
            elif AtribiMachin.vites >= 58:
                vites = AtribiMachin.vites
                AtribiMachin.vites -= 58
                AtribiMachin.gaz -= 7
                
                if AtribiMachin.gaz < 7:
                    AtribiMachin.vites = 0
                
                print(f"\nOu tap kouri a :{vites} km/h, ou frennen ou a :{AtribiMachin.vites} km/h - eu itilize 7 lit gaz ou rete :{AtribiMachin.gaz} lit")
            elif AtribiMachin.vites < 58:
                vites = AtribiMachin.vites
                AtribiMachin.vites = 0
                AtribiMachin.gaz -= 7
                print(f"\nOu tap kouri a :{vites} km/h, ou frennen ou a :{AtribiMachin.vites} km/h - eu itilize 7 lit gaz ou rete :{AtribiMachin.gaz} lit")
        else:
            print(f"\nOu paka frennen koz gaz ou two piti - ou rete :{AtribiMachin.gaz} lit")
        
        input("\nTape Enter sou klavye an puw kontinye")

    """ Metod kap pemet nus vann a yon lot moun machin lan. """
    def vann_machin(self,non_pwopriyete):
        
        print(f"--> :{AtribiMachin.setTente}")
        print(f"Pri machin nan se :{(AtribiMachin._pri)}")
        print(f"\nAnsyen non pwopriyete an se :{AtribiMachin.pwopriyete}")
        AtribiMachin.pwopriyete = non_pwopriyete
        print(f"Nouvo non pwopriyete an se :{AtribiMachin.pwopriyete}")
            
        input("\nTape Enter sou klavye an puw kontinye")
        
    
    """ Metod kap pemet nus douko machin lan selon koule met li vlel. """
    def douko_machin(self,koule):
        print(f"\nAnsyen koule an se te :{AtribiMachin.koule}")
        if koule == AtribiMachin.koule:
            print(f"Ansyen koule an egal a nouvo an pa gen modifikasyon !")
        else:
            AtribiMachin.koule = koule
            AtribiMachin._pri += 200
            print(f"Nouvo koule machin lan se :{AtribiMachin.koule}")
            
        input("\nTape Enter sou klavye an puw kontinye")


    """ Metod kap pemet nus fe gaz nan machin lan. """
    def fe_gaz(self, gaz):
        konnen_gaz = 0
        pri_gaz = 750
        gaz = float(gaz)
        qte_gaz_dispo_en_lit = AtribiMachin.gaz
        qte_gaz_dispo_en_galon = (qte_gaz_dispo_en_lit * 0.264)
        
        
        print(f"\nOu mande achte {gaz} galon gaz - pri pa galon an se {pri_gaz} HTG")
        print(f"Ou gen deja nan rezev ou {qte_gaz_dispo_en_galon} galon gaz")
        
        lit_gaz_achte = (gaz * 3.785)
        print(f"\nKantite galon gaz ou achte an vo {lit_gaz_achte} lit")
        print(f"Pou {lit_gaz_achte} lit gaz wap peye {(pri_gaz * gaz)}")
        
        lit_gaz_total = (lit_gaz_achte + qte_gaz_dispo_en_lit)
        if lit_gaz_total > 3500:
            qte_lit_gaz_mankan = 3500 - qte_gaz_dispo_en_lit
            qte_galon_gaz_mankan = (qte_lit_gaz_mankan * 0.264)
            print("\n----------------------------------------------------------------------------------------------------------------")
            print(f"kantite ou ap gaz wap achte trop - wap ka pran {qte_lit_gaz_mankan:.2f} lit - ou {qte_galon_gaz_mankan:.2f} galon gaz")
            print("----------------------------------------------------------------------------------------------------------------")
        else:
            AtribiMachin.gaz += lit_gaz_achte
            konnen_gaz += 1
            print(f"\nKounya ou gen {AtribiMachin.gaz} lit gaz en stok")
            
        if konnen_gaz == 3:
            AtribiMachin._pri += 1000
            AtribiMachin = 0
            
        input("\nTape Enter sou klavye an puw kontinye")
        