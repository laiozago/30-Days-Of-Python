"""Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
output
['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']"""

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

string_names = [f"{nome} {sobrenome}" for list in names for nome,sobrenome in list]

print(string_names)