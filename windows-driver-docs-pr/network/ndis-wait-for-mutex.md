---
title: NDIS\_WAIT\_FOR\_MUTEX macro
author: windows-driver-content
description: The NDIS\_WAIT\_FOR\_MUTEX macro puts the current thread into the wait state until the specified mutex object is set to the signaled state.
ms.assetid: eaa323cc-4a17-4e94-8779-16efa079c5c4
ms.author: windowsdriverdev 
ms.date: 0718/2017 
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_WAIT_FOR_MUTEX%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


