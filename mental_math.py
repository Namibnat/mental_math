#!/usr/bin/env python3

"""
A program to practice simple mental arithmetic
"""

import random
import os
from timeit import default_timer as timer
import json
import datetime
from pathlib import Path

RAISE_ADDITION = 3
MAX_ADDITION = 360
RAISE_SUBTRACTION = 2
MAX_SUBTRACTION = 360
# remember that raising multiplication one is a whole times table
RAISE_MULTIPLICATION = 1
MAX_MULTIPLICATION = 360
RAISE_DIVISION = 2
MAX_DIVISION = 360
RAISE_HEX = 1
MAX_HEX = 360
RAISE_BINARY = 1
MAX_BINARY = 360
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
    else:
        last_results = record[-1]['results']
        last_addition = last_results['+']
        last_subtraction = last_results['-']
        last_multiplication = last_results['*']
        last_division = last_results['/']
        last_hex = last_results['x']
        last_binary = last_results['b']
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

    today_results['+'] = (do_addition(biggest_addition))
    today_results['-'] = (do_subtraction(biggest_subtraction))
    today_results['*'] = (do_multiplication(biggest_multiplication))
    today_results['/'] = (do_division(biggest_division))
    today_results['x'] = (do_hex(biggest_hex))
    today_results['b'] = (do_binary(biggest_binary))
    to_record = {'date': get_date(), 'results': today_results}
    record.append(to_record)
    quiz_record.write_record()


def do_addition(biggest_addition):
    wrong = 0
    wrong_record = []
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
                    wrong_record.append("{a} + {b}")
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
    print("Mistakes:")
    for problem in wrong_record:
        print(problem)
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
    while nums:
        a, b = nums.pop(), nums.pop()
        while True:
            try:
                answer = input("{} * {}: ".format(a, b))
                if int(answer.strip()) == a * b:
                    print("Good")
                else:
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
                    answer = input("To hex {}: ".format(a))
                    if answer == hex(a)[2:]:
                        print("Good")
                    else:
                        print("wrong, should be {}".format(hex(a)[2:]))
                        wrong += 1
                    break
                else:
                    answer = input("To decimal {}: ".format(hex(a)[2:]))
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
                    answer = input("To binary {}: ".format(a))
                    if answer == bin(a)[2:]:
                        print("Good")
                    else:
                        print("wrong, should be {}".format(bin(a)[2:]))
                        wrong += 1
                    break
                else:
                    answer = input("To decimal {}: ".format(bin(a)[2:]))
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


if __name__ == "__main__":
    clear = ('cls' if os.name == 'nt' else 'clear')
    os.system(clear)
    runall()
