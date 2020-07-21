#!/usr/bin/env python3

"""
A program to practice simple mental arithmetic
"""

import random
import os
from timeit import default_timer as timer
import json
import csv
import datetime
from pathlib import Path

RAISE_ADDITION = 3
MAX_ADDITION = 240
RAISE_SUBTRACTION = 2
MAX_SUBTRACTION = 240
# remember that raising multiplication one is a whole times table
RAISE_MULTIPLICATION = 1
MAX_MULTIPLICATION = 240
RAISE_DIVISION = 2
MAX_DIVISION = 240
RAISE_HEX = 1
MAX_HEX = 240
RAISE_BINARY = 1
MAX_BINARY = 240
RAISE_PERIODIC_TABLE = 1
MAX_PERIODIC_TABLE = 360
RAISE_2TH_POWER = 1
MAX_2TH_POWER = 240
ROUNDS = 100


class QuizRecord:
    def __init__(self):
        self.filename = f"{Path.home()}/.mental_math/record.json"
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
    today = datetime.datetime.now()
    return "{}.{}.{}".format(today.day, today.month, today.year)


def runall():
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
    else:
        last_results = record[-1]['results']
        last_addition = last_results['+']
        last_subtraction = last_results['-']
        last_multiplication = last_results['*']
        last_division = last_results['/']
        last_hex = last_results['x']
        last_binary = last_results['b']
        last_periodic_table = last_results['p']
        try:
            last_2th_power = last_results['2']
        except KeyError:
            biggest_2th_power = 4
            last_2th_power = {}
            last_2th_power['wrong'] = 1
            last_2th_power['it_took'] = MAX_2TH_POWER
            last_2th_power['biggest'] = biggest_2th_power
        if (last_addition['wrong'] == 0 and
                last_addition['it_took'] < MAX_ADDITION):
            biggest_addition = last_addition['biggest'] + RAISE_ADDITION
            print(f"Biggest addition raised to {biggest_addition}")
        else:
            biggest_addition = last_addition['biggest']
        if (last_subtraction['wrong'] == 0 and
                last_subtraction['it_took'] < MAX_SUBTRACTION):
            biggest_subtraction = (last_subtraction['biggest'] +
                                   RAISE_SUBTRACTION)
            print(f"Biggest subtraction raised to {biggest_subtraction}")
        else:
            biggest_subtraction = last_subtraction['biggest']
        if (last_multiplication['wrong'] == 0 and
                last_multiplication['it_took'] < MAX_MULTIPLICATION):
            biggest_multiplication = (last_multiplication['biggest'] +
                                      RAISE_MULTIPLICATION)
            print(f"Biggest multiplication raised to {biggest_multiplication}")
        else:
            biggest_multiplication = last_multiplication['biggest']
        if (last_division['wrong'] == 0 and
                last_division['it_took'] < MAX_DIVISION):
            biggest_division = last_division['biggest'] + RAISE_DIVISION
            print(f"Biggest division raised to {biggest_division}")
        else:
            biggest_division = last_division['biggest']
        if (last_hex['wrong'] == 0 and
                last_hex['it_took'] < MAX_HEX):
            biggest_hex = last_hex['biggest'] + RAISE_HEX
            print(f"Biggest hex raised to {biggest_hex}")
        else:
            biggest_hex = last_hex['biggest']
        if (last_binary['wrong'] == 0 and
                last_binary['it_took'] < MAX_BINARY):
            biggest_binary = last_binary['biggest'] + RAISE_BINARY
            print(f"Biggest binary raised to {biggest_binary}")
        else:
            biggest_binary = last_binary['biggest']
        if (last_periodic_table['wrong'] == 0 and
                last_periodic_table['it_took'] < MAX_PERIODIC_TABLE):
            biggest_periodic_table = last_periodic_table['biggest'] + RAISE_PERIODIC_TABLE
            print(f"Biggest periodic table raised to {biggest_periodic_table}")
        else:
            biggest_periodic_table = last_periodic_table['biggest']
        if (last_2th_power['wrong'] == 0 and
                last_2th_power['it_took'] < MAX_2TH_POWER):
            biggest_2th_power = last_2th_power['biggest'] + RAISE_2TH_POWER
            print(f"Biggest 2th power raised to {biggest_2th_power}")
        else:
            biggest_2th_power = last_2th_power['biggest']

    today_results['+'] = (do_addition(biggest_addition))
    today_results['-'] = (do_subtraction(biggest_subtraction))
    today_results['*'] = (do_multiplication(biggest_multiplication))
    today_results['/'] = (do_division(biggest_division))
    today_results['x'] = (do_hex(biggest_hex))
    today_results['b'] = (do_binary(biggest_binary))
    today_results['p'] = (do_periodic_table(biggest_periodic_table))
    today_results['2'] = (do_2th_power(biggest_2th_power))
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
    input("Press enter to start binary: ")
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


if __name__ == "__main__":
    clear = ('cls' if os.name == 'nt' else 'clear')
    os.system(clear)
    runall()
