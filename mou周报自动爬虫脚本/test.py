# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 00:36:50 2018

@author: WuFan
"""
import subprocess
import json


#r = subprocess.Popen('./test.sh > result.txt')
def txt_to_list():
    result_file = "result.txt"
    result_list = []
    with open(result_file,"r",encoding="UTF-8") as f:

        for line in f:
            #print("---------------------")
            line = line.replace("/n","").strip()
            line_json = json.loads(line)
            a_day_data = line_json["d"].strip().split("],[")
            singal_data_list = []
            for each in a_day_data:
                singal_data_list.append(each.strip("[[").strip("]]").strip('').replace('"',"").split(","))
            result_list.append(singal_data_list)
    return result_list

def get_result(result_list):
    dic_of_target = ["PTA内盘","MEG内盘","半光切片","江浙涤短","涤纶FDY68D","涤纶DTY",
                     "氨纶40D","Cotlook","CCIndex","华东棉浆","粘短1.5D","粘长120D","CPL内盘","锦纶切片","锦纶FDY","锦纶DTY"]
    for each_kind_data in result_list:
        #print(each_kind_data)
        print("--------------------------------------")
        for each_singal_data in each_kind_data:
            if each_singal_data[1] in dic_of_target:
                #print(each_singal_data)
                print(each_singal_data[1],"  ❥  ",each_singal_data[2],"  ❥ ",each_singal_data[-1])

get_result(txt_to_list())
