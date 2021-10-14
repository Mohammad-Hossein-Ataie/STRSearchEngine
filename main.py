import re
import csv
import sys
from pathlib import Path

print("Well come!")
print("Enter any word you want:")
words = input().split(",")


def Program(srt):
    with open(srt, "r", encoding='cp1252') as h:
        sub = h.readlines()
    re_pattern = r'[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3} -->'
    regex = re.compile(re_pattern)
    # Get start times
    start_times = list(filter(regex.search, sub))
    start_times = [time.split(' ')[0] for time in start_times]
    # Get lines
    lines = [[]]
    for sentence in sub:
        if re.match(re_pattern, sentence):
            lines[-1].pop()
            lines.append([])
        else:
            lines[-1].append(sentence)
    lines = lines[1:]
    subs = {start_time: line for start_time, line in zip(start_times, lines)}

    with open('output.csv', 'a+', encoding='cp1252') as output:
        writer = csv.writer(output)
        for key, value in subs.items():
            writer.writerow([key, value])
    csv_file = csv.reader(open('output.csv', "r"), delimiter=",")
    output.close()
    with open('result.csv', mode='a+', encoding='cp1252') as result:
        result = csv.writer(result, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for row in csv_file:
            for x in range(len(words)):
                if any(words[x] in s for s in row):
                    row.append(words[x])
                    row.append(str(srt).replace(
                        'D:\\03-My movies\\02-EnSubtitle\ ', ''))
                    result.writerow(row)
