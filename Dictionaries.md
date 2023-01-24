# Dictionaries  

## General  

- Keys are immutable objects  
- Select, update and remove using `[ ]`  
- Indexed by range of unique keys  
- Lookup table with unique keys  

---

### Example  

        world = {‘key1’:value1, ‘key2’:value2}  
        world[‘key1’]
> outputs value1  
        world[‘key3’] = value3  
> adds this ‘key’:value pair to the end of the dictionary  
> `value3` in `world` returns the boolean True as the key `value3` is in the `world` dictionary  
        world[‘key3’] = value4  
> edits the value of `key3` to `value4`  
        del(world[‘key3’]  
> deletes the `key3:value4` pair from the world dictionary  
        world = {‘key1’:value1, ‘key2’:value2}  
---

### Methods  

Calling the .items() method when iterating over a dictionary:
for key, value in world.items():
	print(key + “--” + str(value))

