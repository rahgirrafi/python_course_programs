import pandas as pd

dict = {
    "name": ["Tom", "Jerry", "Steve", "Alice"],
    "age": [20, 21, 22, 23],
    "gender": ['M', 'M', 'M', 'F'],
    "address": ['NY', 'DC', 'LA', 'SF']
}

dict.update({"phone": [1234567890, 1234567891, 1234567892, 1234567893]})

df = pd.DataFrame(dict)
print(df)


