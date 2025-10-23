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
    
def volid_email(email):
    email = app.email

    if type(email) == str and len(email) != 0:
        return email
    
    else:
        return None
    
def volid_phon(phon):
    phon = app.phon

    if type(phon) == str and len(phon) != 0:
        return phon
    
    else:
        return None
    
def volid_password(password):
    password = app.password

    if type(password) == str and len(password) != 0:
        return password
    
    else:
        return None
    
