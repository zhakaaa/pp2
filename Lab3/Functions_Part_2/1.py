# Write a function that takes a single movie and returns True if its IMDB score is above 5.5

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

def my_func(name) :
    for i in movies.values() :
        if i["name"] == name :
            if i["imdb"] > 5.5 :
                return True
            return False
    
name = input("Enter name of movie: ")
print(my_func(name))














