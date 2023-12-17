""" Klas ki la pou verifye integrite done kp antre nan input yo. """

import re

class VerifyeDoneAntre:
    
    """ Fonsyon cha pou menu an ki pemet verifye si antre yo konpri ant 1 a 5. """
    def verifye_nonb_menu(chwa: str) -> bool:  
        fomat_regex = re.compile(r"^[0-5][0-5]*$")
        final_regex = re.match(fomat_regex, chwa)
    
        if final_regex:
           return True
        else:
            return False
        
    
    def verifye_nouvo_pwopriyete(chwa: str):
        foma_regex = re.compile(r"^[a-z0-9][A-Z0-9]*$")
        final_regex = re.match(foma_regex, chwa)
        
        if final_regex:
            return True
        else:
            return False
        
    def verifye_antre_gaz(chwa: str):
        foma_regex = re.compile(r"^[1-9][0-9]*$")
        final_regex = re.match(foma_regex, chwa)
        
        if final_regex:
            return True
        else:
            return False