import heapq

class AirEvent:
    def __init__(self, timestamp, plane_id, is_takeoff):
        self.timestamp = timestamp
        self.plane_id = plane_id
        self.is_takeoff = is_takeoff

class AirTrafficController:
    def __init__(self):
        self.event_heap = []  # Min heap to store air events

    def schedule_event(self, air_event):
        heapq.heappush(self.event_heap, (air_event.timestamp, air_event))

    def get_next_event(self):
        if not self.event_heap:
            return None

        _, next_air_event = heapq.heappop(self.event_heap)
        return next_air_event

# Example usage:
atc = AirTrafficController()

event1 = AirEvent(10, "ABC123", True)  # Plane ABC123 taking off at timestamp 10
event2 = AirEvent(15, "XYZ789", False)  # Plane XYZ789 landing at timestamp 15
event3 = AirEvent(5, "DEF456", True)   # Plane DEF456 taking off at timestamp 5

atc.schedule_event(event1)
atc.schedule_event(event2)
atc.schedule_event(event3)

next_event = atc.get_next_event()
while next_event:
    action = "takeoff" if next_event.is_takeoff else "landing"
    print(f"At timestamp {next_event.timestamp}, plane {next_event.plane_id} is scheduled for {action}")
    next_event = atc.get_next_event()
