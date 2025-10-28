from core import DataBase
from volid import volid_last_name, volid_ferst_name, volid_email, volid_phon, volid_password

def append_user(db: DataBase):
    sql = """
    INSERT INTO users(first_name, last_name, email, phon, password)
    VALUES(?, ?, ?, ?, ?);
    """

    data = (volid_last_name(DataBase()), volid_ferst_name(DataBase()), volid_email(DataBase), volid_phon(DataBase()), volid_password(DataBase()))

    db.exec_write(sql, data)