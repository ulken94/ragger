import numpy as np

# main.py 예시

def calculate_area(width: float, height: float) -> float:
    """사각형의 넓이를 계산합니다.

    Args:
        width (float): 사각형의 가로 길이.
        height (float): 사각형의 세로 길이.

    Returns:
        float: 계산된 사각형의 넓이.

    Raises:
        ValueError: width나 height가 음수일 경우 발생합니다.

    Example:
        >>> calculate_area(10, 5)
        50.0
    """
    if width < 0 or height < 0:
        raise ValueError("Dimensions must be positive")
    return width * height

def add(a, b):
    return a + b


def main():
    print("Hello from uv-template!")


if __name__ == "__main__":
    main()
