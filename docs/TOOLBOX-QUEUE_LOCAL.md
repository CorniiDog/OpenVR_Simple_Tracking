[Back to DOCS.md](DOCS.md)

Import Statement: `from toolbox import queue_local`

Alternative Import Statement: `from toolbox.queue_local import *`

# >  class Queue #

### [class Queue:](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L2) 

Note

```python
    A queue is a data structure that follows the First In First Out (FIFO) principle.
    This means that the first item added to the queue will be the first item removed from the queue.
    A queue can be implemented using a list or a linked list.
```

Param

```python
    queue_list: list
        The list to initialize the queue with
    max_size: int
        The maximum size of the queue
```

Example

```python
    queue = Queue([1, 2, 3, 4, 5], 10)

    a = queue.dequeue()
    print(a)
```

Reference

```python
    https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
```


 <details>
<summary>

#### Functions and Classes

</summary>

# >  >  function Queue.init #

### [def __init__(self, queue_list: list = None, max_size: int = None):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L30) 

Note

```python
        If the queue_list is not None, then the queue will be initialized with the list
        If the max_size is not None, then the queue will be initialized with the max_size
```

Param

```python
        queue_list: list
            The list to initialize the queue with
        max_size: int
            The maximum size of the queue
```

Return

```python
        None
```

Example

```python
        queue = Queue([1, 2, 3, 4, 5], 10)

        a = queue.dequeue()
        print(a)
```

# >  >  function Queue.enqueue #

### [def enqueue(self, item):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L61) 

Note

```python
        Adds the item to the end of the queue
```

Param

```python
        item: any
            The item to add to the queue
```

Return

```python
        None
```

Example

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        print(queue)
```

# >  >  function Queue.dequeue #

### [def dequeue(self):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L90) 

Note

```python
        Removes the first item from the queue
```

Param

```python
        None
```

Return

```python
        item: any
            The item that was removed from the queue
```

Example

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        a = queue.dequeue()
        print(a)
```

# >  >  function Queue.size #

### [def size(self) -> int:](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L118) 

Note

```python
        Returns the size of the queue
```

Param

```python
        None
```

Return

```python
        size: int
            The size of the queue
```

Example

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        print(queue.size())
```

# >  >  function Queue.is_empty #

### [def is_empty(self) -> bool:](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L146) 

Note

```python
        Returns True if the queue is empty, False otherwise
```

Param

```python
        None
```

Return

```python
        is_empty: bool
            True if the queue is empty, False otherwise
```

Example

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)

        print(queue.is_empty())
```

# >  >  function Queue.peek #

### [def peek(self):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L173) 

Note

```python
        Returns the first item in the queue without removing it
```

Param

```python
        None
```

Return

```python
        item: any
            The first item in the queue
```

Example

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        a = queue.peek()
        print(a)
```

# >  >  function Queue.get_list #

### [def get_list(self):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L201) 

Note

```python
        Returns the list of items in the queue
```

Param

```python
        None
```

Return

```python
        list: list
            The list of items in the queue
```

Example

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        a = queue.get_list()
        print(a)
```

# >  >  function Queue.len #

### [def __len__(self):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L230) 

Note

```python
        Returns the size of the queue
```

Param

```python
        None
```

Return

```python
        size: int
            The size of the queue
```

Example

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)

        print(len(queue))
```

# >  >  function Queue.copy #

### [def copy(self):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L256) 

Note

```python
        Returns a copy of the queue
```

Param

```python
        None
```

Return

```python
        new_queue: Queue
            A copy of the queue
```

Example

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        new_queue = queue.copy()
        print(new_queue)
```

# >  >  function Queue.copy #

### [def __copy__(self):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L288) 

Note

```python
        Returns a copy of the queue
```

Param

```python
        None
```

Return

```python
        new_queue: Queue
            A copy of the queue
```

Example

```python
        queue = Queue(max_size=10)

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        new_queue = queue.copy()
        print(new_queue)
```

# >  >  function Queue.eq #

### [def __eq__(self, other):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L317) 

Note

```python
        Returns True if the queues are equal, False otherwise
```

Param

```python
        other: Queue
            The other queue to compare to
```

Return

