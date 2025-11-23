class Playlist:
    def __init__(self, data, prompt):
        self.__data = data
        self.__prompt = prompt
        
    def __song_genres(self):
        self.genre_dict = {
            'Rap': [],
            'Pop': [],
            'Country': [],
            'Classic': [],
            'Latin': [],
            'Alternative': []
        }

        for song in data:
            genre = song[2]
            if genre in self.genre_dict:
                self.genre_dict[genre].append(song)
        
    def playlist(self):
        self.__song_genres()
        user_playlist = []
        included_songs = set()
        song_counts = [5,3,2]
        
        try: 
            self.genre_dict[prompt[0]]
        except KeyError:
            return "Item 1 not in dictionary"
        try: 
            self.genre_dict[prompt[1]]
        except KeyError:
            return "Item 2 not in dictionary"
        try: 
            self.genre_dict[prompt[2]]
        except KeyError:
            return "Item 3 not in dictionary"   
        
        for i, genre in enumerate(prompt): #Provide a count for genre
            if genre in self.genre_dict:
                songs = random.sample(self.genre_dict[genre], k=song_counts[i])
                for song in songs:
                    song_tuple = tuple(song) #Make song immutable 
                    if song_tuple not in included_songs:
                        user_playlist.append(song)
                        included_songs.add(song_tuple)              
        return user_playlist
                
    def __repr__(self):
       return f'Playlist({data}, {prompt})'

if __name__ == '__main__':
    import csv
    import random
    
    with open('BillboardTop100.csv', newline='') as f:
        """import csv as nested list with each row being an entity"""
        reader = csv.reader(f)
        data = list(reader)
        
        user_prompt = input("Please enter 3 favorite genres: ").split(' ')
        prompt = [genre.capitalize() for genre in user_prompt] 

    while True:
        valid_genres = ['Rap', 'Pop', 'Country', 'Classic', 'Latin', 'Alternative']

        if not all(genre.capitalize() in \
            ['Rap', 'Pop', 'Country', 'Classic', 'Latin', 'Alternative'] for genre in prompt):
            user_prompt = input("Please select 3 genres from 'Rap', 'Pop',"
            "'Country', 'Classic', 'Latin', 'Alternative': ").split(' ')
            prompt = [genre.capitalize() for genre in user_prompt] 
        else:
            break

    """Print Playlist"""    
    song_data = Playlist(data, prompt)
    user_playlist = song_data.playlist()
    print("Enjoy your playlist!")
    for song in user_playlist:
        print(f"{song[0]} - {song[1]}") 
   
    #Check if the playlist contains the correct number of songs
    expected_total_songs = 5 + 3 + 2  #Total songs for each genre
    assert len(user_playlist) == expected_total_songs
    
    #Check for unique songs in the playlist
    unique_songs = set()
    for song in user_playlist:
        assert tuple(song) not in unique_songs
        unique_songs.add(tuple(song))

