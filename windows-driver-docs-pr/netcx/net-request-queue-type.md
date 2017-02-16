---
title: NET_REQUEST_QUEUE_TYPE enumeration
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_TYPE
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET_REQUEST_QUEUE_TYPE enumeration

[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

Specifies the type of queue.

Syntax
------

```ManagedCPlusPlus
typedef enum _NET_REQUEST_QUEUE_TYPE { 
  NetRequestQueueTypeInvalid        = ,
  NetRequestQueueDefaultSequential  = ,
  NetRequestQueueDefaultParallel    = 
} NET_REQUEST_QUEUE_TYPE;
```

Constants
---------

**NetRequestQueueTypeInvalid**  
Not supported.

**NetRequestQueueDefaultSequential**  
Specifies that the queue supports sequential delivery (regular OIDs).

**NetRequestQueueDefaultParallel**  
Specifies that the queue supports parallel dispatching (direct OIDs).


Remarks
-------
The **NET_REQUEST_QUEUE_TYPE** enumeration is used to specify queue type in the [**NET_REQUEST_QUEUE_CONFIG**](net-request-queue-config.md) structure.

The client driver passes an initialized [**NET_REQUEST_QUEUE_CONFIG**](net-request-queue-config.md) structure as an input parameter value to [**NetRequestQueueCreate**](netrequestqueuecreate.md).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Minimum KMDF version</p></td>
<td align="left"><p>1.21</p></td>
</tr>
<tr class="even">
<td align="left"><p>Minimum NetAdapterCx version</p></td>
<td align="left"><p>1.0</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Netrequestqueue.h</td>
</tr>
</tbody>
</table>

 

 





