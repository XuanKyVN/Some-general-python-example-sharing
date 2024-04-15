from collections import defaultdict

'''
y = defaultdict(lambda: defaultdict(lambda: 0))
print y['k1']['k2']   # 0
print dict(y['k1'])   # {'k2': 0}
'''

x = defaultdict(lambda: 0)
x['a'] =0
x['b'] =100

y = defaultdict(lambda: defaultdict(lambda: 0))
y['a']['k1']=10
y['b']['k2']=100

print(y)


SAMPLE= {'Age':28, 'Salary':2000}
SAMPLE = defaultdict(lambda:0,SAMPLE)
print(SAMPLE)

SAMPLE1 = defaultdict(lambda:[])
SAMPLE1['id']=[123,322,768]
print(SAMPLE1)

k = defaultdict(lambda: 0)
k["u"]=12
k['l']=1234
l = defaultdict(lambda: defaultdict(lambda: 0))
print(k)
l['x']['y']=147
l['x']['z']=1445
l['x']

print(l)
track_history = defaultdict(lambda: [])
track_history['a'] =[212,12,34]
track_history['b'] =[212,1312,344]

print(track_history)
'''
Python - Default Dict

Python defaultdict() with examples including lambda
defaultdict(callable, **kwargs)is a sub-class of Python dict built in.

Python creators added several "versions" of standard dict implementation to answer some of the most common user problems.

If you call a non existent key in a standard, normal dict in Python you will get a KeyError. You can avoid this with get() method but if you would like to provide a default value for any key that you will call in your dict, then defaultdict is a way to go.

defaultdict needs to be imported from collections

callable is used to calculate default value. It cannot accept any arguments and needs to return wanted value. It's called default_factory. It doesn't need to return the same value each time.

Take a look at examples below:

from collections import defaultdict

my_dict = defaultdict(lambda: 'curiosity')

print(my_dict)  # defaultdict(<function <lambda> at 0x1032ceca0>, {})

print(my_dict['dev'])  # curiosity

print(my_dict)  # defaultdict(<function <lambda> at 0x1032ceca0>, {'dev': 'curiosity'})
Output:

defaultdict(<function <lambda> at 0x1022f8ca0>, {})
curiosity
defaultdict(<function <lambda> at 0x1022f8ca0>, {'dev': 'curiosity'})
At first, our dict was empty. Then we called 'dev' key, that didn't exist before and our dict returned 'curiosity'. And it was of course added to our dict.

from collections import defaultdict

other_dict = {'starting': 'value'}

my_dict = defaultdict(lambda: 'curiosity', other_dict)

print(my_dict)  # defaultdict(<function <lambda> at 0x10e97d820>, {'starting': 'value'})

print(my_dict['dev'])  # curiosity

print(my_dict)  # defaultdict(<function <lambda> at 0x10e97d820>, {'starting': 'value', 'dev': 'curiosity'})
Output:

defaultdict(<function <lambda> at 0x1023c8940>, {'starting': 'value'})
curiosity
defaultdict(<function <lambda> at 0x1023c8940>, {'starting': 'value', 'dev': 'curiosity'})
We can provide additional data (here other_dict) to "prefill" my_dict.

from collections import defaultdict

my_dict = defaultdict(lambda: 0)
my_second_dict = defaultdict(int)

print(my_dict['dev'], my_second_dict['curiosity'])  # 0 0

print(my_dict)  # defaultdict(<function <lambda> at 0x10308aca0>, {'dev': 0})
print(my_second_dict)  # defaultdict(<class 'int'>, {'curiosity': 0})
Output:

0 0
defaultdict(<function <lambda> at 0x10368aca0>, {'dev': 0})
defaultdict(<class 'int'>, {'curiosity': 0})
Here both lambda: 0 and int are giving the same result.

from collections import defaultdict

my_dict = defaultdict()
my_other_dict = {}

print(my_dict == my_other_dict)  # True

my_dict = defaultdict(lambda: 'curiosity')
my_other_dict = {'dev': 'curiosity'}

print(my_dict == my_other_dict)  # False
print(my_dict['dev'])  # curiosity
print(my_dict == my_other_dict)  # True
Output:

True
False
curiosity
True
Comparison of defaultdict with the same keys as a "standard" dict, will result in True.

'''


