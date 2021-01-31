class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # Collision!

    number_collisions = 1

    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1

    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
      return None

    if possible_return_value[0] == key:
      return possible_return_value[1]

    retrieval_collisions = 1

    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      retrieval_collisions += 1

    return


hash_map=HashMap(15)
hash_map.assign("gabbro", "igneous")
hash_map.assign("sandstone", "sedimentary")
hash_map.assign("gneiss", "metamorphic")
print(hash_map.retrieve("gabbro"),
hash_map.retrieve("sandstone"),
hash_map.retrieve("gneiss"))


ppp="paras"
pppp=ppp.encode()
pp=sum(pppp)
print(pp)




#from linked_list import Node,LinkedList
#from blossom_lib import flower_definitions

#class HashMap:
##  def __init__(self, size):
 #   self.size=size
 #   self.array=[LinkedList() for i in range(self.size)]
#
 # def hash(self, key):
#    key_bytes=key.encode()
 #   hash_code=sum(key_bytes)
#    return hash_code
#
#  def compress(self,hash_code):
#    return hash_code % self.size
#  
#  def assign(self, key, value):
 #   array_index=self.compress(self.hash(key))
 #   payload=Node([key,value])
 #   list_at_array=self.array[array_index]
 #   for item in list_at_array:
 #     if key==item[0]:
  #      item[1]=value
  #      return
  #  list_at_array.insert(payload)
      



 # def retrieve(self, key):
 #   array_index=self.compress(self.hash(key))
#    c=0
 #   list_at_index=self.array[array_index]
 #   for i in list_at_index:
 #     if key==i[0]:
 #       c+=1
 #       return i[1]
 #   return None

      



#blossom=HashMap(len(flower_definitions))
#for i in flower_definitions:
 # blossom.assign(i[0], i[1])


#print(blossom.retrieve("daisy"))

      






