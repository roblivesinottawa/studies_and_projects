class NHL:
    def __init__(self, origin):
        self.origin = origin

    def teams(self):
        return f"Hello, we are from {self.origin}"

    def montreal(self):
        return "Canadiens is the team from Quebec"

    def toronto(self):
        return "Leafs is the team from Toronto"

    def ottawa(self):
        return "Senators is the team from Ottawa"

team = NHL("Canada")
print(team.teams())
print(team.montreal())
print(team.toronto())
print(team.ottawa())