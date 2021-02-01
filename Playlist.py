from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None # <-- Head Pointer in disguise 


  def add_song(self, title):
    """Adds a song to the playlist"""
    new_song = Song(title)
    new_song.set_title(title)
    new_song.set_next_song(self.__first_song)
    self.__first_song = new_song
    

  def find_song(self, title):
    """Finds a song within a playlist"""
    counter = 0
    current_song = self.__first_song

    while current_song.get_title() != str(title).title():
      if current_song.get_next_song() == None:
        return -1
      
      current_song = current_song.get_next_song()
      counter += 1

    return counter


  def remove_song(self, title):
    """Removes a song from a playlist"""
    
    current_song = self.__first_song

    if current_song.get_title() == str(title).title():
      self.__first_song = current_song.get_next_song()
      print("Song has been removed!")
      return

    while current_song.get_next_song().get_title() != str(title).title():
      if current_song.get_next_song() == None:
        print("Song does not exist!")
        return

      current_song = current_song.get_next_song()
    
    target_song = current_song.get_next_song()
    current_song.set_next_song(target_song.get_next_song())

    print("Song has been removed!")
    

  def length(self):
    """Returns the length of the playlist"""

    counter = 0
    current_song = self.__first_song

    while current_song != None:
      current_song = current_song.get_next_song()
      counter += 1

    return counter


  def print_songs(self):
    """Prints the songs that are currently in the playlist"""

    counter = 0
    current_song = self.__first_song

    while current_song != None:
      counter += 1
      print(f"{counter}. {current_song.get_title()}")
      current_song = current_song.get_next_song()

    if counter == 0:
      print("There are no songs to display!")
      
      

    

  