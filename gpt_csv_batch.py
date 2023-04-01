import openai
import os
import pandas as pd
import time
import json

# generate your api key on https://platform.openai.com/account/api-keys
# and set up your key in OS (https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety)
openai.api_key = os.environ["OPENAI_API_KEY"]

domains = pd.read_csv("domains.csv")

domains.insert(len(domains.columns), 'company', "")
domains.insert(len(domains.columns), 'company_website', "")
domains.insert(len(domains.columns), 'result', "")

total_count = len(domains)
step = 300

for start in range(0, total_count, step):

    start_time = time.time()

    for i in range(start, min(start + step, total_count)):
        print('====' + str(i) + '====')
        completion = None
        try:
            URL = domains.iloc[i]["remote_hostname"]
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a network expert. Find out the purpose of the provided URL (choose one out of the options: tracking, marketing, advertising, analytics, CDN, static server, DNS, first-party host).  Response in JSON containing following fields: company, company_website, result. Respond in JSON only.",
                    },
                    {"role": "user", "content": URL},
                ],
                n=1,
                temperature=0.85,
            )
            
            

        except Exception as e:
            print(str(e))
            time.sleep(8)
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a network expert. Find out the purpose of the provided URL (choose one out of the options: tracking, marketing, advertising, analytics, CDN, static server, DNS, first-party host).  Response in JSON containing following fields: company, company_website, result. Respond in JSON only.",
                    },
                    {"role": "user", "content": URL},
                ],
                n=1,
                temperature=0.85,
            )
           
            continue
        
        # convert str to json
        print(completion.choices[0].message.content)
        try:
            resp = json.loads(completion.choices[0].message.content)
            domains.loc[i, ['company','company_website','result']] = [resp['company'], resp['company_website'], resp['result']]
        except Exception:
            print('=======================' + str(i) + ' is wrong =======================')
            continue
    
    

    filename = "./results/answers_" + str(start) + ".csv"
    domains.loc[list(range(start, min(start + step, total_count)))].to_csv(filename)  # , index=False

    end_time = time.time()
    time_used = end_time - start_time
    print("=============TIME USED: " + str(time_used) + "=====================")
