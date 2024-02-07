# Write a function that takes a category name and returns just those movies under that category.

movies  = {
    "movie_1" : {
        "name" : "Usual Suspects",
        "imdb" : 7.0,
        "category" : "Thriller" 
    },
    "movie_2" : {
        "name" : "Hitman",
        "imdb" : 6.3,
        "category" : "Action" 
    },
    "movie_3" : {
        "name" : "Dark Knight",
        "imdb" : 9.0,
        "category" : "Adventure" 
    }, 
    "movie_4" : {
        "name" : "The Help",
        "imdb" : 8.0,
        "category" : "Drama" 
    },
    "movie_5" : {
        "name" : "The Choice",
        "imdb" : 6.2,
        "category" : "Romance" 
    },
    "movie_6" : {
        "name" : "Colonia",
        "imdb" : 7.4,
        "category" : "Romance" 
    },
    "movie_7" : {
        "name" : "Love",
        "imdb" : 6.0,
        "category" : "Romance" 
    },
    "movie_8" : {
        "name" : "Bride Wars",
        "imdb" : 5.4,
        "category" : "Romance" 
    },
    "movie_9" : {
        "name" : "AlphaJet",
        "imdb" : 3.2,
        "category" : "War" 
    },
    "movie_10" : {
        "name" : "Ringing Crime",
        "imdb" : 4.0,
        "category" : "Crime" 
    },
    "movie_11" : {
        "name" : "Jocking Muck",
        "imdb" : 7.2,
        "category" : "Comedy" 
    },
    "movie_12" : {
        "name" : "What is the name",
        "imdb" : 9.2,
        "category" : "Suspense" 
    },
    "movie_13" : {
        "name" : "Detective",
        "imdb" : 7.0,
        "category" : "Suspense" 
    },
    "movie_14" : {
        "name" : "Exam",
        "imdb" : 4.2,
        "category" : "Thriller" 
    },
    "movie_15" : {
        "name" : "We Two",
        "imdb" : 7.2,
        "category" : "Romance" 
    }
}

def my_func(category) :
    lst = []
    for i in movies.values() :
        if i["category"] == category :
            lst.append(i["name"])
    return lst
    
category = input("Enter category of movie: ")
print(my_func(category))














