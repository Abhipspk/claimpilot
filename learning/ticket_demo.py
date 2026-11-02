class MetroTicket:
    def __init__(self, ticket_id, from_station, to_station, fare):
        self.ticket_id = ticket_id
        self.from_station = from_station
        self.to_station = to_station
        self.fare = fare

    def route_text(self):
        return f"{self.from_station} -> {self.to_station} (Rs {self.fare})"

if __name__ == "__main__":
    t1=MetroTicket("T-1", "Miyapur", "Ameerpet", 40)
    t2 = MetroTicket("T-2", "Ameerpet", "LB Nagar", 55)
    print(t1.ticket_id)
    print(t1.route_text())
    print(t2.route_text())
    t1.fare = 45
    print(t1.fare)
    print(t1)
    print(t1 == MetroTicket("T-1", "Miyapur", "Ameerpet", 45))
        