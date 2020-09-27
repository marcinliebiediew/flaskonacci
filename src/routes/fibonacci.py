import math
from datetime import datetime
from functools import lru_cache
from typing import List

from flask import Blueprint, abort, jsonify, request

from src.extensions import db
from src.models import Logs

fibonacci_bp = Blueprint('fibonacci', __name__)


@fibonacci_bp.route('/fib/<int:number>')
def python_fib(number: int) -> str:
    data = str(subset_sum_from_fibonacci_set(number))
    log = Logs(path_and_method=f"{request.method} {request.path}",
               request_data=number,
               response_data=data)
    db.session.add(log)
    db.session.commit()
    return data


def subset_sum_from_fibonacci_set(target_number: int) -> List[List[int]]:
    valid_numbers = []
    for e in range(target_number + 1):
        if 0 < (v := fibonacci(e)) <= target_number:
            valid_numbers.append(v)
        elif v > target_number:
            break
    return list(subset_sum(valid_numbers, target_number))


@lru_cache(maxsize=100)
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def subset_sum(numbers: List[int], target: int, partial=[], partial_sum=0):
    """
        https://stackoverflow.com/a/34519260/7432829 - it's nicer than what I came up with :(
        I tried to do it with dynamic programming (pseudo-polynomial complexity),
            but couldn't make it work to return all possible subsets, not just one.
    """
    if partial_sum == target:
        yield partial
    if partial_sum >= target:
        return
    for i, n in enumerate(numbers):
        remaining = numbers[i + 1:]
        yield from subset_sum(remaining, target, partial + [n],
                              partial_sum + n)
