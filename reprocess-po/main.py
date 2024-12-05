import csv
import requests

# 定义 TransactionType 枚举
class TransactionType:
    NoneType = 0
    Booking = 1
    EdiCustomerUpdate = 2
    DeleteBookingRelationship = 3

# 将 TransactionType 字符串转换为枚举值
def get_transaction_type_enum(transaction_type_str):
    mapping = {
        "None": TransactionType.NoneType,
        "Booking": TransactionType.Booking,
        "EdiCustomerUpdate": TransactionType.EdiCustomerUpdate,
        "DeleteBookingRelationship": TransactionType.DeleteBookingRelationship
    }
    return mapping.get(transaction_type_str, TransactionType.NoneType)

# 读取 CSV 文件并发送 POST 请求
def process_csv_and_send_requests(csv_file_path, url):
    headers = {
        "Content-Type": "application/json"
    }
    with open(csv_file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            transaction_id = int(row['TransactionId'])
            transaction_type_str = 2
            
            
            # 构建请求体
            payload = {
                "TransactionId": transaction_id,
                "TransactionType": transaction_type_str
            }
            # 发送 POST 请求
            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                print(f"Successfully sent: {payload}")
            else:
                print(f"Failed to send: {payload}, Status Code: {response.status_code}, Response: {response.text}")

# 使用脚本
csv_file_path = 'file2.csv'  # 替换为你的CSV文件路径
url = 'http://inavisphere.chrobinson.com/api/PO/PurchaseOrderItemsHistoryOrch/v1/PurchaseOrderTransactions/'  # 替换为你的API端点

process_csv_and_send_requests(csv_file_path, url)
