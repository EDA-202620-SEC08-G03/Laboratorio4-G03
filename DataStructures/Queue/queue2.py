def peek (my_queue):
    
    if my_queue["size"] == 0:
        raise Exception('EmptyStructureError: queue is empty')
    
    primer = my_queue["elements"][0]
    return primer

def size (my_queue):
    
    return my_queue["size"]