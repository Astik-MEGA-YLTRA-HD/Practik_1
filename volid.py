import app

def volid_ferst_name(ferst_name):
    ferst_name = app.ferst_name
    
    if type(ferst_name) == str and len(ferst_name) != 0:
        return ferst_name
    
    else:
        return None
    
def volid_last_name(last_name):
    last_name = app.last_name
    
    if type(last_name) == str and len(last_name) != 0:
        return last_name
    
    else:
        return None