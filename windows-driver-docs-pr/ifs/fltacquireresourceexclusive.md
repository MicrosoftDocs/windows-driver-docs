---
title: FltAcquireResourceExclusive routine
description: The FltAcquireResourceExclusive routine acquires the given resource for exclusive access by the calling thread.
ms.assetid: 3736582e-33eb-4967-acfa-4b9d2b8cd87f
keywords: ["FltAcquireResourceExclusive routine Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FltAcquireResourceExclusive
api_location:
- fltMgr.lib
- fltMgr.dll
api_type:
- LibDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FltAcquireResourceExclusive routine


The **FltAcquireResourceExclusive** routine acquires the given resource for exclusive access by the calling thread.

Syntax
------

```ManagedCPlusPlus
VOID FltAcquireResourceExclusive(
  _Inout_ PERESOURCE Resource
);
```

Parameters
----------

*Resource* \[in, out\]  
A pointer to an opaque ERESOURCE structure. This structure must be allocated by the caller from nonpaged pool and initialized by calling [**ExInitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545317) or [**ExReinitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545542).

Return value
------------

None

Remarks
-------

This routine is available on Windows XP with Service Pack 2 (SP2), Windows Server 2003 with Service Pack 1 (SP1), and later versions of Windows.

**FltAcquireResourceExclusive** acquires the given resource for exclusive access by the calling thread.

The following circumstances determine whether or when the caller is given exclusive access to the given resource:

-   If the resource is currently not owned, exclusive access is granted immediately to the current thread.

-   If the caller already has acquired the resource for exclusive access, the current thread is granted the same type of access recursively.

-   Callers who have shared access to the resource must release the lock and then reacquire it exclusively.

-   If the resource is currently owned as exclusive by another thread, or if the caller only has shared access to the resource, the current thread is put into a wait state until the resource can be acquired.

&gt; \[!Note\]
&gt;   If two threads each hold a shared lock on the same resource and both attempt to acquire the lock exclusively without releasing their shared lock, they will deadlock. This means that each thread will wait for the other to release its shared hold on the lock, and neither will release its shared hold until the other does.

 

**FltAcquireResourceExclusive** is a wrapper for [**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351) that disables normal kernel APC delivery.

Because **FltAcquireResourceExclusive** disables normal kernel APC delivery, it is not necessary to call [**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021) or [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md) before calling **FltAcquireResourceExclusive**.

To release the resource after it is acquired, call [**FltReleaseResource**](fltreleaseresource.md). Every successful call to **FltAcquireResourceExclusive** must be matched by a subsequent call to **FltReleaseResource**.

To acquire a resource for shared access, call [**FltAcquireResourceShared**](fltacquireresourceshared.md).

To delete a resource from the system's resource list, call [**ExDeleteResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff544578).

To initialize a resource for reuse, call [**ExReinitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545542).

For more information about ERESOURCE structures, see [Introduction to ERESOURCE Routines](https://msdn.microsoft.com/library/windows/hardware/ff548046) in the Kernel Architecture Design Guide.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Target platform</p></td>
<td align="left"><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" data-raw-source="[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)">Universal</a></td>
</tr>
<tr class="even">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows XP SP2, Windows Server 2003 SP1, and later versions of all Windows operating systems.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Fltkernel.h (include Fltkernel.h)</td>
</tr>
<tr class="even">
<td align="left"><p>Library</p></td>
<td align="left">FltMgr.lib</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>&lt;= APC_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351)

[**ExDeleteResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff544578)

[**ExInitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545317)

[**ExReinitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545542)

[**FltAcquireResourceShared**](fltacquireresourceshared.md)

[**FltReleaseResource**](fltreleaseresource.md)

[**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md)

[**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021)

 

 






