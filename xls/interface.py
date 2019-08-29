import commands as cmd
import exceptions as erx

class Commands:

    cmd = {}

    def __init__(self,name,options,optReq,func):

        if name in cmd:
            raise erx.AlreadyPresentError()

        self.name = name
        cmd.insert(name)
        self.options = list(options)
        self.optReq = optReq
        self.run = func


command_list = { 
    "load": Commands("load", "", False, cmd.load),
    "currentWB": Commands("currentWB", "", False, cmd.currentWB),
    "currentWS": Commands("currentWS", "", False, cmd.currentWS),
    "switchWS": Commands("switchWS", "", True, cmd.switchWS),
    "add": Commands("add", "", True, cmd.add),
    "delete": Commands("delete", "", True, cmd.delete),
    "update": Commands("update", "", True, cmd.update),
    "append": Commands("append", "", True, cmd.append),
    "addColumn": Commands("addColumn", "", True, cmd.addColumn),
    "printRange": Commands("printRange", "", True, cmd.printRange),
    "eraseRange": Commands("eraseRange", "", True, cmd.eraseRange),
    "save": Commands("save", "", False, cmd.save),
    "saveAs": Commands("saveAs", "", False, cmd.saveAs)  
    }

