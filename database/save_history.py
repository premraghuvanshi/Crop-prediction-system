from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text


async def save_crop_recommendation(data : dict , db : AsyncSession) -> dict:

    query=text(""" INSERT INTO `crop_recommendation_history` ( `user_id` , `N`,`P`,`K`,`temperature`,`humidity`,`ph`,`rainfall`, `predicted_crop` , `confidence`)
               VALUES (:user_id , :N, :P, :K, :temperature, :humidity, :ph, :rainfall, :predicted_crop , :confidence) ;
    """)

    try : 

        await db.execute(query, data)
        await db.commit()

        return {"status" : "success" , "message" : "History saved successfully"}
    
    except Exception as e :

        return {"status" : "failed", "message" : str(e)}







async def fetch_history(user_id : int , db : AsyncSession) -> dict:

    query = text(""" SELECT  `N`,`P`,`K`,`temperature`,`humidity`,`ph`,`rainfall`, `predicted_crop` , `confidence` FROM `crop_recommendation_history`
                 WHERE user_id = :user_id ;
    """)

    try :

        crop_recommend_history = await db.execute(query, {"user_id" : user_id})
        rows = crop_recommend_history.mappings().fetchall()
        
        if not rows :
            return {"status" : "success" , "message" : "user has no history", "data" : []}
        
        return {"status" : "success" , "message" : "data is fetch successfully", "data" : [dict(row) for row in rows]}
    
    except Exception as e :
        
        return {" status" : "failed" , "message" : str(e)}



        
    