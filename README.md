# Prompt
- Python Version: Python 3.11.2
- gspread:[Docs](https://docs.gspread.org/en/latest/)
- gspread-formatting:[Docs](https://pypi.org/project/gspread-formatting/)
- service account.json:[How to get json file](https://docs.gspread.org/en/latest/oauth2.html#enable-api-access-for-a-project)
- sheet open key:[where is key](https://github.com/Nanfengzhiwo1/googlesheet_write/assets/107869748/520c7be3-2a87-425b-aa59-5528df7cf13a)

# How to Start
1.`pip install gspread`,`pip install gspread-formatting` 

2.create a sheet and rename it,input 5 titles in the first row
![image](https://github.com/Nanfengzhiwo1/googlesheet_write/assets/107869748/34db52d8-eafa-41f8-93fd-7436006ebb0b)
### About cell title 

> 1. *There are 5 titles, but **date** will auto write*.  
> 2. ***Images**,it can have multiple pictures or no pictures*.  
> 3. *After modifying the code,you can change the title to what you want*.


3.replace parameters in python file,**[your.json](https://docs.gspread.org/en/latest/oauth2.html#enable-api-access-for-a-project)**,**yours sheet key[https://github.com/Nanfengzhiwo1/googlesheet_write/assets/107869748/520c7be3-2a87-425b-aa59-5528df7cf13a]**,**Typename**,**SubmittedBy**,**Description**,**Image_list** and **Tab_name**
![image](https://github.com/Nanfengzhiwo1/googlesheet_write/assets/107869748/85f78ae9-74f1-4310-9275-ea0201ab4538)
![image](https://github.com/Nanfengzhiwo1/googlesheet_write/assets/107869748/b52e6ea8-9840-4639-a0ef-8aaced5bde4b)


4.run `python test.py`,add a row

# Preview

![image](https://github.com/Nanfengzhiwo1/googlesheet_write/assets/107869748/ffe6b257-e533-4e0d-9099-a1c648a15bad)







