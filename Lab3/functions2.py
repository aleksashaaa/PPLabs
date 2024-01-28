movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def single_imdb(film):
    for i in movies:
        if i["name"] == film:
            return i["imdb"] > 5.5
    return False

film = input("Write the name of a movie: ")
print(single_imdb(film))

#2
def all_imdb():
    res = []
    for i in movies:
        if i["imdb"] > 5.5:
            res.append(i)
    return res

print("All films with 5.5 and higher:\n", all_imdb())

#3
def category(catg):
    for i in movies:
        if i["category"] == catg:
            print(i["name"])

catg = input("Write the category: ")
category(catg)

#4
def average_score():
    res = 0
    for i in movies:
        res += i["imdb"]
    return res/len(movies)

print("Average IMDB score:\n", average_score())

#5
def average_by_cat(catg):
    res = 0
    n = 0
    for i in movies:
        if i["category"] == catg:
            res += i["imdb"]
            n += 1
    return res/n

catg = input("Write the category: ")
print("Average IMDB score in", catg, ":", average_by_cat(catg))