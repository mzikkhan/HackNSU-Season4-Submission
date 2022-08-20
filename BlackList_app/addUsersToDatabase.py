from mimetypes import init


from django.db import connections
class UserAdd:
    def __init__(self,studentId="",name="",email="") :
        self.studentId=studentId
        self.name=name;
        self.email=email
    
    def addUser(self):
        db_cursor=connections['default'].cursor()
        db_cursor.execute("INSERT INTO BlackList_app_users(userid,name,email) VALUES('"+self.studentId+"','"+self.name+"','"+self.email+"')")
        