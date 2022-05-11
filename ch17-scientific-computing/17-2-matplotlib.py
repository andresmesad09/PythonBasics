import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path


def main():
    # ----
    # 1) Recreate graphs
    # ----

    # Plot
    ys = np.arange(1, 13).reshape(3, 4)
    fig, ax = plt.subplots()
    ax.plot(ys, linestyle='--')
    fig.suptitle('Plot a 3 x 4 np.array)')
    plt.show()

    # Bar plot
    courses = {
        'Datacamp': 500,
        'Platzi': 250,
        'Real Python': 450,
    }
    fig, ax = plt.subplots()
    ax.bar(courses.keys(), courses.values())
    fig.suptitle('Courses by platform', fontsize=18)
    ax.set_xlabel('Platform')
    ax.set_ylabel('Count of courses')
    plt.show()

    # Histogram
    xs = np.random.randn(10000)
    fig, ax = plt.subplots()
    ax.hist(xs, bins=20)
    fig.suptitle('Distribution of values', fontsize=18)
    ax.set_ylabel('Count')
    plt.show()

    # ----
    # 2) Do pirates cause global warming?
    # ----
    path_csv = Path.cwd() / 'ch17-scientific-computing' / 'pirates.csv'
    path_png = Path.cwd() / 'ch17-scientific-computing' / 'pirates.png'
    df = pd.read_csv(str(path_csv))

    fig, ax = plt.subplots()
    ax.plot(df['Pirates'], df['Temperature'])
    ax.set_xlabel('Number or pirates')
    ax.set_ylabel('Temperature')
    fig.suptitle('Number of Pirates vs Temperature')
    fig.savefig(str(path_png))
    plt.show()


if __name__ == '__main__':
    main()
