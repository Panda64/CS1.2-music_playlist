class Song:

  def __init__(self, title):
      self.__title = title
      self.__next_song = None


  def get_title(self):
    """Getter method for the song title"""

    return self.__title
  
  
  def set_title(self, title):
    """Setter method for the song title"""

    self.__title = str(title).title()


  def get_next_song(self):
    """Getter method for the next song object (node)"""
    
    return self.__next_song


  def set_next_song(self, next_title):
    """Setter method for the next song object (node)"""

    self.__next_song = next_title


  def __str__(self):
    """Returns a human-friendly message of the current song title"""

    return f"Song Title: {self.get_title()}"


  def __repr__(self):
    """Returns a human-friendly message of the titles of the current song and the song next up"""

    return f"{self.get_title()} -> {self.get_next_song()}"
