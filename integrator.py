import argparse
import numpy as np
import matplotlib.pyplot as plt


def left_choicer(a, b):
    return a


def right_choicer(a, b):
    return b


def mid_choicer(a, b):
    return (a + b) / 2


def random_choicer(a, b):
    return np.random.uniform(a, b)


def integrate(f, x_left, x_right, n_points, choicer):
    borders = np.linspace(x_left, x_right, n_points + 1)
    segments = np.hstack([
        borders[:-1].reshape(-1, 1),
        borders[1:].reshape(-1, 1)
    ])
    dots = np.apply_along_axis(lambda row: choicer(row[0], row[1]), 1, segments)
    ys = f(dots)

    integral_sum = np.sum(ys * (segments[:, 1] - segments[:, 0]))
    
    fig, ax = plt.subplots(1, figsize=(15, 8))
    ax.bar(segments.mean(axis=1), ys, width=10/n_points)
    ax.set_title(f"Integral sum: {integral_sum}")

    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Integrator by evjeny. Integrates f(x)=sin(x) on [0, 4Pi]")
    parser.add_argument("-n", type=int, default=100, help="Number of points to split the interval")
    parser.add_argument("-e", type=str, default="mid", help="Type of equipment, must be one of: left, right, mid, random")
    args = parser.parse_args()

    if args.n <= 0:
        print("n must be greater than 0!")
        return
    
    if args.e not in ["left", "right", "mid", "random"]:
        print("e must be one of: left, right, mid, random !")
        return
    
    choicers = {
        "left": left_choicer,
        "right": right_choicer,
        "mid": mid_choicer,
        "random": random_choicer
    }

    integrate(np.sin, 0, 4 * np.pi, args.n, choicers.get(args.e))


if __name__ == "__main__":
    main()

