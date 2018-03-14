---
title: NDIS_WAIT_FOR_MUTEX macro
author: windows-driver-content
description: The NDIS_WAIT_FOR_MUTEX macro puts the current thread into the wait state until the specified mutex object is set to the signaled state.
ms.assetid: eaa323cc-4a17-4e94-8779-16efa079c5c4
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_WAIT_FOR_MUTEX macro Network Drivers Starting with Windows Vista
---

# NDIS\_WAIT\_FOR\_MUTEX macro


The NDIS\_WAIT\_FOR\_MUTEX macro puts the current thread into the wait state until the specified mutex object is set to the signaled state.

Syntax
------

```ManagedCPlusPlus
NTSTATUS NDIS_WAIT_FOR_MUTEX(
   PNDIS_MUTEX _Mutex_
);
```

Parameters
----------

*\_Mutex\_*   
A pointer to an initialized NDIS\_MUTEX-type mutex object. The caller initialized the mutex object in a prior call to the [**NDIS\_INIT\_MUTEX**](ndis-init-mutex.md) macro. NDIS\_MUTEX is a wrapper for the KMUTEX type.

Return value
------------

NDIS\_WAIT\_FOR\_MUTEX returns the following status value:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>STATUS_SUCCESS</strong></td>
<td><p>The operation completed successfully.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

NDIS network drivers should use the NDIS\_WAIT\_FOR\_MUTEX macro to wait for a mutex to transition to the signaled state.

A driver cannot wait for a nonzero time interval on a mutex object at a raised IRQL or in an *arbitrary thread context* (that is, the context of whatever thread is current when a driver function is called).

NDIS\_WAIT\_FOR\_MUTEX examines the current state of the mutex object to determine if the wait operation can be satisfied immediately. If the operation can be satisfied immediately, the necessary updates are made to mutex object. Otherwise, the current thread is in a waiting state, and a new thread is selected for execution on the current processor.

This macro is an NDIS wrapper for the [**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350) routine.

Callers of NDIS\_WAIT\_FOR\_MUTEX must be running at IRQL = PASSIVE\_LEVEL and in a nonarbitrary thread context.

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
<td><p>PASSIVE_LEVEL (see Remarks section)</p></td>
</tr>
<tr class="odd">
<td><p>DDI compliance rules</p></td>
<td>[<strong>Irql_Synch_Function</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548015)</td>
</tr>
</tbody>
</table>

## See also


[**KeWaitForSingleObject**](https://msdn.microsoft.com/library/windows/hardware/ff553350)

[**NDIS\_INIT\_MUTEX**](ndis-init-mutex.md)

[**NDIS\_RELEASE\_MUTEX**](ndis-release-mutex.md)

 

 




