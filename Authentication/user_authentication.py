from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
import logging






async def user_register(data : dict , db : AsyncSession) -> dict[str,str] :
    
    query = text("""
    INSERT INTO `users` (`name`, `email`, `district`, `land_in_hectors`, `password`)
    VALUES (:name, :email, :district, :land_in_hectors, :password);
    """)

    try :
        await db.execute(query , data)
        await db.commit()
        
        return {"status": "success", "message":"user data inserted succesfully"}
    except Exception as e :
        db.rollback()

        return {"status": "failed", "message":str(e)}






async def user_login(email : str , db : AsyncSession) -> dict:

    query = text("""SELECT  `id`, `email`, `password`, `district` FROM `users` WHERE email = :email ;""")

    try:
        result=await db.execute(query, {"email":email})
        row=result.mappings().fetchone()
        
        if not row :
            return {"status" : "failed", "message" : "invalid credentials" , "data" : None}
        
        return  {"status" : "success", "message" : "successfulyy loggend in ", "data" : dict(row) }
    
    except Exception as e :

        logging.error(f"Database logging error for {email} : {e} ")

        return {"status" : "failed", "message" : "internal sever error" , "data" : None}
        

