#/bin/env python3
#-*-coding:utf-8-*-

import argparse
import io
import json
import logging
import os
import re
import requests
import sys
import time

from datetime import date, datetime
from subprocess import call
from bs4 import BeautifulSoup

def GetResp(url, headers=None, params=None):
    resp = requests.get(url, timeout=10.0, headers=headers, params=params)
    if resp.status_code == 200:
        return resp
    else:
        print('Get Http Error %d when request url [%s]', resp.status_code, url)

def GenerateTemplate(problem_count, args):
    template_file = None
    if args.language == 'c++17':
        template_file = 'template_cpp17.cc'
    else:
        print('Unsupportted language')
        return 
    for index in range(problem_count):
        call(['cp', template_file, '%s/%s.cc' % (args.contest, str(chr(ord('A') + index)))])
    print("Successfully generate templates")

def GenerateSampleTests(problem_count, args):
    for index in range(problem_count):
        problem_url = "https://codeforces.com/contest/%s/problem/%s" % (args.contest, str(chr(ord('A') + index)))
        problem = GetResp(problem_url)
        if problem == None:
            print("Fail to fetch sample test of problem %s" % str(chr(ord('A') + index)))
            continue
        soup = BeautifulSoup(problem.text, 'html.parser')
        tests = soup.find(class_='sample-test').find_all('pre')
        for u in range(0, len(tests), 2):
            input = tests[u].text[1:]
            output = tests[u + 1].text[1:]
            input_file = open("%s/%s%d.in" % (args.contest, str(chr(ord('a') + index)), u / 2 + 1), "w")
            output_file = open("%s/%s%d.out" % (args.contest, str(chr(ord('a') + index)), u / 2 + 1), "w")
            input_file.write(input)
            output_file.write(output)
            input_file.close()
            output_file.close()
        print("Successfully generate %d sample test(s) for problem %s" % (len(tests) / 2, str(chr(ord('A') + index))))

def Generate(args):
    dashboard_url = "https://codeforces.com/contest/%s" % (args.contest)
    dashboard = GetResp(dashboard_url)
    if dashboard == None:
        return
    soup = BeautifulSoup(dashboard.text, 'html.parser')
    problem_count = str(soup.find(class_="problems")).count('submit') // 2
    print('Totally %d problems found in contest %s' % (problem_count, args.contest))
    call(['mkdir', '-p', args.contest])
    GenerateTemplate(problem_count, args)
    GenerateSampleTests(problem_count, args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Codeforces', description='Codeforces Helper')

    parser.add_argument('--language', '-l', default="c++17", help='The programming language you want to use.')
    parser.add_argument('--contest', '-c', help="The contest you want to play.")
    args = parser.parse_args()

    if args.contest == None:
        print('Contest id shouldn\'t be empty!')
    else:
        Generate(args)