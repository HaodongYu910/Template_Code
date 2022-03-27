from multiprocessing.sharedctypes import Value
import operator

a = {'flavia': {'info': 0, 'error': 4}, 'xlg': {'info': 0, 'error': 3}, 'rr.robinson': {'info': 1, 'error': 1}, 'ac': {'info': 2, 'error': 1}, 'enim.non': {'info': 2, 'error': 2}, 'breee': {'info': 1, 'error': 4}, 'bpacheco': {'info': 0, 'error': 1}, 'blossom': {'info': 1, 'error': 6}, 'ahmed.miller': {'info': 2, 'error': 3}, 'britanni': {'info': 0, 'error': 1}, 'mdouglas': {'info': 1, 'error': 3}, 'oren': {'info': 2, 'error': 6}, 'sri': {'info': 2, 'error': 1}, 'jackowens': {'info': 2, 'error': 3}, 'mcintosh': {'info': 4, 'error': 2}, 'mai.hendrix': {'info': 0, 'error': 2}, 'kirknixon': {'info': 1, 'error': 1}, 'nonummy': {'info': 2, 'error': 2}, 'montanap': {'info': 0, 'error': 3}, 'noel': {'info': 5, 'error': 3}}
b = sorted(a.items(), key=operator.itemgetter(0))
c = dict(b)
print(dict(sorted(a.items(), key=operator.itemgetter(0))))

d = {'Tried to add information to closed ticket': 12, "Ticket doesn't exist": 7, 'Timeout while retrieving information': 15, 'The ticket was modified while updating': 9, 'Permission denied while closing ticket': 10, 'Connection to DB failed': 13}
e = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
f = dict(e)
print(f)
