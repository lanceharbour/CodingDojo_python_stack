hero = {'name': 'Superman', 'powers':['flight', 'superhuman strength', 'x-ray vision']}
print(f"{hero['name']} has {hero['powers'][2]}")

boy_wizard = {'name': 'Harry Potter', 'student_info':{'house':'Gryffindor', 'year': 1}}
print(f"{boy_wizard['name']} is a {boy_wizard['student_info']['year']}st year in {boy_wizard['student_info']['house']}")

books = [{'title': 'Pride and Prejudice', 'authors':[{'name':'Jane Austen','birth_year': 1775}],'pub_year':1813},{'title':'Pride and Prejudice and Zombies','authors':[{'name':'Jane Austen','birth_year': 1775},{'name':'Seth Grahame-Smith','birth_year':1976}], 'pub_year':2009}]
print(f"{books[0]['title']} was written by {books[0]['authors'][0]['name']} in {books[0]['pub_year']}")
print(f"{books[1]['title']} was written by {books[1]['authors'][1]['name']} in {books[1]['pub_year']}")