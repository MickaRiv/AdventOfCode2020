import numpy as np
import sys

def parse(filename):
    data = np.loadtxt(filename,dtype=str,delimiter=";")
    rules = {}
    for i,d in enumerate(data):
        if "your ticket" in d:
            break
        ruleData = d.split(":")
        rule = [[int(num) for num in nums.split("-")] for nums in ruleData[1].split(" or ")]
        rules[ruleData[0]] = rule
    myTicket = np.fromstring(data[i+1],dtype=int,sep=",")
    otherTickets = np.array([np.fromstring(d,dtype=int,sep=",") for d in data[i+3:]])
    return rules, myTicket, otherTickets

def spotError(ticket,rules):
    return [entry for entry in ticket if not checkValidEntry(entry,rules)]

def possibleField(entries,rules):
    return [ruleName for ruleName,rule in rules.items() if np.all([checkValidEntry(entry, {ruleName:rule}) for entry in entries])]

def checkValidEntry(entry,rules):
    return np.any([[rulePart[0] <= entry <= rulePart[1] for rulePart in rule] for rulename,rule in rules.items()])

rules, myTicket,otherTickets = parse("input")
print(np.sum([np.sum(spotError(ticket,rules),dtype=int) for ticket in otherTickets]))

validTickets = np.array([ticket for ticket in otherTickets if len(spotError(ticket,rules)) == 0])
fields = [possibleField(validTicketsEntry,rules) for validTicketsEntry in validTickets.T]
fieldNames = ["" for _ in range(len(fields))]
for _ in range(len(fields)):
    for i,field in enumerate(fields):
        if len(field) == 1:
            break
    fieldNames[i] = field[0]
    for field in fields:
        try:
            field.remove(fieldNames[i])
        except:
            pass
print(np.prod([entry for entry,name in zip(myTicket,fieldNames) if name.startswith("departure")],dtype=np.int64))