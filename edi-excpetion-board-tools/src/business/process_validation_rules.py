
from typing import List
from model.environment import Environment
from model.validation_rule import ValidationRule
from repository.validation_rule_repoistory import SaveValidationRule


#envList=[Environment.Dev,Environment.INT,Environment.TRN,Environment.PRD]

envList=[Environment.Dev]

def ProcessValidationRules(ccode:str, rules: List[ValidationRule]):
    #Process Dev
    if ccode =="":
        return
    if len(rules)<=0 :
        return
        
    for env in envList:        
        SaveValidationRule(env, ccode, rules)
    