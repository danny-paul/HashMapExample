class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        # creates a list of a list
        # basically creates buckets to handle when hash collisions occur
        return [[] for _ in range(self.size)]

    # will set a value to the corresponding index position of the key in the hashmap
    def set_val(self, key, value):
        # gets the index of the hash_table since doing the modulo of the size will always result in a value smaller
        # than the size of our array
        hash_key = hash(key) % self.size

        # now with the index, we can grab the appropriate bucket (recall, we created a list of a list)
        bucket = self.hash_table[hash_key]

        # now we need to iterate through the bucket in case there were collisions with our hash_table (list of list)
        # but recall that a user may send us a key that may already
        found_key = False
        for index, record in enumerate(bucket):
            record_key, record_val = record

            # check if there is a match within the bucket (list)
            if record_key == key:
                found_key = True
                break

        if found_key:
            bucket[index] = (key, value)
        else:
            bucket.append((key, value))

