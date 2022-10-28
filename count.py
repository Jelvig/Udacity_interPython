"""This code takes in a txt file and give the top ten most used words"""
import collections


def count_unique_words(filename):
    with open(filename, 'r') as f:
        flat_list=[word for line in f for word in line.split()]
        count = collections.Counter(flat_list)
        top = count.most_common(10)
    return print(top)


if __name__ == '__main__':
    count_unique_words('hamlet.txt')
