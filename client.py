import csv
import requests
import json
import os
from random import randint as rd

def generate_csv():
    '''Generates random CSV for testing'''
    with open('health_customers.csv', 'w', newline='') as health_file:
        fieldnames = ['id', 'postcode', 'age', 'gender', 'has_provider', 'has_children', 'marital_status', 'cover_type']

        csv_writer = csv.DictWriter(health_file, fieldnames=fieldnames)
        # to write the header of csv file
        csv_writer.writeheader()
        #create csv writer to write csv data into file
        for i in range(100):
            customer = {'id': i,
                        'postcode': rd(0,9999),
                        'age': rd(18, 99),
                        'gender': ['female', 'male'][rd(0,1)],
                        'has_provider': rd(0,1),
                        'has_children': rd(0,1),
                        'marital_status': ['single', 'married', 'de facto'][rd(0,2)],
                        'cover_type': ['hospital', 'extras', 'combined'][rd(0,2)]
                        }
            csv_writer.writerow(customer)

def request_skill(data_to_send):
    '''Request REST endpoint to get skills result'''
    url = "http://localhost:8080/skill/health"
    headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }

    customer = {'id': data_to_send['id'],
                'postcode': data_to_send['postcode'],
                'age': data_to_send['age'],
                'gender': data_to_send['gender'],
                'has_provider': data_to_send['has_provider'],
                'has_children': data_to_send['has_children'],
                'marital_status': data_to_send['marital_status'],
                'cover_type': data_to_send['cover_type']
        }
    response = requests.request("POST", url, data=json.dumps(customer), headers=headers)
    # print(response)
    return response.content

def process_csv():
    '''Process input csv input, request REST endpoint and get results'''
    if os.path.exists('health_customers.csv'):
        with open('health_customers.csv', 'r', newline='') as csv_in:
            fieldnames = ['id', 'postcode', 'age', 'gender', 'has_provider', 'has_children', 'marital_status', 'cover_type']
            next(csv_in)
            reader = csv.DictReader(csv_in, fieldnames=fieldnames)
            with open('health_skills.csv', 'w', newline='') as csv_out:
                fieldnames = ['id', 'skill']
                writer = csv.DictWriter(csv_out, fieldnames=fieldnames)
                writer.writeheader()
                for row in reader:
                    #requesting skills
                    response = request_skill(row)
                    skill = { 'id': row['id'],
                            'skill': json.loads(response.decode('utf-8'))['skill']
                            }
                    
                    writer.writerow(skill)

if __name__ == '__main__':
    #generate csv for testing
    # print("Generating csv for testing...")
    # generate_csv()

    print("Sending profiles and receiving skills...")
    process_csv()
    print("Done.")
    