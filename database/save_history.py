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







async def fetch_prediction_history(user_id : int , db : AsyncSession) -> dict:

    query = text(""" SELECT  `N`,`P`,`K`,`temperature`,`humidity`,`ph`,`rainfall`, `predicted_crop` , `confidence` ,`time`, FROM `crop_recommendation_history`
                 WHERE user_id = :user_id ;
    """)

    try :

        crop_recommend_history = await db.execute(query, {"user_id" : user_id})
        rows = crop_recommend_history.mappings().fetchall()
        
        if not rows :
            return {"status" : "success" , "message" : "user has no history", "data" : []}

        formated_rows=[]

        for row in rows:

            data_row = dict(row)

            if data_row.get("time"):

                data_row["time"] = str(data_row.get("time"))

            formated_rows.append(data_row)

        return {"status" : "success" , "message" : "data is fetch successfully", "data" : formated_rows}
    
    except Exception as e :
        
        return {" status" : "failed" , "message" : str(e)}



async def save_crop_production(history , db : AsyncSession)-> dict :

    query = text(""" INSERT INTO `crop_production_history` (`user_id`, `district`, `year`, `season`, `crop`, `area`, `prediction` , `production_per_hectare`)
                 VALUES (:user_id, :district, :year, :season, :crop, :area, :prediction, :production_per_hectare);""")

    try :

        await db.execute(query, history)
        await db.commit()
        return {"status": "success", "message" : "pridiction history saved"}

    except Exception as e:

        return {"status" : "failed", "message" : str(e)}


async def fetch_production_history(user_id , db : AsyncSession)-> dict :

    query=text("""SELECT `district`, `year`, `season`, `crop` , `area` , `prediction`, `production_per_hectare`, `time` FROM `crop_production_history` WHERE `user_id` = :user_id """)

    try:

        crop_prodiction_history= await db.execute(query,{"user_id":user_id})
        rows = crop_prodiction_history.mappings().fetchall()

        if not rows :
            return {"status" : "success" , "message" : "user has no history", "data" : []}

        formated_rows=[]
        
        for row in rows:
        
            data_row = dict(row)
        
            if data_row.get("time"):
        
                data_row["time"] = str(data_row.get("time"))
        
            formated_rows.append(data_row)
            
        return {"status" : "success" , "message" : "data is fetch successfully", "data" : formated_rows}
        
    except Exception as e :
            
            return {" status" : "failed" , "message" : str(e)}

