def FitPolynomial(*coords):
    for idx, (x, y) in enumerate(coords):
        print(f"x{idx}: {x} \ny{idx}: {y}")


def main():
    FitPolynomial((3, 7), (5, 6), (4, 4))


if __name__ == "__main__":
    main()