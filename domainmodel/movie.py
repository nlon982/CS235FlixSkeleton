from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:
    def __init__(self, title, release_year):
        if title == "" or type(title) != str:
            self.__title = None
        else:
            self.__title = title.strip()  # would be less repeated codes to user setter method?

        if type(release_year) == int and release_year >= 1900: # using short circuiting to avoid an error being thrown if incorrect type
            self.__release_year = release_year
        else:
            self.__release_year = None

        self.__description = None
        self.__director = None
        self.__actors = list()
        self.__genres = list()
        self.__runtime_minutes = None

    # getter and setter methods (for all attributes except year)
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, a_title):
        if a_title != "" and type(a_title) == str: # this wasn't asked for
            self.__title = a_title.strip()
        else:
            self.__title = None # HIDDEN TEST CASE
        # assuming they don't want it set if it's an invalid name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, a_description):
        if type(a_description) == str:
            self.__description = a_description.strip()
        else:
            self.__description == None # HIDDEN TEST CASE

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, a_director):
        if type(a_director) == Director:
            self.__director = a_director

    @property
    def actors(self):
        return self.__actors

    @actors.setter
    def actors(self, actor_list):
        # ambigious on whether this should be added, and how it should work (considering add_actor exists)
        # so this will be used when you go a_movie_object.actors = [actor_object1, actor_object2, actor_object3]
        self.__actor_list = list() # empty list
        for a_actor in actor_list:
            if type(a_actor) == Actor:
                self.__actors.append(a_actor)

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, genre_list): # ambigious (ditto to above)
        self.__genre_list = list() # empty list
        for a_genre in genre_list:
            if type(a_genre) == Genre:
                self.__genres.append(a_genre)

    @property
    def runtime_minutes(self):
        return self.__runtime_minutes

    @runtime_minutes.setter
    def runtime_minutes(self, runtime_minutes):
        # i'll assume a number is passed, and round if a float is given
        if runtime_minutes > 0: # positive number
            self.__runtime_minutes = round(runtime_minutes)
        else:
            raise ValueError # as requested

    # they missed out having a getter and setter for year, putting it in for the sake of cleanliness
    @property
    def release_year(self):
        return self.__release_year

    @release_year.setter
    def release_year(self, a_release_year):
        # assumming year is a number
        if type(a_release_year) == int and a_release_year >= 1900:
            self.__release_year = a_release_year

    # other methods

    def add_actor(self, a_actor):
        if type(a_actor) == Actor: # assuming they want this
            if a_actor not in self.__actors:
                self.__actors.append(a_actor)
        # unsure if they want to throw an error

    def remove_actor(self, a_actor):
        if type(a_actor) == Actor:  # so it doesn't throw an error when using 'in' below
            if a_actor in self.__actors: # necessary because remove raises a ValueError if not found
                self.__actors.remove(a_actor)
        # they asked to NOT throw an error (hence above)

    def add_genre(self, a_genre):
        if type(a_genre) == Genre: # assuming they want this
            if a_genre not in self.__genres:
                self.__genres.append(a_genre)
        # unsure if they want to throw an error

    def remove_genre(self, a_genre):
        # ditto to remove_actor
        if type(a_genre) == Genre:
            if a_genre in self.__genres:
                self.__genres.remove(a_genre)

    # special methods, aka magic methods

    def __repr__(self):
        return "<Movie {}, {}>".format(self.__title, self.__release_year)

    def __eq__(self, other):
        # note, is it considered good practice to not use getter/setter methods (and rather directly talk to the attributes) in the class's methods, or nah?
        return (self.__title.lower() == other.title.lower()) and (self.__release_year == other.release_year)

    def __lt__(self, other):
        # presuming what they mean is that want me to sort by title THEN by release year (that intuively makes sense)

        if self.__title.lower() == other.title.lower():
            return self.__release_year < other.release_year
        else:
            return self.__title.lower() < other.title.lower()

    def __hash__(self):
        return hash(self.__title.lower() + str(self.__release_year)) # this would be one way to have a hash based on title and release year