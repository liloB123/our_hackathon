from pywebio.input import *
from pywebio.input import *
from pywebio.output import *
from pywebio import start_server
import re
subject = []
education_level = []
grade = []
sub_subject = [[]]
dict1 = {}
def input_upload_summary():
    input_upload_summary = input_group(select("subject", subject, name= 'input_subject', required=True),
    textarea('sub_subject', rows=1, name= 'input_sub_subject', required=True),
    select("education_level", education_level, name= 'input_education_level', required=True),
    select("subject", grade, name= 'input_class', required=True),
    file_upload('summary', placeholder='Choose file', accept='image/*',name= 'summary_upload', required=True)
                                       )
    return input_subject, input_sub_subject, input_education_level, input_class
input_subject, input_sub_subject, input_education_level, input_class = input_upload_summary()

def added_description_list():
    for i in range(len(subject)):
        if input_subject == subject[i]:
            sub_subject[i].append(input_subject)

def input_search_summary():




# def input_test_input_sub_subject():
#     # if input_sub_subject == '':
#     #     input_sub_subject = 'כללי'
#     input_sub_subject = input('sub_subject')
#     while len(input_sub_subject) < 20:
#         print('more then 20 letters')
#         print('input_sub_subject')
#         input_sub_subject = input('sub_subject')
#     return input_sub_subject





def search_subject():
    input_search_subject = input('search subject')
    for i in subject:
        for letter in i:
            # r = re.compile("^[a-z]{1,15}$")
def put_sub_subject():






for i in range(len(subject)):
    dict1[subject[i]] = []
    # dict1[subject[i]] = sub_subject[i]
