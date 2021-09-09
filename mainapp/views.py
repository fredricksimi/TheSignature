from django.shortcuts import render

# Create your views here.
# def home_view(request):
#     return render(request, 'mainapp/index.html')

import base64
from django.shortcuts import render
import json
import requests
from requests.structures import CaseInsensitiveDict

def get_data():
    # url = "http://192.168.100.216:81/api/apiLogin"
    url = "https://hrmis.zalegoacademy.ac.ke/zalegoemp/public/api/apiLogin"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"
    data = "email=fkemosi@gmail.com&password=@Voldermort1997"
    resp = requests.post(url, headers=headers, data=data)

    my_token = json.loads(resp.text)
    token =my_token["token"]


    # url_2 = "http://192.168.100.216:81/api/apiData"
    url_2 = "https://hrmis.zalegoacademy.ac.ke/zalegoemp/public/api/apiData"
    headers = CaseInsensitiveDict()
    headers["Authorization"] = f"Bearer {token}"
    resp = requests.get(url_2, headers=headers)
    our_json_data = resp.text
    return json.loads(our_json_data)



# def index(request):
#     id = 'ZAL-001'
#     employees = get_data()
#     for employee in employees:
#         if employee['Employee Id'] == id:
#             print(employee)
#     return render(request, 'mainapp/index.html',{'employee':employee})


def home_view(request, empid):
    id = empid
    employees = get_data()

    for employee in employees:
        if employee['Employee Id'] == id:
            emp_data = {
                'full_name' : employee['Full Name'],
                'employee_id' : employee['Employee Id'],
                'company' : employee['Company'],
                'designation' : employee['Designation'],
                'department' : employee['Department'],
                'job_title' : employee['Job Title'],
                'phone_number' : employee['Phone Number'],
                'email' : employee['Email'],
                # 'location' : employee['Loacation'],
                # 'photo' : employee['photo']
            }
            if employee['Company'] == 'Zalda Company':
                companyLogo = "https://github.com/Zalego-development/CompanyLogos/blob/main/zaldacropped.png?raw=true"
                website = "www.zalda.com"
            elif employee['Company'] == 'Zalego Academy':
                companyLogo = "https://github.com/Zalego-development/CompanyLogos/blob/main/zalegocropped.png?raw=true"
                website = "www.zalegoacademy.ac.ke"
            elif employee['Company'] == 'DAPROIM AFRICA LIMITED' or employee['Company'] == 'StepWise':
                companyLogo = "https://github.com/Zalego-development/CompanyLogos/blob/main/stepwisecropped.png?raw=true"
                website = "stepwise.net"
            elif employee['Company'] == 'NEXT STEP FOUNDATION':
                companyLogo = "https://github.com/Zalego-development/CompanyLogos/blob/main/nextcropped.png?raw=true"

            if employee['photo'][-9:] == 'admin.png':
                photo = "https://github.com/Zalego-development/CompanyLogos/blob/main/placeholder-hi.png?raw=true"
            else:
                photo = employee['photo']
                
            print(employee['photo'][-9:])
            context = {'employee': emp_data, 'companyLogo':companyLogo, 'website':website, 'photo':photo}
    
    return render(request, 'mainapp/index.html',context)