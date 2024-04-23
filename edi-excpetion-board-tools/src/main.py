from business.process_validation_rules import ProcessValidationRules
from model.validation_rule import ValidationRule
import datetime

def main():    
    print(datetime.datetime.now())
    validationRule=[ValidationRule.PO_Line_Canceled_After_Booked_Shipped,ValidationRule.PO_Line_Qty_Reduced_Below_Booked_Shipped_Qty,ValidationRule.PO_Line_Destination_mismatch_After_Booked_Shipped,ValidationRule.PO_Line_Requested_Delivery_Date_Mismatch_After_Book]
    ProcessValidationRules("C8523735",validationRule)
    print(datetime.datetime.now())
    pass

main()