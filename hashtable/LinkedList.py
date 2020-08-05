class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __get_node_by_key(self, key):
        current = self.head
        while current:
            if current.key == key:
                break
            current = current.next
        
        return current

    def get(self, key):
        node = self.__get_node_by_key(key)

        return None if not node else node.value

    def put(self, key, value):
        # look for node with same key
        node = self.__get_node_by_key(key)
        # check if node with same key already exists
        if node:
            node.value = value
            return
            
        # create new node with key and value passed as parameters and add make it the list head
        node = HashTableEntry(key, value)
        node.next = self.head
        self.head = node

    def delete(self, key):
        if not self.head:
            return
        
        current = self.head
        previous = None

        return_value = None

        while current:
            if current.key == key:
                return_value = current.value
                if previous:
                    # link prev next to current next
                    previous.next = current.next
                else:
                    self.head = None
                
                break

            previous = current
            current = current.next

        return return_value