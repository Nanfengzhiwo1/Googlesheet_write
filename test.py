import gspread,datetime
from gspread_formatting import *

gc = gspread.service_account(filename='your.json')
sh = gc.open_by_key('yours sheet key')

def get_date():
    date = datetime.date.today().strftime("%Y-%m-%d")
    return date

def adddata_row(type,name,Description,image_list,tab_name):
    worksheet_list = sh.worksheets()
    current_worksheet = None
    date=get_date()

    for sheet in worksheet_list:
        # Traverse sheets,match the tab_name
        if sheet.title == tab_name:
            print(sheet.title)
            current_worksheet = sheet
            current_row=len(current_worksheet.col_values(1))+1

            # Set current row format
            current_worksheet.format("{}:{}".format(current_row,current_row),
                                         {
                                             "horizontalAlignment": "CENTER",
                                             "verticalAlignment": "MIDDLE",                                          
                                            }
                                        )
            image_list_length=len(image_list)
            current_worksheet.append_row([date,type,name,Description],value_input_option='USER_ENTERED')

            # Process multiple images
            for i in range(image_list_length):
                current_worksheet.update_cell(current_row,5+i,'=IMAGE(\"{}\")'.format(image_list[i]))
            
            # Set cell size
            set_row_height(current_worksheet,'{head}:{rear}'.format(head=current_row,rear=current_row),150)
            set_column_width(current_worksheet,'{head}:{rear}'.format(head=chr(65),rear=chr(4+image_list_length-1+65)),250)# number to letter
                     
            break

if __name__ == '__main__':
    Typename='str+multi_image'
    SubmittedBy='Nanfengzhiwo1'
    Description='long long ago,there was a...'
    Image_list=['https://avatars.githubusercontent.com/u/107869748?s=96&v=4','https://avatars.githubusercontent.com/u/107869748?s=96&v=4','https://avatars.githubusercontent.com/u/107869748?s=96&v=4']
    Tab_name='tab5'
    adddata_row(Typename,SubmittedBy,Description,Image_list,Tab_name)
    
