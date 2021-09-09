import statistics

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachussets Institute of Techology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500],
]


def enrollment_stats(my_list_of_lists):
    enrollments = [university[1] for university in my_list_of_lists]
    tuition_fees = [university[2] for university in my_list_of_lists]
    return enrollments, tuition_fees

def mean(my_list):
    return sum(my_list) / len(my_list)

def median(my_list):
    return statistics.median_grouped(my_list)

def main():
    students_list = enrollment_stats(universities)[0]
    tuition_list = enrollment_stats(universities)[1]
    print('*' * 20)
    print(f'Total students: {sum(students_list):,.0f}')
    print(f'Total tuition: $ {sum(tuition_list):,.0f}')
    print('\n')
    print(f'Student mean: {mean(students_list):,.2f}')
    print(f'Student median: {median(students_list):,.0f}')
    print('\n')
    print(f'Tuition mean: $ {mean(tuition_list):,.2f}')
    print(f'Tuition median: $ {median(tuition_list):,.0f}')
    print('*' * 20)


if __name__ == '__main__':
    main()
