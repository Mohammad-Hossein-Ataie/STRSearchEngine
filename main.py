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
