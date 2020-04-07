#!/usr/bin/env python3.7

"""
A program to practice simple mental arithmetic
"""

import random
from timeit import default_timer as timer
import json
import datetime

RAISE_ADDITION = 10
MAX_ADDITION = 180
RAISE_SUBTRACTION = 5
MAX_SUBTRACTION = 240
RAISE_MULTIPLICATION = 3
MAX_MULTIPLICATION = 240
RAISE_DIVISION = 2
MAX_DIVISION = 300
ROUNDS = 100


class QuizRecord:
    def __init__(self):
        self.filename = "/home/vernon/.mental_math/record.json"
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
    else:
        last_results = record[-1]['results']
        last_addition = last_results['+']
        last_subtraction = last_results['-']
        last_multiplication = last_results['*']
        last_division = last_results['/']
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

    today_results['+'] = (do_addition(biggest_addition))
    today_results['-'] = (do_subtraction(biggest_subtraction))
    today_results['*'] = (do_multiplication(biggest_multiplication))
    today_results['/'] = (do_division(biggest_division))
    # division = do_devision()
    to_record = {'date': get_date(), 'results': today_results}
    record.append(to_record)
    quiz_record.write_record()


def do_addition(biggest_addition):
    wrong = 0
    nums = [random.randint(2, biggest_addition) for n in range(ROUNDS)]
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
    nums = [random.randint(2, biggest_subtraction) for n in range(ROUNDS)]
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
    nums = [random.randint(2, biggest_multiplication) for n in range(ROUNDS)]
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
    nums = [random.randint(2, biggest_division) for n in range(ROUNDS)]
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


if __name__ == "__main__":
    runall()
