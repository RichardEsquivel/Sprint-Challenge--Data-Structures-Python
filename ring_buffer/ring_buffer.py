from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # check if length of list is smaller than capacity if so we will add to the tail of the ring buffer till full
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            # current value will be at head
            self.current = self.storage.head
        else:
            # when length of list hits capacity set current node to item passed in
            self.current.value = item
            # Move to next node if one exists and set that one as the current node
            if self.current.next:
                self.current = self.current.next
                # If there is no next node and you're at the tail the current node will be made into the head
            else:
                self.current = self.storage.head
            #

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        # Start from the head
        node = self.storage.head
        # continue until node value reads None
        while node:
            # Refresh with value passed in from node head
            list_buffer_contents.append(node.value)
            # continue till you reach node value of None which breaks the while loop
            node = node.next
        return list_buffer_contents

# ----------------Stretch Goal-------------------


# class ArrayRingBuffer:
#     def __init__(self, capacity):
#         pass

#     def append(self, item):
#         pass

#     def get(self):
#         pass
