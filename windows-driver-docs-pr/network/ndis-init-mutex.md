---
title: NDIS_INIT_MUTEX macro
author: windows-driver-content
description: The NDIS_INIT_MUTEX macro initializes a mutex object and sets it to a signaled state.
ms.assetid: d0d21732-e74d-42ac-a051-1f6a960092e1
ms.author: windowsdriverdev 
ms.date: 0718/2017 
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_INIT_MUTEX%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


