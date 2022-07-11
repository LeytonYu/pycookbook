import json

import openpyxl

with open('raw_data', 'rt', encoding='utf8') as f:
  data = json.loads(f.read())

workbook = openpyxl.Workbook()
sheet = workbook.active
head = {
  'GGBT': '标题',
  'GWFBSJ': '岗位发布时间',
  'YJZJS': '简介',
  'GWMC': '岗位名称',
  'GWRS': '岗位人数',
  'GWZZ': '岗位职责',
  'ZPTJ': '招聘条件',
  'GZTJYGZDY': '工作条件与工资待遇',
  'YPFS': '应聘方式',
}


def do_it():
  for obj in data:
    tp = obj.pop('DATA')
    obj.update(tp[0])

  head_list = list(head.values())
  sheet.append(head_list)
  for line_dict in data:
    sheet.append([str(line_dict.get(k)) if line_dict.get(k) else '' for k in head.keys()])

  workbook.save('上海科技大学人才招聘.xlsx')


if __name__ == '__main__':
  do_it()
