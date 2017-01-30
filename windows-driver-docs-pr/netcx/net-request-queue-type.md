---
title: NET_REQUEST_QUEUE_TYPE enumeration
description: .
ms.assetid: 34aa0f46-b86f-4ee3-82ff-7fd8e2f86f54
keywords: ["NET_REQUEST_QUEUE_TYPE enumeration Network Drivers Starting with Windows Vista"]
topic_type:
- apiref
api_name:
- NET_REQUEST_QUEUE_TYPE
api_location:
- netrequestqueue.h
api_type:
- HeaderDef
---

# NET\_REQUEST\_QUEUE\_TYPE enumeration


[!include[NetAdapterCx Beta Prerelease](../netcx-beta-prerelease.md)]

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

<a href="" id="netrequestqueuetypeinvalid"></a>**NetRequestQueueTypeInvalid**  

<a href="" id="netrequestqueuedefaultsequential"></a>**NetRequestQueueDefaultSequential**  

<a href="" id="netrequestqueuedefaultparallel"></a>**NetRequestQueueDefaultParallel**  

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

 

 





