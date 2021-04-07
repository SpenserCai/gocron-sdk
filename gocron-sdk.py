import base64,hashlib
import json,time,jwt
import requests
class GoCron:
    @staticmethod
    def CreateToken():
        authSecret = "auth_secret"
        apiBaseUrl = "base_url"
        apiUser = "user_name"
        apiUserId = int("user_id")
        jwtHeaders = headers = {"alg": "HS256","typ": "JWT"}
        payload = {
            'uid': apiUserId,
            'issuer': 'gocron',
            'username': apiUser,
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

    @staticmethod
    def GetLogListQuery(query):
        taskId = query.get("id","")
        taskProtocol = query.get("protocol","")
        taskStatus = query.get("status","")
        pageSize = query.get("page_size","")
        page = query.get("page","")
        urlPath = '/api/task/log?page_size={0}&page={1}&task_id={2}&protocol={3}&status={4}'.format(pageSize,page,taskId,taskProtocol,taskStatus)
        return GoCron.SendResquest(urlPath)

    @staticmethod
    def RunTaskWithTaskId(taskId):
        return GoCron.SendResquest('/api/task/run/{0}'.format(taskId))

    @staticmethod
    def RemoveTaskWithTaskId(taskId):
        return GoCron.SendResquest('/api/task/remove/{0}'.format(taskId))
