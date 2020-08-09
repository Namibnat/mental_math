#!/usr/bin/env python3

"""
Mental workout routine

A simple routine to run
through a few different mental
challenges, mostly math and chemistry
"""

import random
import os
from timeit import default_timer as timer
import json
import csv
import datetime
from pathlib import Path

RECORD_FILE = f"{Path.home()}/.mental_math/record.json"

RAISE = 1
MAX_ADDITION = 240
MAX_SUBTRACTION = 240
MAX_MULTIPLICATION = 240
MAX_DIVISION = 240
MAX_HEX = 240
MAX_BINARY = 240
MAX_PERIODIC_TABLE = 240
MAX_2TH_POWER = 240
MAX_16TH_POWER = 240
ROUNDS = 100


class QuizRecord:
    """Keep score"""
    def __init__(self):
        self.filename = RECORD_FILE
        try:
            record_fp = open(self.filename, 'r')
            self.record = json.load(record_fp)
            record_fp.close()
        except FileNotFoundError:
            self.record = []

    def write_record(self):
        record_fp = open(self.filename, 'w')
        json.dump(self.record, record_fp)
        record_fp.close()


def get_date():
    """Returns date in the form dd.mm.yyyy"""
    today = datetime.datetime.now()
    return "{}.{}.{}".format(today.day, today.month, today.year)


def biggest_helper(last, max, item):
    """Set the biggest value for the problem set"""
    if (last['wrong'] == 0 and last['it_took'] < max):
        biggest = last['biggest'] + RAISE
        print(f"Biggest {item} raised to {biggest}")
    else:
        biggest = last['biggest']
    return biggest


def last_helper(last_results, item, biggest):
    """Determine the last values

    If there was no last value for this entry,
    it gets created
    """
    try:
        last = last_results[item]
    except KeyError:
        last = {}
        last['wrong'] = 1
        last['it_took'] = MAX_16TH_POWER
        last['biggest'] = biggest
    return last


def runall():
    """Sets all the needed parameters, then runs all the quizes"""
    today_results = {}
    quiz_record = QuizRecord()
    record = quiz_record.record
    if not record:
        biggest_addition = 10
        biggest_subtraction = 9
        biggest_multiplication = 8
        biggest_division = 7
        biggest_hex = 11
        biggest_binary = 3
        biggest_periodic_table = 3
        biggest_2th_power = 4
        biggest_16th_power = 2
    else:
        last_results = record[-1]['results']
        last_addition = last_helper(last_results, '+', 10)
        last_subtraction = last_helper(last_results, '-', 9)
        last_multiplication = last_helper(last_results, '*', 8)
        last_division = last_helper(last_results, '/', 7)
        last_hex = last_helper(last_results, 'x', 11)
        last_binary = last_helper(last_results, 'b', 3)
        last_periodic_table = last_helper(last_results, 'p', 3)
        last_2th_power = last_helper(last_results, '2', 4)
        last_16th_power = last_helper(last_results, '16', 2)

        biggest_addition = biggest_helper(last_addition, MAX_ADDITION, 'addition')
        biggest_subtraction = biggest_helper(last_subtraction,
                                             MAX_SUBTRACTION, 'subtraction')
        biggest_multiplication = biggest_helper(last_multiplication,
                                                MAX_MULTIPLICATION, 'multiplication')
        biggest_division = biggest_helper(last_division, MAX_DIVISION, 'division')
        biggest_hex = biggest_helper(last_hex, MAX_HEX, 'hex')
        biggest_binary = biggest_helper(last_binary, MAX_BINARY, 'binary')
        biggest_periodic_table = biggest_helper(last_periodic_table,
                                                MAX_PERIODIC_TABLE,
                                                'periodic table')
        biggest_2th_power = biggest_helper(last_2th_power,
                                           MAX_2TH_POWER, '2nd power')
        biggest_16th_power = biggest_helper(last_16th_power,
                                            MAX_16TH_POWER, '16th power')

    today_results['+'] = (do_addition(biggest_addition))
    today_results['-'] = (do_subtraction(biggest_subtraction))
    today_results['*'] = (do_multiplication(biggest_multiplication))
    today_results['/'] = (do_division(biggest_division))
    today_results['x'] = (do_hex(biggest_hex))
    today_results['b'] = (do_binary(biggest_binary))
    today_results['p'] = (do_periodic_table(biggest_periodic_table))
    today_results['2'] = (do_2th_power(biggest_2th_power))
    today_results['16'] = (do_16th_power(biggest_16th_power))
    to_record = {'date': get_date(), 'results': today_results}
    record.append(to_record)
    quiz_record.write_record()


