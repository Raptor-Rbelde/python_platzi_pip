import matplotlib.pyplot as plt

def generate_chart():
    labels = ["A", "B", "C"]
    values = [1, 4, 2]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    plt.savefig("pie.png")
    plt.close()