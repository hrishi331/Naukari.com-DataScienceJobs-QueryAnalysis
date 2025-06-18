import requests
import json
import numpy as np
import pandas as pd
import time

final_table = {'job_title' : [],
  'company_name' : [],
  'skills' :  [],
  'jobdescription' :  [],
  'staticurl' : [],
  'staticurl' : [],
  'experince' : [],
  'salary' : [],
  'location' : [],
  'company_review_count' : [],
  'company_rating' : []}

n = 1
for k in range(1,851):
  url = f"https://www.naukri.com/jobapi/v3/search?noOfResults=20&urlType=search_by_keyword&searchType=adv&keyword=data%20scientist&pageNo={k}&sort=r&k=data%20scientist&nignbevent_src=jobsearchDeskGNB&seoKey=data-scientist-jobs-2&src=seo_srp&latLong=&sid=17501426147053681"

  payload = {}
  headers = {
  'accept': 'application/json',
  'accept-language': 'en-US,en;q=0.9',
  'appid': '109',
  'cache-control': 'no-cache',
  'clientid': 'd3skt0p',
  'content-type': 'application/json',
  'gid': 'LOCATION,INDUSTRY,EDUCATION,FAREA_ROLE',
  'nkparam': 'OPcK/5zd986oJ9e2v49g5jSy6p+XxqS6CcTmWV4t9ShrPXX/xxmY9eNUAP5q8Rq8l2LsNp3FU3ZfZSjcnFyQOA==',
  'pragma': 'no-cache',
  'priority': 'u=1, i',
  'referer': 'https://www.naukri.com/data-scientist-jobs-2?k=data+scientist&nignbevent_src=jobsearchDeskGNB',
  'sec-ch-ua': '"Chromium";v="137", "Not/A)Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Linux"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'systemid': 'Naukri',
  'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36',
  'Cookie': '_t_ds=471a8001750142035-12471a800-0471a800; J=0; _ga=GA1.1.1269723706.1750142037; bm_mi=3EFE48A362B31395D728086B8A73888F~YAAQjv7UF5ELs1iXAQAA6XKZfByNDe1N9cnNAYmIBiblQ3PEI1pzUK/tyUse3Rfxs/p03AtxOq+/dITwpBfWdTve8fhs+WfciCTVT0k1Z0CXC58VmROeQlWWTgLCwwYP0keOpEZ1JbImAzwX/i/AFObxYMJVnXILHHIZahTAI8yObHzqJoD+e3ao0a3Spc0KyNtlE3uA8n46NVa2Ms8efEi6w0bnyJcflEb26ePIbwDzjk6nA7s928qqc1nL6ZJUNT9JJfkI3n+doqXJ80t09voulkbsopT2/c5ZhtsqtYxHjTPyKdh+xUp7f9c/lIhg/2kYx2f5xoXyAWwr2ZqcUj7gNhfCkm69rDTLeXk=~1; ak_bmsc=38ADD0C296C3F5552120C803CA165F44~000000000000000000000000000000~YAAQjv7UF68Ls1iXAQAAn3WZfBzy5TVPvjPhNEvtHv9392tij8240Yal1XUeazYh2OOCnFX9lqvnqVbfcB+Q8OEqtFFJY4PZhfKLGAdvx2SnC2sDNdKheUmHamSQEmiMo5lDk3OmrDEEJlb/hnDXw/J6BEuTC3/Jz3xGWMEY5QcnMXU6lgqHGlZw12n+c7hO1QrS8t5SvNGslzSDnfwg4DeeYGULlaLsHNux6bIghLy617f5fGImMS2J6RIc9aDM5Ay3P3+GK4HFhKy7byJa+JO7yxFC76Wy7fUJ1A1gak+pepxLoX7C4aqeWONBhGdmpRcra49sEON3OqOT7zBDznIaYRaI8UFCuVMmIsRCM4lF7QEGM61gLVfrAQnw+sensIu+SulBG0tOoew/nQQfnKDOg7d4Hu1+Z4CplrHdcT9iqQtLzOcrbRW6Cov8geeZ4ynCtoNe9xpZPmXfHueL6uIe3+FdbZhSXwA7NO+1kzE4hbj1YqCQxRE48ufi171yNqqfv5250XLS2kg/seQ=; _gcl_au=1.1.268589570.1750142156; jd=040425501951; __gads=ID=05c2983b9f35a56f:T=1750142037:RT=1750142442:S=ALNI_Ma9PuLTZNl3PB21cBVEzhpAhJmIHA; __gpi=UID=00001130e26a98ef:T=1750142037:RT=1750142442:S=ALNI_MYilS_2Mfv51TLe5ppuzFJkxGYBwA; __eoi=ID=a3e97cd594f5b993:T=1750142037:RT=1750142442:S=AA-AfjauH0yWf7ndTHhOjEjc3S1H; bm_sv=9411D3F0010D336E835363FDBFC00936~YAAQjv7UF8Zms1iXAQAAqj2jfBwVVfTwVGpotSsM5Zct2pUNRdqDqsg/vyMXE4pjvFFAfgDkgFIVqkzu25VFCexRN4J02v/MLwI4rpLOm+IBdVtq29NJG906COqUSvUrgJysnHTXH6sdKZsu2cVhruu6FKSJpgAH8bye1hNE5nOQa6nB53ytxUloT8SCeGJNtG263wCGJI7gsZSjks7Mh81dY5ZXKu26Mhut/xgeBaoQ5mb1JslApnfo7uWHR+3NtQ==~1; _ga_K2YBNZVRLL=GS2.1.s1750142036$o1$g1$t1750142782$j60$l0$h0; HOWTORT=cl=1750142927628&r=https%3A%2F%2Fwww.naukri.com%2Fdata-scientist-jobs%3Fk%3Ddata%2Bscientist%26nignbevent_src%3DjobsearchDeskGNB&nu=https%3A%2F%2Fwww.naukri.com%2Fdata-scientist-jobs-2; J=0; bm_sv=9411D3F0010D336E835363FDBFC00936~YAAQh4nMFwjXL3uXAQAAw1mpfBznqtL4NLo6RDF4penKcXNJf/7fHisG587DTovbN/CaGEsO1yb6fJxsnoRX/dMUmRcf/67DaD4YW3HKZVDvSFc6bqlNK5hu/vQoNTIYoiya306lN1k3Y1O2kKFzLLixb21FO+Fb3wlmX3SkzoXjZLICyvEYoNPwfUo0QHCY39otNZxivkBmVABByT9/fmQFxXkJpQDRR+jVJ70sGUGXcDnObP1JU1fA/OcmspnALA==~1'
  }

  response = requests.request("GET", url, headers=headers, data=payload)

  info_dict = response.json()

  for i in info_dict.get('jobDetails'):
    try:
      staticurl = i.get('staticUrl')
      job_card = {'job_title' : i.get('title'),
      'company_name' : i.get('companyName'),
      'skills' :  i.get('tagsAndSkills'),
      'jobdescription' :  i.get('jobDescription'),
      'staticurl' : ''.join(['https://www.naukri.com/',staticurl]),
      'experince' : i.get('placeholders')[0].get('label'),
      'salary' : i.get('placeholders')[1].get('label'),
      'location' : i.get('placeholders')[2].get('label') if len(i.get('placeholders'))>=3 else np.nan,
      'company_review_count' : i.get('ambitionBoxData').get('ReviewsCount'),
      'company_rating' : i.get('ambitionBoxData').get('AggregateRating') }

      final_table['job_title'].append(job_card.get('job_title',np.nan))
      final_table['company_name'].append(job_card.get('company_name',np.nan))
      final_table['skills'].append(job_card.get('skills',np.nan))
      final_table['jobdescription'].append(job_card.get('jobdescription',np.nan))
      final_table['staticurl'].append(job_card.get('staticurl',np.nan))
      final_table['experince'].append(job_card.get('experince',np.nan))
      final_table['salary'].append(job_card.get('salary',np.nan))
      final_table['location'].append(job_card.get('location',np.nan))
      final_table['company_review_count'].append(job_card.get('company_review_count',np.nan))
      final_table['company_rating'].append(job_card.get('company_rating',np.nan))
    
    except:
      continue
    
    n = n+1

    print(f"page {k} | total {n} items scraped ! ")
  print(f"page {k} scraping complete!")
  st = round(np.random.uniform(0.50,2.00),2)
  print(f"Waiting for {st} sec before next page!")
  time.sleep(st)

DSjobs_Dataset = pd.DataFrame(final_table)

DSjobs_Dataset.to_csv("Database/DSjobs_Dataset.csv",index='False')






