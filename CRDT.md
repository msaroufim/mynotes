# CRDTs - conflict free replicated data types
* https://ckeditor.com/blog/ (very high level)Lessons-learned-from-creating-a-rich-text-editor-with-real-time-collaboration/ 
* http://archagon.net/blog/2018/03/24/data-laced-with-history/ ((swift implementation, complicated article but lots and lots of excellent 
references)#conflict-free-replicated-data-types 
* http://jtfmumm.com/blog/2015/11/17/crdt-primer-1-defanging-order-theory/)
* https://hal.inria.fr/inria-00555588/document

Main value of CRDTs or operational transform is to manage a central state that's being changed by multiple actors concurrently while respecting eventual consistency.

Operational tranforms sync changes by broadcasting the diff of actions to all clients so that they can all simulate thew new state. I think Dota uses this for example. This is sometimes also called an event log. Can take O(n^2) to sync though. Operational transform also needs a central server which costs a lot of money if you have lots of users

Advantages
* Users shouldn't be picking the correct revision
* Offline work should also be possible (if someone DC's for a long time)
* Sync should happen in the background off the main application

Timestamps have their own issues since they depend on server vs client time for e.g

Google docs uses strong eventual consistency not strong consistency. Docs uses operational transform which has complicated guarantees.

A document is essentially a sort of database

Can do apps with cloud storage using CloudKit - apple gives 1PB of storage for devs (which sounds kinda nuts)

Typical approahces involve a Lamport timestamp (every new operation has a timestamp) and concurrency issues are resolved with some heuristics e.g: deleting the word "dog" means someone had to insert the word "dog" before.

CRDT merge is associative, commutative and idempotent

CRDTs grow in memory when theres lot of deletes since each delete is replaced with a tombstone. Fundamentally CRDTs operate over strings so need to turn whatever datastructure you have into a string.

> One last thing to note is that there are actually two kinds of CRDTs: CmRDTs and CvRDTs
* CmRDTs, or operation-based CRDTs, only require peers to exchange mutation events, but place some constraints on the transport layer. (For instance, exactly-once and/or causal delivery, depending on the CmRDT in question.)
*  With CvRDTs, or state-based CRDTs, peers must exchange their full data structures and then merge them locally, placing no constraints on the transport layer but taking up far more bandwidth and possibly CPU time. Both types of CRDT are equivalent and can be converted to either form.

## Order theory
3 core concepts
1. Can compare stuff with less than, equal etc..
2. Some elements are incomparable
3. Can join some elements

All integers can be compared to each other so this is called a total order

Order consists of a set of elements and a relation.
* In the case of integers it's the integers and the relation could be <= or >= (total order)
* In the case of people and relation of ancestor then not all people are ancestors of each other (partial order)

Vector clock has n timestamps corresponding to an event. They can't have a total order, same for any vector really

A join between a V b is a least upper bound, what is the smallest set that contains both a and b?

Joins obey 3 laws
1. Commutative a V b = b V a -> it doensn't matter which way you apply the join
2. Associative: (a V b) V c = a V (b V c) -> to join 3 elements, join 2 first
3. Idempotence: a V a = a -> can take join of self as many times as you like

Join semi lattice is an order <S, <= > for which there exists a join x V y for any x,y \in S

Any total order is a join semi lattice since a join (least upper bound always exists)

Why do I care about order theory for CRDTs? In short, just as joins tend to move “upwards,” so do merges of state-based CRDTs tend to converge on the One True Value, and for the very same reasons.

## Convergence of CRDTs
Specially covers CvRDT below

CRDT have 2 components
1. State, all possible states are treated as elements from a set
2. Merge function which is actually a join per the above definition

Idempotency is useful because we repeat particular merges without affecting the output.

Order not mattering means given 3 different nodes or more. You can do merges pairwise and are guaranteed to end up with the correct state in the end


```python
#crdt implementation of a counter
class GCounter:
  def __init__(self, nodeId, state_list):
    self.nodeId = nodeId
    self.state_list = state_list 

  def value(self):
    return sum(self.state_list)

  def increment(self):
    self.state_list[self.nodeId] += 1

  def merge(self, incoming):
    for idx in range(0, len(self.state_list)):
      self.state_list[idx] = max(self.state_list[idx], 
        incoming.state_list[idx])
```