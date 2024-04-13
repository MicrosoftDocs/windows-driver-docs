---
title: Framework Object Collections
description: Framework Object Collections
keywords:
- framework objects WDK KMDF , collections
- collections WDK KMDF
- framework collection objects WDK KMDF
- object collections WDK KMDF
ms.date: 04/20/2017
---

# Framework Object Collections





Drivers can group framework objects into collections that are represented by *framework collection objects*.

For example, if a driver receives a framework request object that represents a large I/O request, the driver might have to break the large request into smaller requests that it can send to an [I/O target](./introduction-to-i-o-targets.md). To break a large request into smaller ones, the driver must create a set of request objects that represent the smaller requests. To keep track of these driver-created request objects, the driver might create a collection object and add them to the collection.

Typically, the objects in an object collection consist of a single type of framework object, but a driver can create a collection that consists of different types of objects.

Your driver can also create a collection of collections. That is, a collection can consist of a set of collection objects.

Framework-based drivers can perform the following operations on object collections:

-   Create a collection object.

    To create a new collection, drivers can call [**WdfCollectionCreate**](/windows-hardware/drivers/ddi/wdfcollection/nf-wdfcollection-wdfcollectioncreate).

-   Add an object to a collection.

    To add objects to a collection, drivers can call [**WdfCollectionAdd**](/windows-hardware/drivers/ddi/wdfcollection/nf-wdfcollection-wdfcollectionadd), one or more times. Each call to **WdfCollectionAdd** appends an object to the end of the collection and increments the appended object's reference count.

-   Remove an object from a collection.

    To remove an object from a collection and decrement its reference count, drivers can call [**WdfCollectionRemove**](/windows-hardware/drivers/ddi/wdfcollection/nf-wdfcollection-wdfcollectionremove) or [**WdfCollectionRemoveItem**](/windows-hardware/drivers/ddi/wdfcollection/nf-wdfcollection-wdfcollectionremoveitem). When an object is removed, all objects after the removed one will have their index automatically decremented.

-   Obtain the number of objects in a collection.

    To determine the number of objects that a collection contains, drivers can call [**WdfCollectionGetCount**](/windows-hardware/drivers/ddi/wdfcollection/nf-wdfcollection-wdfcollectiongetcount).

-   Obtain a handle to an object in the collection.

    If a driver calls [**WdfCollectionGetItem**](/windows-hardware/drivers/ddi/wdfcollection/nf-wdfcollection-wdfcollectiongetitem), supplying an index value as an input argument, the driver receives a handle to the object that is associated with the index value. (An index value of zero represents the first object in the collection, an index value of one represents the second object, and so on--like a linked list. When the driver removes item *i* from a collection, item *i*+1 becomes item *i*.)

    Drivers can also call [**WdfCollectionGetFirstItem**](/windows-hardware/drivers/ddi/wdfcollection/nf-wdfcollection-wdfcollectiongetfirstitem) or [**WdfCollectionGetLastItem**](/windows-hardware/drivers/ddi/wdfcollection/nf-wdfcollection-wdfcollectiongetlastitem) to obtain a handle to the first or last item that was added to the collection.

-   Lock a collection.

    A driver can call [**WdfWaitLockAcquire**](/previous-versions/ff551168(v=vs.85)) to synchronize access to a collection at IRQL = PASSIVE\_LEVEL, or it can call [**WdfSpinLockAcquire**](/previous-versions/windows/hardware/drivers/ff550040(v=vs.85)) synchronize access at IRQL = DISPATCH\_LEVEL. After a driver acquires a lock, the collection cannot be accessed by other code in the driver that also calls **WdfWaitLockAcquire** or **WdfSpinLockAcquire**. After completing an operation on the collection, the driver must call [**WdfWaitLockRelease**](/windows-hardware/drivers/ddi/wdfsync/nf-wdfsync-wdfwaitlockrelease).

    Calling [**WdfWaitLockAcquire**](/previous-versions/ff551168(v=vs.85)) or [**WdfSpinLockAcquire**](/previous-versions/windows/hardware/drivers/ff550040(v=vs.85)) does not prevent other code in the driver from simultaneously accessing the collection, if that other code does not also call **WdfWaitLockAcquire** or **WdfSpinLockAcquire**.

-   Delete a collection.

    To delete a collection object, drivers can call [**WdfObjectDelete**](/windows-hardware/drivers/ddi/wdfobject/nf-wdfobject-wdfobjectdelete). More typically, however, drivers specify a parent object when they create a collection, and the framework deletes the collection object when it deletes the parent object.

    For example, if a driver creates a set of request objects so that it can break a large I/O request into smaller requests, it can make the large I/O request's request object the parent object of the collection object. Eventually the driver's I/O target will call [**WdfRequestComplete**](/windows-hardware/drivers/ddi/wdfrequest/nf-wdfrequest-wdfrequestcomplete) to complete the smaller requests. At that point, the driver can call **WdfRequestComplete** for the large I/O request, causing the framework to delete the request object and its child object: the collection object.

    When the framework deletes a collection object that contains objects that have not been removed, the framework removes the objects from the collection and decrements their reference counts, but it deletes only the collection object.

Sometimes a driver must examine all of the objects within a collection. The following code example demonstrates this situation:

```cpp
WdfWaitLockAcquire(CollectionLockHandle, NULL);
ItemCount = WdfCollectionGetCount(CollectionHandle);
for (i=0; i<ItemCount; i++) {
    ObjectHandle = WdfCollectionGetItem(CollectionHandle, i);
    // 1. Call object-specific methods to obtain object properties.
    // 2. Perform object-specific operations.
    }
WdfWaitLockRelease(CollectionLockHandle);
```