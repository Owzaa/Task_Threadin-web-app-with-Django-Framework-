#!/usr/bin/python

# -*- coding: utf-8 -*-
import StringIO
import xlsxwriter
from .views import allTasks,QuedTasks,DeletedTasks,CreateTasks


def WriteToExcel(allTasks_data,QuedTasks_data,DeletedTasks_data,CreatedTasks_data, allTasks=None):

    output = StringIO.StringIO()

    workbook = xlsxwriter.Workbook(output)

    # adding the code to add data
    title_text = u"{0} {1}".format(ugettext("All TasksHistory for"), title_text, title)

worksheet_s.merge_range('B2:H2', title_text, allTasks_text)



 worksheet_s = workbook.add_worksheet("allTasks")
 
 # Header Columns
  worksheet_s.write(4, 0, ugettext("CreatedTasks"), header)

 worksheet_s.write(4, 1, ugettext("DeletedTasks"), header)

 worksheet_s.write(4, 2, ugettext(u"QuedTasks"), header)


 for idx, data in enumerate(allTasks_data):

    row = 5 + idx

    worksheet_s.write_number(row, 0, idx + 1, cell_center)

    worksheet_s.write_string(row, 1, data.CreatedTasks.name, cell)
worksheet_s.write_string(row, 2, data.DeletedTasks.name, cell)
worksheet_s.write_string(row, 3, data.QuedTasks.name, cell)
  
    worksheet_s.write(row, 4, data.date.strftime('%d/%m/%Y'),     cell_center)
    
    
observations_col_width = 25

for idx, data in enumerate(allTasks_data):

    # ...

    worksheet_s.write_string(row, 3, data.description, cell)

    if len(data.description) > description_col_width:

        description_col_width = len(data.description)

    # ...

worksheet_s.set_column('D:D', description_col_width)


    workbook.close()

    xlsx_data = output.getvalue()

    # xlsx_data contains the Excel file

    return xlsx_data
    
    
   

