from enum import Enum

from model.environment import Environment


# --29	PO Line Canceled After Booked/Shipped
# --31	PO Line UOM Mismatch to Booked/Shipped UOM
# --33	PO Line Qty Reduced Below Booked/Shipped Qty
# --37	PO Line Destination mismatch After Booked/Shipped
# --41	PO Line Requested Delivery Date Mismatch After Boo

class ValidationRule(Enum):
    PO_Line_Canceled_After_Booked_Shipped = 'PO Line Canceled After Booked/Shipped'
    PO_Line_UOM_Mismatch_to_Booked_Shipped_UOM = 'PO Line UOM Mismatch to Booked/Shipped UOM'
    PO_Line_Qty_Reduced_Below_Booked_Shipped_Qty = 'PO Line Qty Reduced Below Booked/Shipped Qty'
    PO_Line_Destination_mismatch_After_Booked_Shipped = 'PO Line Destination mismatch After Booked/Shipped'
    PO_Line_Requested_Delivery_Date_Mismatch_After_Book = 'PO Line Requested Delivery Date Mismatch After Book'   


def GetValidationRuleByEnv(env: Environment, rule: ValidationRule):
    match env:
        case Environment.Dev | Environment.PRD:
            return getPRDValidationRuleID(rule)
        case Environment.INT:
            return getINTValidationRuleID(rule)
        case Environment.TRN:
            return getTRNValidationRuleID(rule)        
        case _:
            return getPRDValidationRuleID(rule)



def getPRDValidationRuleID(rule: ValidationRule):
    match rule:
        case ValidationRule.PO_Line_Canceled_After_Booked_Shipped:
            return 29
        case ValidationRule.PO_Line_UOM_Mismatch_to_Booked_Shipped_UOM:
            return 31
        case ValidationRule.PO_Line_Qty_Reduced_Below_Booked_Shipped_Qty:
            return 33
        case ValidationRule.PO_Line_Destination_mismatch_After_Booked_Shipped:
            return 37
        case ValidationRule.PO_Line_Requested_Delivery_Date_Mismatch_After_Book:
            return 41

def getINTValidationRuleID(rule: ValidationRule):
    match rule:
        case ValidationRule.PO_Line_Canceled_After_Booked_Shipped:
            return 33
        case ValidationRule.PO_Line_UOM_Mismatch_to_Booked_Shipped_UOM:
            return 35
        case ValidationRule.PO_Line_Qty_Reduced_Below_Booked_Shipped_Qty:
            return 32
        case ValidationRule.PO_Line_Destination_mismatch_After_Booked_Shipped:
            return 44
        case ValidationRule.PO_Line_Requested_Delivery_Date_Mismatch_After_Book:
            return 46

def getTRNValidationRuleID(rule: ValidationRule):
    match rule:
        case ValidationRule.PO_Line_Canceled_After_Booked_Shipped:
            return 75
        case ValidationRule.PO_Line_UOM_Mismatch_to_Booked_Shipped_UOM:
            return 54
        case ValidationRule.PO_Line_Qty_Reduced_Below_Booked_Shipped_Qty:
            return 58
        case ValidationRule.PO_Line_Destination_mismatch_After_Booked_Shipped:
            return 78
        case ValidationRule.PO_Line_Requested_Delivery_Date_Mismatch_After_Book:
            return -1