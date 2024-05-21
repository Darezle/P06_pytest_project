from calculator.calculator import Calculator

def test_add():
    # arrange
    a = 4321
    b = 1234
    cal = Calculator()

    # act
    result = cal.add(a, b)

    # assert
    expected = 5555
    assert result == expected

def test_subtract():
    # arrange
    a = 4321
    b = 1234
    cal = Calculator()

    # act
    result = cal.subtract(a, b)

    # assert
    expected = 3087
    assert result == expected

def test_multiply():
    # arrange
    a = 4
    b = 12
    cal = Calculator()

    # act
    result = cal.multiply(a, b)

    # assert
    expected = 48
    assert result == expected

def test_divide():
    # arrange
    a = 12
    b = 4
    cal = Calculator()

    # act
    result = cal.divide(a, b)

    # assert
    expected = 3
    assert result == expected

