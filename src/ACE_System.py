import sys
import numpy as np
import cv2
import time
import db_connection
from pylepton import Lepton
from datetime import datetime
import coolsms_API
import threading

#이미지내 최대온도
def max_temp(img):
    global getImage
    imgt=getImage.copy()
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(imgt)
    deg = display_temperatureC(img, maxVal, maxLoc, (0, 255, 0))
    return ktoc(maxVal)

#이미지내 최소온도
def min_temp(img):
    imgt=getImage.copy()
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(imgt)
    min_deg = display_temperatureC(img, minVal, minLoc,(0, 0, 255))
    return ktoc(minVal)

#컬러맵 설정 default rainbow
def generate_color_map(colorMapType = 1):
   
    lut = np.zeros((256, 1, 3), dtype=np.uint8)

    #colorMaps   

    colormap_rainbow = [1, 3, 74, 0, 3, 74, 0, 3, 75, 0, 3, 75, 0, 3, 76, 0, 3, 76, 0, 3, 77, 0, 3, 79, 0, 3, 82, 0, 5, 85, 0, 7, 88, 0, 10, 91, 0, 14, 94, 0, 19, 98, 0, 22, 100, 0, 25, 103, 0, 28, 106, 0, 32, 109, 0, 35, 112, 0, 38, 116, 0, 40, 119, 0, 42, 123, 0, 45, 128, 0, 49, 133, 0, 50, 134, 0, 51, 136, 0, 52, 137, 0, 53, 139, 0, 54, 142, 0, 55, 144, 0, 56, 145, 0, 58, 149, 0, 61, 154, 0, 63, 156, 0, 65, 159, 0, 66, 161, 0, 68, 164, 0, 69, 167, 0, 71, 170, 0, 73, 174, 0, 75, 179, 0, 76, 181, 0, 78, 184, 0, 79, 187, 0, 80, 188, 0, 81, 190, 0, 84, 194, 0, 87, 198, 0, 88, 200, 0, 90, 203, 0, 92, 205, 0, 94, 207, 0, 94, 208, 0, 95, 209, 0, 96, 210, 0, 97, 211, 0, 99, 214, 0, 102, 217, 0, 103, 218, 0, 104, 219, 0, 105, 220, 0, 107, 221, 0, 109, 223, 0, 111, 223, 0, 113, 223, 0, 115, 222, 0, 117, 221, 0, 118, 220, 1, 120, 219, 1, 122, 217, 2, 124, 216, 2, 126, 214, 3, 129, 212, 3, 131, 207, 4, 132, 205, 4, 133, 202, 4, 134, 197, 5, 136, 192, 6, 138, 185, 7, 141, 178, 8, 142, 172, 10, 144, 166, 10, 144, 162, 11, 145, 158, 12, 146, 153, 13, 147, 149, 15, 149, 140, 17, 151, 132, 22, 153, 120, 25, 154, 115, 28, 156, 109, 34, 158, 101, 40, 160, 94, 45, 162, 86, 51, 164, 79, 59, 167, 69, 67, 171, 60, 72, 173, 54, 78, 175, 48, 83, 177, 43, 89, 179, 39, 93, 181, 35, 98, 183, 31, 105, 185, 26, 109, 187, 23, 113, 188, 21, 118, 189, 19, 123, 191, 17, 128, 193, 14, 134, 195, 12, 138, 196, 10, 142, 197, 8, 146, 198, 6, 151, 200, 5, 155, 201, 4, 160, 203, 3, 164, 204, 2, 169, 205, 2, 173, 206, 1, 175, 207, 1, 178, 207, 1, 184, 208, 0, 190, 210, 0, 193, 211, 0, 196, 212, 0, 199, 212, 0, 202, 213, 1, 207, 214, 2, 212, 215, 3, 215, 214, 3, 218, 214, 3, 220, 213, 3, 222, 213, 4, 224, 212, 4, 225, 212, 5, 226, 212, 5, 229, 211, 5, 232, 211, 6, 232, 211, 6, 233, 211, 6, 234, 210, 6, 235, 210, 7, 236, 209, 7, 237, 208, 8, 239, 206, 8, 241, 204, 9, 242, 203, 9, 244, 202, 10, 244, 201, 10, 245, 200, 10, 245, 199, 11, 246, 198, 11, 247, 197, 12, 248, 194, 13, 249, 191, 14, 250, 189, 14, 251, 187, 15, 251, 185, 16, 252, 183, 17, 252, 178, 18, 253, 174, 19, 253, 171, 19, 254, 168, 20, 254, 165, 21, 254, 164, 21, 255, 163, 22, 255, 161, 22, 255, 159, 23, 255, 157, 23, 255, 155, 24, 255, 149, 25, 255, 143, 27, 255, 139, 28, 255, 135, 30, 255, 131, 31, 255, 127, 32, 255, 118, 34, 255, 110, 36, 255, 104, 37, 255, 101, 38, 255, 99, 39, 255, 93, 40, 255, 88, 42, 254, 82, 43, 254, 77, 45, 254, 69, 47, 254, 62, 49, 253, 57, 50, 253, 53, 52, 252, 49, 53, 252, 45, 55, 251, 39, 57, 251, 33, 59, 251, 32, 60, 251, 31, 60, 251, 30, 61, 251, 29, 61, 251, 28, 62, 250, 27, 63, 250, 27, 65, 249, 26, 66, 249, 26, 68, 248, 25, 70, 248, 24, 73, 247, 24, 75, 247, 25, 77, 247, 25, 79, 247, 26, 81, 247, 32, 83, 247, 35, 85, 247, 38, 86, 247, 42, 88, 247, 46, 90, 247, 50, 92, 248, 55, 94, 248, 59, 96, 248, 64, 98, 248, 72, 101, 249, 81, 104, 249, 87, 106, 250, 93, 108, 250, 95, 109, 250, 98, 110, 250, 100, 111, 251, 101, 112, 251, 102, 113, 251, 109, 117, 252, 116, 121, 252, 121, 123, 253, 126, 126, 253, 130, 128, 254, 135, 131, 254, 139, 133, 254, 144, 136, 254, 151, 140, 255, 158, 144, 255, 163, 146, 255, 168, 149, 255, 173, 152, 255, 176, 153, 255, 178, 155, 255, 184, 160, 255, 191, 165, 255, 195, 168, 255, 199, 172, 255, 203, 175, 255, 207, 179, 255, 211, 182, 255, 216, 185, 255, 218, 190, 255, 220, 196, 255, 222, 200, 255, 225, 202, 255, 227, 204, 255, 230, 206, 255, 233, 208]
   
    def chunk(ulist, step):
        return map(lambda i: ulist[i: i + step], range(0, len(ulist), step))

    if (colorMapType == 1):
        chunks = chunk(colormap_rainbow, 3)    
    red = []
    green = []
    blue = []
    

    for chunk in chunks:
        red.append(chunk[0])
        green.append(chunk[1])
        blue.append(chunk[2])

    lut[:, 0, 0] = blue

    lut[:, 0, 1] = green

    lut[:, 0, 2] = red

    return lut

