from sdk.api.message import Message
from sdk.exceptions import CoolsmsException

def sendMsg(deg):    
    api_key = "NCSYHZ5RDHYSX6MT"
    api_secret = "C1QTL9MBI05LYDKFNZO1STHSGCPLUCWT"
    params = dict()
    params['type'] = 'sms'
    params['to'] = '01086461870' #받는번호
    params['from'] = '01086461870' #보내는번호
    params['text'] = '배전반 A에서 고온이 감지되었습니다! 배전반 A를 확인해주세요! 배전반A 온도: %.1f도'%(deg) #문자 내용
    cool = Message(api_key,api_secret)
    response =cool.send(params)
    return response            
