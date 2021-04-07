import base64,hashlib
import json,time,jwt
import requests
class GoCron:
    @staticmethod
    def CreateToken():
        authSecret = "[AUTH_SECRET]"
        jwtHeaders = headers = {"alg": "HS256","typ": "JWT"}
        apiBaseUrl = "http://127.0.0.1:5920"
        payload = {
            'uid': 1,
            'issuer': 'gocron',
            'username': '[YOUR_USER_NAME]',
            'is_admin': 1,
            "iat":int(time.time()),
            "exp": int(time.time()+60)
        }
        authToken = jwt.encode(payload,authSecret,algorithm="HS256",headers=jwtHeaders)
        return authToken

    @staticmethod
    def SendResquest(urlPath):
        header = {"Auth-Token":GoCron.CreateToken()}
        repData = requests.get(url = apiBaseUrl + urlPath,headers=header).text
        repData = json.loads(repData)
        return repData
        
    @staticmethod
    def GetTaskDetail(taskId):
        return GoCron.SendResquest('/api/task/{0}'.format(taskId))

    @staticmethod
    def DisableTask(taskId):
        return GoCron.SendResquest('/api/task/disable/{0}'.format(taskId))

    @staticmethod
    def EnableTask(taskId):
        return GoCron.SendResquest('/api/task/enable/{0}'.format(taskId))

    @staticmethod
    def GetTaskListQuery(query):
        taskId = query.get("id","")
        taskName = query.get("name","")
        taskProtocol = query.get("protocol","")
        taskTag = query.get("tag","")
        hostId = query.get("host_id","")
        taskStatus = query.get("status","")
        pageSize = query.get("page_size","")
        page = query.get("page","")
        urlPath = '/api/task?page_size={0}&page={1}&id={2}&protocol={3}&name={4}&tag={5}&host_id={6}&status={7}'.format(pageSize,page,taskId,taskProtocol,taskName,taskTag,hostId,taskStatus)
        return GoCron.SendResquest(urlPath)
