import pyodbc
import requests

Dev_DB_Conn_ = 'DRIVER={SQL Server};SERVER=POMGMTDB_DEV;DATABASE=POManagement;Trusted_Connection=true'
INT_DB_Conn_ = 'DRIVER={SQL Server};SERVER=POMGMTDB_INT;DATABASE=POManagement;Trusted_Connection=true'
TRN_DB_Conn_ = 'DRIVER={SQL Server};SERVER=DB29TR2012b;DATABASE=POManagement;Trusted_Connection=true'
PRD_DB_Conn_ = 'DRIVER={SQL Server};SERVER=POMgmtDB;DATABASE=POManagement;Trusted_Connection=true'

#Service_Url="https://dev-inavisphere.chrobinson.com/api/PO/Legacy/v1/Tests/ComparePurchaseOrderSPResults"
Service_Url="http://localhost:2345/Tests/ComparePurchaseOrderSPResults"


def get_customer_data():
    query = "SELECT top 100 CustomerCode, CustomerPONum FROM po.po (nolock)  order by createdDate  desc"
    try:
        # Establish the connection
        conn = pyodbc.connect(PRD_DB_Conn_)
        cursor = conn.cursor()
        
        # Execute the query
        cursor.execute(query)
        
        # Fetch all results
        results = cursor.fetchall()
        
        # Extract CustomerCode and CustomerPONum
        customer_data = [(row.CustomerCode, row.CustomerPONum) for row in results]
        
        # Close the connection
        cursor.close()
        conn.close()
        
        return customer_data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None



def post_customer_data(customer_code, customer_po_number):
    headers = {
        'Content-Type': 'application/json'
    }
    body = {
        "CustomerCode": customer_code,
        "CustomerPONumber": customer_po_number
    }
    
    try:
        response = requests.post(Service_Url, json=body, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:            
            response_data = response.json()
            # Check if Pass is true
            if response_data.get('pass') is True:
                return True
            else:
                return False            
        else:
            print(f"POST request failed with status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def comparesp():
    customer_data = get_customer_data()
    i=1
    for customer_code, customer_po_num in customer_data:
        res = post_customer_data(customer_code, customer_po_num)
        print(f"Seq:{i},CustomerCode: {customer_code}, CustomerPONum: {customer_po_num}, Result: {res}")        
        i=i+1

comparesp()
#post_customer_data("C8145065", "458582")
