
class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        # Your code here
        self.capacity = capacity
        self.storage = [None] * capacity
        self.size = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.storage)

    # Day 2, Task: Implement load factor measurements and automatic hashtable size doubling.
    # Step 1: Compute and maintain load factor.
    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        count = 0
        for item in self.storage:
            if item:
                curr_item = item
                count += 1
                while curr_item.next:
                    count += 1
                    curr_item = curr_item.next

        return count / len(self.storage)

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash_1 = 5381
        for x in key:
            hash_1 = ((hash_1 << 5) + hash_1) + ord(x)

        return hash_1 & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.djb2(key) % self.capacity

    # Day 2, Task: Implement linked-list chaining for collision resolution.
    # Step 1: Modified `put()` method to handle collisions.
    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        current = self.storage[hash_index]

        new_node = HashTableEntry(key, value)

        if current:
            head = None

            while current:
                if current.key == key:
                    current.value = value
                    return None
                head = current
                current = current.next

            head.next = new_node
            self.size += 1
        else:
            self.storage[hash_index] = new_node
            self.size += 1

        # Day 2, Task: Implement load factor measurements and automatic hashtable size doubling.
        # Step 2: When load factor increases above `0.7`, automatically rehash the table to double its previous size.
        if self.get_load_factor() >= 0.7:
            self.resize(self.capacity * 2)

    # Day 2, Task: Implement linked-list chaining for collision resolution.
    # Step 1: Modified `delete()` method to handle collisions.
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        current = self.storage[hash_index]

        if current:
            if current.key == key:
                self.storage[hash_index] = current.next
                return None

            prev = None

            while current:
                # if a node's key matches the one we are searching for
                if current.key == key:
                    # set the prev_node.next to the curr.next
                    prev.next = current.next

                prev = current
                current = current.next

    # Day 2, Task: Implement linked-list chaining for collision resolution.
    # Step 1: Modified `get()` method to handle collisions.
    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        hash_index = self.hash_index(key)
        current = self.storage[hash_index]

        if current:
            while current:
                if current.key == key:
                    return current.value

                current = current.next

        return None

    # Day 2, Task: Implement load factor measurements and automatic hashtable size doubling.
    # Add the resize() method
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        arr = self.storage

        self.capacity = new_capacity
        self.storage = [None] * self.capacity

        for item in range(len(arr)):
            if arr[item]:
                current = arr[item]

                while current.next:
                    self.put(current.key, current.value)
                    current = current.next

                self.put(current.key, current.value)

        return self.storage


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")