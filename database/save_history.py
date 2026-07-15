from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text


async def save_crop_recommendation(data : dict , db : AsyncSession) -> dict:

    query=text(""" INSERT INTO `crop_recommendation_history` ( `user_id` , `features`, `predicted_crop` , `confidence`)
               VALUES (:user_id , :features, :predicted_crop , :confidence) ;
    """)

    try : 

        await db.execute(query, data)
        await db.commit()

        return {"status" : "success" , "message" : "History saved successfully"}
    
    except Exception as e :

        return {"status" : "failed", "message" : str(e)}
    