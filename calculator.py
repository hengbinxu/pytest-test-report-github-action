from typing import Tuple, Optional
from typing_extensions import Self

Num = float | int


class Calculator:
    def __init__(self, init_num: Optional[Num] = None) -> None:
        self.result = init_num if init_num else 0

    def add(self, *nums: Tuple[Num, ...]) -> Self:
        for num in nums:
            self.result += num
        return self

    def subtract(self, *nums: Tuple[Num, ...]) -> Self:
        for num in nums:
            self.result -= num
        return self

    def multiply(self, *nums: Tuple[Num, ...]) -> Self:
        for num in nums:
            self.result *= num
        return self

    def divide(self, num: Num) -> Self:
        try:
            self.result /= num
        except ZeroDivisionError:
            print("Divisor can't be 0")
        return self

    def reset(self) -> Self:
        self.set_result(0)
        return self

    def get_result(self) -> Num:
        return self.result

    def set_result(self, num: Num) -> Self:
        self.result = num
        return self
