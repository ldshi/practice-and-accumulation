#
## python --version -> Python 2.7.10
#

records = {}

first_line = raw_input().strip().split(' ')

counter = int(first_line[0])
districts_number = int(first_line[1])

while counter > 0:
  record = raw_input().strip().split(' ')
  if record[1] in records.keys():
    records[record[1]][record[0]] = record[2]
    records[record[1]]['_grades'].append(int(record[2]))
  else:
    records[record[1]] = {
      record[0]: record[2],
      '_grades': [int(record[2])]
    }

  counter -= 1

  

district = 1
while district <= districts_number:
  key = str(district)

  highest_grade = max(records[key]['_grades'])
  how_many = records[key]['_grades'].count(highest_grade)

  if how_many > 2:
    print '?'
  elif how_many == 2:
    tmp = []
    for surname in records[key]:
      if surname != '_grades' and records[key][surname] == str(highest_grade):
        tmp.append(surname)
        if len(tmp) == 2:
          print ' '.join(tmp)
          break
  else:
    records[key]['_grades'].remove(highest_grade)
    secondary_highest_grade = max(records[key]['_grades'])
    how_many = records[key]['_grades'].count(secondary_highest_grade)

    tmp = []
    for surname in records[key]:
      if surname != '_grades':
        if records[key][surname] == str(highest_grade):
          tmp.append(surname)
        elif records[key][surname] == str(secondary_highest_grade):
          if how_many > 1:
            tmp.append('?')
          else:
            tmp.append(surname)

        if len(tmp) == 2:
          print ' '.join(tmp)
          break

  district += 1


