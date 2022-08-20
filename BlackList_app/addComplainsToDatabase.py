from django.db import connections
class RegisterComplains:
    def __init__(self,studentId,description,links,anonimity) :
        self.studentId=studentId
        self.description=description
        self.links=links
        self.anonimity=anonimity
    def registerComplains(self):
        
        db_cursor=connections['default'].cursor()
        
        #test the bool typecasting in execute line, might run into errors, if so, fix
        db_cursor.execute("INSERT INTO BlackList_app_complain (abuseDescription,links,anonymity,bully_id) VALUES('"+self.description+"','"+self.links+"','"+self.anonimity+"','"+self.studentId+"')")
        