#섭씨 온도 설정 default
def ktoc(val):
    return round(((val - 27000) / 100.0), 2)

#온도 화면에 출력(섭씨)
def display_temperatureC(img, val_k, loc, color):
    val = ktoc(val_k)
    cv2.putText(img,"{0:.1f} 'C".format(val), loc, cv2.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)
    x, y = loc
    cv2.line(img, (x - 2, y), (x + 2, y), color, 1)
    cv2.line(img, (x, y - 2), (x, y + 2), color, 1)

def raw_to_8bit(data):
    cv2.normalize(data, data, 0, 65535, cv2.NORM_MINMAX)
    np.right_shift(data, 8, data)
    return cv2.cvtColor(np.uint8(data), cv2.COLOR_GRAY2RGB)

#온도값 데이터베이스에 저장
def MariaDB_temp(deg_db, min_deg_db, avg_deg_db):    
    print ("{:%Y.%m.%d %H:%M:%S}".format(datetime.now())+ " MaxTemp = {0:.1f} C".format(deg_db)+" MinTemp = {0:.1f} C".format(min_deg_db)+" AvgTemp = {0:.1f} C".format(avg_deg_db))          
    Values = [("{:%Y.%m.%d %H:%M:%S}".format(datetime.now()),deg_db, min_deg_db, avg_deg_db, "{:%Y%m%d}".format(datetime.now()), "{:%H%M%S}".format(datetime.now()))]   
    cur.executemany(Query,Values)
    Maria.commit()
    time.sleep(10)      

#데이터베이스 연결    
Maria=db_connection.Maria_conn

try:   
    with Maria.cursor() as cur:
        Query = "INSERT INTO Temp_Data (TIME, MAXTEMP, MINTEMP, AVGTEMP, DAY, HOUR) VALUES (%s,%s,%s,%s,%s,%s)"        
        Query2= "INSERT INTO TEMP_TEXT_DATA (TEMPTIME, IMGTEXT, TEMPDAY, TEMPHOUR) VALUES (%s,%s,%s,%s)" 
        while True:
            with Lepton() as l:
                a,_ = l.capture()

            a = cv2.resize(a[:,:], (640, 480))

            getImage = a.copy()                         
            cnt = 0
            img = cv2.LUT(raw_to_8bit(a), generate_color_map())
            
            deg = max_temp(img)
            min_deg=min_temp(img)
            avg_deg = round((deg+min_deg)/2,2)
                                    
            if(deg>80):
                cnt = cnt+1                
                cv2.imwrite("test%d.jpg"%cnt,img) 
                response = coolsms_API.sendMsg(deg)                
                print("Success MessageSend: %s건"%response['success_count'])
                print("Failed MessageSend: %s건"%response['error_count'])
                print("Group ID: %s"%response['group_id'])
                if "error_list" in response:
                    print('Error List : %s'%response['error_list'])

            cv2.putText(img,"AverageTemp:%.1f'C"%(avg_deg),(10,30),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
            cv2.putText(img,"MaxTemp:%.1f'C"%(deg),(10,55),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)
            cv2.putText(img,"MinTemp:%.1f'C"%(min_deg),(10,80),cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
            cv2.imshow('frame',img)

            DB_temp = threading.Thread(target=MariaDB_temp, args=(deg, min_deg, avg_deg))
            if deg is not None:
                DB_temp.start
                time.sleep(1)                                           
            else:
                print("Faild to get Reading.")
            
                           
            if cv2.waitKey(1) & 0xFF == ord('q'):                
                break        
            #cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX) # extend contrast
            #np.right_shift(a, 8, a) # fit data into 8 bits
            #cv2.imwrite("output.jpg", np.uint8(a)) # write it!

except KeyboardInterrupt:
    print('Close')
except coolsms_API.CoolsmsException as e:
        print("Error code : %s"%e.error_code)
        print("Error message : %s"%e.msg)
        sys.exit()
finally:
    Maria.close()