def do_addition(biggest_addition):
    wrong = 0
    nums = [random.randint(2, biggest_addition) for n in range(2 * ROUNDS)]
    input("Press enter to start addition: ")
    start = timer()
    while nums:
        a, b = nums.pop(), nums.pop()
        while True:
            try:
                answer = input("{} + {}: ".format(a, b))
                if int(answer.strip()) == a + b:
                    print("Good")
                else:
                    print("wrong, should be {}".format(a + b))
                    wrong += 1
                break
            except ValueError:
                print("The value you entered didn't work, try again")
    end = timer()
    it_took = round(end - start)
    minutes, seconds = [it_took // 60, it_took % 60]
    print("{} wrong and it took {} minutes and {} seconds".format(
        wrong,
        minutes,
        seconds,
        )
    )
    return {
        'biggest': biggest_addition,
        'wrong': wrong,
        'it_took': it_took,
    }


def do_subtraction(biggest_subtraction):
    """
    Run a 100 subtraction sums, up to a biggest value
    """
    wrong = 0
    nums = [random.randint(2, biggest_subtraction) for n in range(2 * ROUNDS)]
    input("Press enter to start subtraction: ")
    start = timer()
    while nums:
        a, b = nums.pop(), nums.pop()
        a, b = sorted((a, b), reverse=True)
        while True:
            try:
                answer = input("{} - {}: ".format(a, b))
                if int(answer.strip()) == a - b:
                    print("Good")
                else:
                    print("wrong, should be {}".format(a - b))
                    wrong += 1
                break
            except ValueError:
                print("The value you entered wasn't a number, try again")
    end = timer()
    it_took = round(end - start)
    minutes, seconds = [it_took // 60, it_took % 60]
    print("{} wrong and it took {} minutes and {} seconds".format(
        wrong,
        minutes,
        seconds,
        )
    )
    return {
        'biggest': biggest_subtraction,
        'wrong': wrong,
        'it_took': it_took,
    }


def do_multiplication(biggest_multiplication):
    """
    Run a 100 multiplication sums, up to a biggest value
    """
    wrong = 0
    nums = [random.randint(2, biggest_multiplication) for n in range(2 * ROUNDS)]
    input("Press enter to start multiplication: ")
    start = timer()
    wrong_record = []
    while nums:
        a, b = nums.pop(), nums.pop()
        while True:
            try:
                answer = input("{} * {}: ".format(a, b))
                if int(answer.strip()) == a * b:
                    print("Good")
                else:
                    wrong_record.append(f"{a} x {b}")
                    print("wrong, should be {}".format(a * b))
                    wrong += 1
                break
            except ValueError:
                print("The value you typed wasn't a proper answer, try again")
    end = timer()
    it_took = round(end - start)
    minutes, seconds = [it_took // 60, it_took % 60]
    print("{} wrong and it took {} minutes and {} seconds".format(
        wrong,
        minutes,
        seconds,
        )
    )
    if wrong_record:
        print("\nMistakes:")
        for problem in wrong_record:
            print(problem)
    return {
        'biggest': biggest_multiplication,
        'wrong': wrong,
        'it_took': it_took,
    }


def do_division(biggest_division):
    """
    Run a 100 division sums, up to a biggest value
    """
    wrong = 0
    nums = [random.randint(2, biggest_division) for n in range(2 * ROUNDS)]
    print("For division, if there is a remainder, put a space then remainder")
    input("Press enter to start division: ")
    start = timer()
    while nums:
        a, b = nums.pop(), nums.pop()
        a, b = sorted((a, b), reverse=True)
        while True:
            try:
                answer = input("{} / {}: ".format(a, b))
                if a % b:
                    floor, remainder = answer.strip().split(" ")
                else:
                    floor = answer
                    remainder = '0'
                if (int(floor.strip()) == a // b and
                        int(remainder.strip()) == a % b):
                    print("Good")
                else:
                    print("wrong, should be {} remainder {}".format(a // b,
                                                                    a % b))
                    wrong += 1
                break
            except ValueError:
                print("Your input wasn't a a correct answer, try again")
    end = timer()
    it_took = round(end - start)
    minutes, seconds = [it_took // 60, it_took % 60]
    print("{} wrong and it took {} minutes and {} seconds".format(
        wrong,
        minutes,
        seconds,
        )
    )
    return {
        'biggest': biggest_division,
        'wrong': wrong,
        'it_took': it_took,
    }


def do_hex(biggest_hex):
    wrong = 0
    nums = [random.randint(8, biggest_hex) for n in range(ROUNDS)]
    input("Press enter to start hex: ")
    start = timer()
    while nums:
        a = nums.pop()
        while True:
            try:
                flip = random.randint(0, 1)
                # decimal to hex
                if flip:
                    answer = input("{} in decimal, to hex: ".format(a))
                    if answer == hex(a)[2:]:
                        print("Good")
                    else:
                        print("wrong, should be {}".format(hex(a)[2:]))
                        wrong += 1
                    break
                else:
                    answer = input("{} in hex, to decimal: ".format(hex(a)[2:]))
                    if answer == str(a):
                        print("Good")
                    else:
                        print("wrong, should be {}".format(a))
                        wrong += 1
                    break

            except ValueError:
                print("The value you entered didn't work, try again")
    end = timer()
    it_took = round(end - start)
    minutes, seconds = [it_took // 60, it_took % 60]
    print("{} wrong and it took {} minutes and {} seconds".format(
        wrong,
        minutes,
        seconds,
        )
    )
    return {
        'biggest': biggest_hex,
        'wrong': wrong,
        'it_took': it_took,
    }


def do_binary(biggest_binary):
    wrong = 0
    nums = [random.randint(0, biggest_binary) for n in range(ROUNDS)]
    input("Press enter to start binary: ")
    start = timer()
    while nums:
        a = nums.pop()
        while True:
            try:
                flip = random.randint(0, 1)
                if flip:
                    answer = input("{} in decimal, to binary: ".format(a))
                    if answer == bin(a)[2:]:
                        print("Good")
                    else:
                        print("wrong, should be {}".format(bin(a)[2:]))
                        wrong += 1
                    break
                else:
                    answer = input("{} in binary, to decimal: ".format(bin(a)[2:]))
                    if answer == str(a):
                        print("Good")
                    else:
                        print("wrong, should be {}".format(a))
                        wrong += 1
                    break

            except ValueError:
                print("The value you entered didn't work, try again")
    end = timer()
    it_took = round(end - start)
    minutes, seconds = [it_took // 60, it_took % 60]
    print("{} wrong and it took {} minutes and {} seconds".format(
        wrong,
        minutes,
        seconds,
        )
    )
    return {
        'biggest': biggest_binary,
        'wrong': wrong,
        'it_took': it_took,
    }


def do_periodic_table(biggest_periodic_table):
    # The period table I'm using goes to 118, so setting explicit top val
    if biggest_periodic_table > 118:
        biggest_periodic_table = 118
    wrong = 0
    ptable = []
    with open("periodic_table.csv", "r") as pt_file:
        pt_data = list(csv.reader(pt_file, delimiter=","))
        for row in pt_data[:biggest_periodic_table]:
            ptable.append((row[1], row[2]))
    del ptable[0]  # This is just deleting the titles
    elements = [random.choice(ptable) for n in range(ROUNDS)]
    input("Press enter to start periodic table: ")
    start = timer()
    while elements:
        a = elements.pop()
        while True:
            try:
                flip = random.randint(0, 1)
                if flip:
                    answer = input("To element symbol {}: ".format(a[0]))
                    if answer == str(a[1]):
                        print("Good")
                    else:
                        print("wrong, should be {}".format(a[1]))
                        wrong += 1
                    break
                else:
                    answer = input("To element name {}: ".format(a[1]))
                    if answer == str(a[0]):
                        print("Good")
                    else:
                        print("wrong, should be {}".format(a[0]))
                        wrong += 1
                    break

            except ValueError:
                print("The value you entered didn't work, try again")
    end = timer()
    it_took = round(end - start)
    minutes, seconds = [it_took // 60, it_took % 60]
    print("{} wrong and it took {} minutes and {} seconds".format(
        wrong,
        minutes,
        seconds,
        )
    )
    return {
        'biggest': biggest_periodic_table,
        'wrong': wrong,
        'it_took': it_took,
    }


def do_2th_power(biggest_2th_power):
    wrong = 0
    nums = [random.randint(0, biggest_2th_power) for n in range(ROUNDS)]
    input("Press enter to start 2-powers: ")
    start = timer()
    while nums:
        try:
            a = nums.pop()
            answer = input("2^{}: ".format(a))
            if answer == str(2**a):
                print("Good")
            else:
                print("Wrong, should be {}".format(2**a))
                wrong += 1
        except ValueError:
            print("The value you entered didn't work, try again")
    end = timer()
    it_took = round(end - start)
    minutes, seconds = [it_took // 60, it_took % 60]
    print("{} wrong and it took {} minutes and {} seconds".format(
        wrong,
        minutes,
        seconds,
        )
    )
    return {
        'biggest': biggest_2th_power,
        'wrong': wrong,
        'it_took': it_took,
    }


def do_16th_power(biggest_16th_power):
    wrong = 0
    nums = [random.randint(0, biggest_16th_power) for n in range(ROUNDS)]
    input("Press enter to start 16-powers: ")
    start = timer()
    while nums:
        try:
            a = nums.pop()
            answer = input("16^{}: ".format(a))
            if answer == str(16**a):
                print("Good")
            else:
                print("Wrong, should be {}".format(16**a))
                wrong += 1
        except ValueError:
            print("The value you entered didn't work, try again")
    end = timer()
    it_took = round(end - start)
    minutes, seconds = [it_took // 60, it_took % 60]
    print("{} wrong and it took {} minutes and {} seconds".format(
        wrong,
        minutes,
        seconds,
        )
    )
    return {
        'biggest': biggest_16th_power,
        'wrong': wrong,
        'it_took': it_took,
    }


if __name__ == "__main__":
    clear = ('cls' if os.name == 'nt' else 'clear')
    os.system(clear)
    runall()
