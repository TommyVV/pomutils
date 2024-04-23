from typing import List
import pyodbc
from model.environment import Environment
from model.validation_rule import GetValidationRuleByEnv, ValidationRule


Dev_DB_Conn_ = 'DRIVER={SQL Server};SERVER=POMGMTDB_DEV;DATABASE=POManagement;Trusted_Connection=true'
INT_DB_Conn_ = 'DRIVER={SQL Server};SERVER=POMGMTDB_INT;DATABASE=POManagement;Trusted_Connection=true'
TRN_DB_Conn_ = 'DRIVER={SQL Server};SERVER=DB29TR2012b;DATABASE=POManagement;Trusted_Connection=true'
PRD_DB_Conn_ = 'DRIVER={SQL Server};SERVER=POMgmtDB;DATABASE=POManagement;Trusted_Connection=true'


def SaveValidationRule(env: Environment, code: str, rules: List[ValidationRule]):
    conn_str =match_conn(env)
    if len(rules)<=0 : return
    
    try:
        # Connect to the database
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        for rule in rules:
            ruleId =GetValidationRuleByEnv(env, rule)    
            if(ruleId<0):
                continue        
            print(f'Connected to {env} database, code:{code}, ruleId:{ruleId}')
            # Execute the stored procedure with parameters
            cursor.execute(f'EXEC [dbo].[CreateValidationRuleParty] @ValidationRuleID={ruleId}, @PartyCode={code}')

        # Commit the changes
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except pyodbc.Error as e:
        print(f'Error executing stored procedure: {e}')

def match_conn(env: Environment):
    match env:
        case Environment.Dev:
            return Dev_DB_Conn_
        case Environment.INT:
            return INT_DB_Conn_
        case Environment.TRN:
            return TRN_DB_Conn_
        case Environment.PRD:
            return PRD_DB_Conn_
        case _:
            return Dev_DB_Conn_