class Player:

  def __init__(self, name, team):
    self.name = name
    self.xp = 1500
    self.team = team
  
  def introduce(self):
    print(f"Hello! I'm {self.name} and play at {self.team}")


class Team:
  def __init__(self, team_name):
    self.team_name = team_name
    self.players = []
  
  def add_player(self, name):
    self.players.append(Player(name, self.team_name))

  def show_player(self):
    for player in self.players:
      player.introduce()


team_x = Team("Team X")
team_x.add_player("nico")

blue_team = Team("blue Team")
blue_team.add_player("Lynn")

# nico.introduce()
# lynn.introduce()
print()
team_x.show_player()
