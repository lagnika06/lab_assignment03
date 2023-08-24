class FlightTable:
    def __init__(self):
        self.matches = [
            {"Location": "Mumbai", "Team 01": "India", "Team 02": "Sri Lanka", "Timing": "DAY"},
            {"Location": "Delhi", "Team 01": "England", "Team 02": "Australia", "Timing": "DAY-NIGHT"},
            {"Location": "Chennai", "Team 01": "India", "Team 02": "South Africa", "Timing": "DAY"},
            {"Location": "Indore", "Team 01": "England", "Team 02": "Sri Lanka", "Timing": "DAY-NIGHT"},
            {"Location": "Mohali", "Team 01": "Australia", "Team 02": "South Africa", "Timing": "DAY-NIGHT"},
            {"Location": "Delhi", "Team 01": "India", "Team 02": "Australia", "Timing": "DAY"}
        ]

    def search_by_team(self, team_name):
        return [match for match in self.matches if team_name in [match["Team 01"], match["Team 02"]]]

    def search_by_location(self, location):
        return [match for match in self.matches if match["Location"] == location]

    def search_by_timing(self, timing):
        return [match for match in self.matches if match["Timing"] == timing]

    def display_matches(self, matches):
        for match in matches:
            print("Location:", match["Location"])
            print("Team 01:", match["Team 01"])
            print("Team 02:", match["Team 02"])
            print("Timing:", match["Timing"])
            print()

def main():
    flight_table = FlightTable()

    while True:
        print("Search options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            team_name = input("Enter team name: ")
            matches = flight_table.search_by_team(team_name)
            flight_table.display_matches(matches)
        elif choice == "2":
            location = input("Enter location: ")
            matches = flight_table.search_by_location(location)
            flight_table.display_matches(matches)
        elif choice == "3":
            timing = input("Enter timing: ")
            matches = flight_table.search_by_timing(timing)
            flight_table.display_matches(matches)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()