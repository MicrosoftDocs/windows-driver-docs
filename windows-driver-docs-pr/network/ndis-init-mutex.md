---
title: NDIS_INIT_MUTEX macro
author: windows-driver-content
description: The NDIS_INIT_MUTEX macro initializes a mutex object and sets it to a signaled state.
ms.assetid: d0d21732-e74d-42ac-a051-1f6a960092e1
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_INIT_MUTEX macro Network Drivers Starting with Windows Vista
---

# NDIS\_INIT\_MUTEX macro


The NDIS\_INIT\_MUTEX macro initializes a mutex object and sets it to a signaled state.

Syntax
------

```ManagedCPlusPlus
VOID NDIS_INIT_MUTEX(
   PNDIS_MUTEX _Mutex_
);
```

Parameters
----------

*\_Mutex\_*   
A pointer to a caller-supplied NDIS\_MUTEX-type mutex object. NDIS\_MUTEX is a wrapper for KMUTEX.

Return value
------------

None

Remarks
-------

NDIS network drivers should use the NDIS\_INIT\_MUTEX macro to initialize a mutex.

The initial state of the mutex object is the signaled state. To acquire the mutex, call the [**NDIS\_WAIT\_FOR\_MUTEX**](ndis-wait-for-mutex.md) macro. To release the mutex, call the [**NDIS\_RELEASE\_MUTEX**](ndis-release-mutex.md) macro.

A driver cannot wait for a nonzero time interval on a mutex object at a raised IRQL or in an *arbitrary thread context* (that is, the context of whatever thread is current when a driver function is called).

Storage for a mutex object must reside in a driver context area or in a nonpaged pool that the caller allocated.

The NDIS\_INIT\_MUTEX macro is an NDIS wrapper for the [**KeInitializeMutex**](https://msdn.microsoft.com/library/windows/hardware/ff552147) routine.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Target platform</p></td>
<td>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
</tr>
<tr class="even">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and later.</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
<tr class="even">
<td><p>IRQL</p></td>
<td><p>Any level</p></td>
</tr>
</tbody>
</table>

## See also


[**KeInitializeMutex**](https://msdn.microsoft.com/library/windows/hardware/ff552147)

[**NDIS\_RELEASE\_MUTEX**](ndis-release-mutex.md)

[**NDIS\_WAIT\_FOR\_MUTEX**](ndis-wait-for-mutex.md)

 

 




