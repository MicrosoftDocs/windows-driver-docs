---
title: NDIS_RELEASE_MUTEX macro
author: windows-driver-content
description: The NDIS_RELEASE_MUTEX macro releases the specified mutex object.
ms.assetid: 0358f584-c1a2-4462-8294-09504eb18b17
ms.author: windowsdriverdev 
ms.date: 0718/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - NDIS_RELEASE_MUTEX macro Network Drivers Starting with Windows Vista
---

# NDIS\_RELEASE\_MUTEX macro


The NDIS\_RELEASE\_MUTEX macro releases the specified mutex object.

Syntax
------

```ManagedCPlusPlus
LONG NDIS_RELEASE_MUTEX(
   PNDIS_MUTEX _Mutex_
);
```

Parameters
----------

*\_Mutex\_*   
A pointer to an initialized NDIS\_MUTEX-type mutex object. The caller initialized the mutex object in a prior call to the [**NDIS\_INIT\_MUTEX**](ndis-init-mutex.md) macro. NDIS\_MUTEX is a wrapper for the KMUTEX type.

Return value
------------

NDIS\_RELEASE\_MUTEX returns a LONG value. If the return value is zero, the mutex object was released and is in the signaled state. If NDIS\_RELEASE MUTEX returns a nonzero value, the mutex is not in the signaled state.

Remarks
-------

NDIS network drivers should use the NDIS\_RELEASE\_MUTEX macro to release a mutex.

Only the thread that is currently holding the mutex object can release it. Otherwise, a bugcheck occurs. A bugcheck also occurs if a driver attempts to release a mutex object that is in the signaled state.

To acquire the mutex, call the [**NDIS\_WAIT\_FOR\_MUTEX**](ndis-wait-for-mutex.md) macro. If a mutex is acquired recursively, the holding thread must call NDIS\_RELEASE\_MUTEX the same number of times that it acquired the mutex to set it back to the signaled state.

NDIS\_RELEASE\_MUTEX is an NDIS wrapper for the [**KeReleaseMutex**](https://msdn.microsoft.com/library/windows/hardware/ff553140) routine.

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
<td><p>PASSIVE_LEVEL</p></td>
</tr>
<tr class="odd">
<td><p>DDI compliance rules</p></td>
<td>[<strong>Irql_Synch_Function</strong>](https://msdn.microsoft.com/library/windows/hardware/ff548015)</td>
</tr>
</tbody>
</table>

## See also


[**KeReleaseMutex**](https://msdn.microsoft.com/library/windows/hardware/ff553140)

[**NDIS\_INIT\_MUTEX**](ndis-init-mutex.md)

[**NDIS\_WAIT\_FOR\_MUTEX**](ndis-wait-for-mutex.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20NDIS_RELEASE_MUTEX%20macro%20%20RELEASE:%20%287/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


