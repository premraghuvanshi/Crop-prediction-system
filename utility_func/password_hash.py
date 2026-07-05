import bcrypt



def hash_password(plain_password : str ) -> str :

    salt = bcrypt.gensalt()

    password_in_bytes = plain_password.encode('utf-8')

    return bcrypt.hashpw(password_in_bytes, salt).decode('utf-8')



def verify_password(plain_password : str, hashed_password : str ) -> bool :
    
    password_in_bytes = plain_password.encode('utf-8')

    result = bcrypt.checkpw(password_in_bytes, hashed_password.encode('utf-8'))

    return result