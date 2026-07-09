class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_time = 0
        orders = len(customers)
        free_at = None
        
        for arrival, duration in customers:
            print(f"{arrival=} {duration=} {free_at=}")
            if (free_at is None) or (free_at is not None and free_at <= arrival):
                total_time += duration
                free_at = arrival + duration
            elif free_at is not None and free_at > arrival:
                #total_time += duration + free_at - (free_at - arrival)
                free_at = (free_at - arrival) + arrival + duration
                total_time += free_at - arrival
            
            #print(f"{total_time=} {free_at=}")
        return total_time / orders