import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['Python', 'C++', 'Ruby', 'Java']
    sizes = [215, 130, 245, 210]

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    fig, ax=plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.savefig('pie_chart.png')
    plt.close()