```python
        is_equal: bool
            True if the queues are equal, False otherwise
```

Example

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue == other)
```

# >  >  function Queue.ne #

### [def __ne__(self, other):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L348) 

Note

```python
        Returns True if the queues are not equal, False otherwise
```

Param

```python
        other: Queue
            The other queue to compare to
```

Return

```python
        is_not_equal: bool
            True if the queues are not equal, False otherwise
```

Example

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue != other)
```

# >  >  function Queue.getitem #

### [def __getitem__(self, index):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L373) 

Note

```python
        Returns the item at the given index
```

Param

```python
        index: int
            The index of the item to get
```

Return

```python
        item: any
            The item at the given index
```

Example

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue[2])
```

# >  >  function Queue.setitem #

### [def __setitem__(self, index, value):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L397) 

Note

```python
        Sets the item at the given index to the given value
```

Param

```python
        index: int
            The index of the item to set
        value: any
            The value to set the item to
```

Return

```python
        None
```

Example

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        queue[2] = 10
        print(queue)
```

# >  >  function Queue.delitem #

### [def __delitem__(self, index):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L423) 

Note

```python
        Deletes the item at the given index
```

Param

```python
        index: int
            The index of the item to delete
```

Return

```python
        None
```

Example

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        del queue[2]
        print(queue)
```

# >  >  function Queue.iter #

### [def __iter__(self):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L447) 

Note

```python
        Returns an iterator for the queue
```

Param

```python
        None
```

Return

```python
        iter: iter
            An iterator for the queue
```

Example

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        for item in queue:
            print(item)
```

# >  >  function Queue.reversed #

### [def __reversed__(self):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L471) 

Note

```python
        Returns an iterator for the queue in reverse order
```

Param

```python
        None
```

Return

```python
        reversed: iter
            An iterator for the queue in reverse order
```

Example

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        for item in reversed(queue):
            print(item)
```

# >  >  function Queue.contains #

### [def __contains__(self, item):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L495) 

Note

```python
        Returns True if the item is in the queue, False otherwise
```

Param

```python
        item: any
            The item to check for
```

Return

```python
        is_in: bool
            True if the item is in the queue, False otherwise
```

Example

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        print(1 in queue)
```

# >  >  function Queue.add #

### [def __add__(self, other):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L519) 

Note

```python
        Returns a new queue with the items from both queues
```

Param

```python
        other: Queue
            The other queue to add to this queue
```

Return

```python
        new_queue: Queue
            A new queue with the items from both queues
```

Example

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([6, 7, 8, 9, 10], max_size=10)

        new_queue = queue + other
        print(new_queue)
```

# >  >  function Queue.iadd #

### [def __iadd__(self, other):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L550) 

Note

```python
        Returns this queue with the items from both queues
```

Param

```python
        other: Queue
            The other queue to add to this queue
```

Return

```python
        self: Queue
            This queue with the items from both queues
```

Example

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)
        other = Queue([6, 7, 8, 9, 10], max_size=10)

        queue += other
        print(queue)
```

# >  >  function Queue.mul #

### [def __mul__(self, other):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L578) 

Note

```python
        Returns a new queue with the items from this queue repeated the given number of times
```

Param

```python
        other: int
            The number of times to repeat the queue
```

Return

```python
        new_queue: Queue
            A new queue with the items from this queue repeated the given number of times
```

Example

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        new_queue = queue * 3
        print(new_queue)
```

# >  >  function Queue.imul #

### [def __imul__(self, other):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L607) 

Note

```python
        Returns this queue with the items from this queue repeated the given number of times
```

Param

```python
        other: int
            The number of times to repeat the queue
```

Return

```python
        self: Queue
            This queue with the items from this queue repeated the given number of times
```

Example

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        queue *= 3
        print(queue)
```

# >  >  function Queue.str #

### [def __str__(self):](../../../Downloads/Template-master/Template-master/toolbox/queue_local.py#L636) 

Note

```python
        Returns a string representation of the queue
```

Param

```python
        None
```

Return

```python
        string: str
            A string representation of the queue
```

Example

```python
        queue = Queue([1, 2, 3, 4, 5], max_size=10)

        print(queue)
```

</details>

