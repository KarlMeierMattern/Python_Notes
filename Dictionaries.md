# Dictionaries  

## General  

- Keys are immutable objects  
- Select, update and remove using `[ ]`  
- Indexed by range of unique keys  
- Lookup table with unique keys  

---

### Example  

        world = {‘key1’:2, ‘key2’:4}  
        world[‘key1’]  

> outputs `2`  

        world[‘key3’] = 6  

> adds the `key3:6` pair to the end of the dictionary  

        world[‘key3’] = 8  

> edits the value of `key3` to `8`  

        del(world[‘key3’]  

> deletes the `key3:8` pair from the world dictionary  

        world = {‘key1’:value1, ‘key2’:value2}  
        
---

### Methods  

Calling the .items() method when iterating over a dictionary:
for key, value in world.items():
	print(key + “--” + str(value))

