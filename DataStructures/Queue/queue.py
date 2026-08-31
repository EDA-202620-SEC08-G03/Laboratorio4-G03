from DataStructures.List import single_linked_list as sll
def new_queue():
    queue = sll.new_list()
    return queue

def enqueue(queue,element):
    sll.add_last(queue,element)
    return queue

def peek (my_queue):
    
    if my_queue["size"] == 0:
        raise Exception('EmptyStructureError: queue is empty')
    
    primer = my_queue["first"]["info"]
    return primer


def size (my_queue):
    
    return my_queue["size"]

def dequeue(my_queue):
    if is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty')
    x = sll.get_element(my_queue,0)
    sll.delete_element(my_queue,0)
    return x

def is_empty(my_queue):
    y = sll.is_empty(my_queue)
    return y
