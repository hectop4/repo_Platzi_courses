import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):

    fig,ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

def generate_pie_chart(labels, values):
    fig,ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    ax.axis('equal')
    plt.show()

if __name__ == '__main__':
    labels = ['G1', 'G20', 'G3', 'G4', 'G5']
    values = [20, 34, 30, 30, 27]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)
