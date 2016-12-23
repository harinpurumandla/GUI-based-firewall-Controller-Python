import iptc
import os
import socket
import datetime
def createRule(action, protocol, comments):
    rule = iptc.Rule()
    rule.protocol = protocol
    rule.target = iptc.Target(rule, action)
    match = rule.create_match("comment")
    match.comment = "FWH:" + comments
    return rule
def clearFile():
    with open("medium.rules", "w"):
        pass
def getIpaddress(website):
    try:
        if "http" not in website:
            return socket.gethostbyname(website)
        else:
            return socket.gethostbyname(website.split('/')[2])
    except:
        return False

def inserRule(dir, src, action, protocol, comments):
    rule = createRule(action, protocol, comments)
    if isDuplicate(rule) == True:
        return False
    else:
        dire = ""
        if dir == True:
            dire = "input"
            chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
            rule.src = src
            chain.insert_rule(rule)
        elif dir == False:
            dire = "output"
            chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "OUTPUT")
            rule.dst = src
            chain.insert_rule(rule)
    writeLog("Rule Added for ipaddress "+src+" protocol used "+protocol+" action "+action+" Target "+dire+" WebsiteName: "+comments)
    return True

def removeRule(dir, src, action, protocol, comments):
    try:
        rule = createRule(action, protocol, comments)
        if dir == True:
            chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
            rule.src = src
            chain.delete_rule(rule)
        elif dir == False:
            chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "OUTPUT")
            rule.dst = src
            chain.delete_rule(rule)
    except:
        print ''
def removeRules(rule,dir):
    dire = ""
    if dir == True:
        dire = "input"
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
        chain.delete_rule(rule)
    elif dir == False:
        dire = "output"
        chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "OUTPUT")
        chain.delete_rule(rule)
    writeLog( "Rule Added for ipaddress " + rule.src + " protocol used " + rule.protocol + " action " + rule.target.name + " Direction " + dire)

def countRules():
    length = 0
    input = 0
    output = 0
    table = iptc.Table(iptc.Table.FILTER)
    for chain in table.chains:
        length = length + len(chain.rules)
        if chain.name == "INPUT":
            input = input + len(chain.rules)
        elif chain.name == "OUTPUT":
            output = output + len(chain.rules)
    return length, input, output


def coutSetupRules():
    length = 0
    input = 0
    output = 0
    table = iptc.Table(iptc.Table.FILTER)
    for chain in table.chains:
        for rule in chain.rules:
            for match in rule.matches:
                if match.comment.startswith("FWH"):
                    length = length + 1
                    if chain.name == "INPUT":
                        input = input + 1
                    elif chain.name == "OUTPUT":
                        output = output + 1
    return length, input, output


def typeRule(rulesearch):
    table = iptc.Table(iptc.Table.FILTER)
    for chain in table.chains:
        for rule in chain.rules:
            if rulesearch == rule:
                return chain.name


def listRules():
    listrule = []
    rules = []
    table = iptc.Table(iptc.Table.FILTER)
    for chain in table.chains:
        for rule in chain.rules:
            listrule.append([rule.src, chain.name, rule.target.name, rule.protocol])
            rules.append(rule)
    return listrule,rules

def listSetupRules():
    listrule = []
    rules =[]
    table = iptc.Table(iptc.Table.FILTER)
    for chain in table.chains:
        for rule in chain.rules:
            for match in rule.matches:
                if "FWH" in match.comment:
                    listrule.append([match.comment,rule.src,chain.name,rule.target.name,rule.protocol])
                    rules.append(rule)
    return listrule,rules
def clearIPtables():
    os.system(" iptables -P INPUT ACCEPT ")
    os.system(" iptables -P FORWARD ACCEPT")
    os.system(" iptables -P OUTPUT ACCEPT")
    os.system(" iptables -t nat -F")
    os.system(" iptables -t mangle -F")
    os.system(" iptables -F")
    os.system(" iptables -X")

def toggleIPtable(option):
    if option == True:
        os.system("iptables-save > backup.rules")
        clearIPtables()
    elif option == False:
        os.system("iptables-restore < backup.rules")
        clearFile()

def setState(state):
    clearIPtables()
    os.system("iptables-restore < medium.rules")
    clearFile()
    if state == 1:
        os.system("iptables-save >medium.rules ")
        writeLog("State changed to High Filtering")
        clearIPtables()
        os.system(" iptables -P INPUT DROP ")
        os.system(" iptables -P FORWARD DROP")
        os.system(" iptables -P OUTPUT DROP")
    elif state == 2:
        clearIPtables()
        os.system("iptables-restore < medium.rules")
        writeLog("State changed to Medium Filtering")
        clearFile()
    elif state ==3:
        clearFile()
        os.system("iptables-save > medium.rules")
        writeLog("State changed to Low Filtering")
        clearIPtables()
        toggleIPtable(True)

def findDuplicates():
    c=0
    a, rule1 = listRules()
    a, rule2 = listRules()
    for i in range(0,len(rule1)):
        for j in range(0,len(rule2)):
            if i != j:
                if rule1[i] == rule1[i] :
                    removeRules(rule1[i],True)
                    removeRules(rule1[i],False)
                    c= c+1
    return c

def isDuplicate(newrule):
    table = iptc.Table(iptc.Table.FILTER)
    for chain in table.chains:
        for rule in chain.rules:
            if rule == newrule:
                return True
    return False

def getInfo(rule):
    dir = typeRule(rule)
    src = ""
    if dir == "INPUT":
        src = rule.src
    elif dir == "OUTPUT":
        src = rule.dst
    action = rule.target.name
    protocol = rule.protocol
    comments =""
    for match in rule.matches:
        if match.comment.startswith("FWH"):
            comments = match.comment
    return dir,src,action,protocol,comments
def writeLog(str):
    with open("log", "a") as logfile:
             logfile.write("*********************************** " + datetime.datetime.now().strftime("%y-%m-%d-%H-%M")+ "***********************************\n")
             logfile.write(str)
             logfile.write("\n*******************************************************************************************\n\n")


