
def getcs():
    s= input("server");
    d= input("db");
    u= input("user");
    p= input("password");
    return "server= %s;dbname=%s;user=%s;password=%s"%(s,d,u,p)
cs=getcs()
def cstodict(cs):
    return dict([i.split("=") for i in cs.split(";")])    
