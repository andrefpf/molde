from molde.colors import Color
from random import randint


def test_conversions():
    color = Color.from_hex("#b5e83c")
    assert color.to_hex().lower() == "#b5e83c"
    assert color.to_rgb() == (181, 232, 60)
    assert color.to_hsv() == (78, 74, 91)


def test_color_creation():
    a = Color.from_hex("#b5e83c")
    b = Color.from_rgb(181, 232, 60)
    c = Color.from_hsv(78, 74, 91)
    assert a == b == c


def test_in_out():
    rgba = [randint(0, 255) for _ in range(4)]
    reference = Color.from_rgba(*rgba)

    assert reference == Color.from_rgba(*reference.to_rgba())
    assert reference == Color.from_rgba_f(*reference.to_rgba_f())

    rgb = [randint(0, 255) for _ in range(3)]
    reference = Color.from_rgb(*rgb)

    assert reference == Color.from_rgb(*reference.to_rgb())
    assert reference == Color.from_rgb_f(*reference.to_rgb_f())
    assert reference == Color.from_hex(reference.to_hex())

    hsv_a = (randint(0, 360), randint(0, 100), randint(0, 100))
    hsv_b = Color.from_hsv(*hsv_a).to_hsv()
    for a, b in zip(hsv_a, hsv_b):
        # The conversion is not very lossless =(
        assert abs(a - b) <= 5


def test_color_modifications():
    color = Color.from_hex("#ff0000")
    assert color.with_brightness(50).to_rgb() == (128, 0, 0)

    color = Color.from_hex("#ffffff").with_brightness(10)
    assert color.to_rgb() == (26, 26, 26)

    color = Color.from_hex("#0000ff").with_saturation(50)
    assert color.to_rgb() == (128, 128, 255)

    color = Color.from_hex("#80ff80").with_saturation(80)
    assert color.to_rgb() == (51, 255, 51)

    color = Color.from_hex("#ff0000").with_rgba(g=255)
    assert color.to_rgb() == (255, 255, 0)

    color = Color.from_hex("#ff0000").with_rgba_f(b=1)
    assert color.to_rgb() == (255, 0, 255)

    color = Color.from_rgba(10, 20, 200, 128).apply_factor(2)
    assert color.to_rgba() == (20, 40, 255, 128)

