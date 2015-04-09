This repo contains a linked list!

Here's how to use it!

```python
>>> from linked_list import LinkedList
>>> list = LinkedList()
>>> list.enqueue('Mighty')
>>> list.enqueue('Morphin')
>>> list.enqueue('Power')
>>> list.enqueue('Rangers')
>>> print list
[Mighty, Morphin, Power, Rangers]
>>> print list.dequeue()
Mighty
>>> print list.dequeue()
Morphin
>>> print list.dequeue()
Power
>>> print list.dequeue()
Rangers
```