import cv2
import pymysql
import db_connection

def textDB_Convert():    
    cur.execute(Query)
    imgtext = cur.fetchall()    
    return imgtext
    
seq = None
i=0
cnt=0
Maria=db_connection.Maria_conn
try:    
    with Maria.cursor() as cur:
        Query =  "select imgtext from temp_text_data"
        while True:
            if seq == None:
                break 
            for i in 999999:                                 
                img = textDB_Convert()                      
                cnt=cnt+1
                cv2.imwrite("testConver%d.jpg"%cnt,img)         


finally:
    Maria.close()