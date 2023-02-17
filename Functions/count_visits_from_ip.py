'''
The first get_count_visits_from_ip using Counter returns a dictionary, where the key is IP, 
and the value is the number of occurrences in the specified list.

Example:

{
     '85.157.172.253': 2,
     ...
}
The second function get_frequent_visit_from_ip returns a tuple with the most frequently used 
IP in the list and the number of its occurrences in the list.
'''

from collections import Counter


def get_count_visits_from_ip(ips):
    dict_count_visits = dict(Counter(ips))
    return dict_count_visits


def get_frequent_visit_from_ip(ips):
    dict_count_visits = Counter(ips)
    frequent_visit = dict_count_visits.most_common(1)
    return tuple(*frequent_visit)


if __name__ == "__main__":
    ips = ['85.157.172.253', '143.231.49.229', '173.37.214.238', '27.137.126.114', '76.98.129.245', '66.50.38.43', '248.95.93.236',
           '173.37.214.238', '76.98.129.245', '76.98.129.245', '85.157.172.253', '66.50.38.43', '66.50.38.43', '66.50.38.43']
    print(get_count_visits_from_ip(ips))
    print(get_frequent_visit_from_ip(ips))
