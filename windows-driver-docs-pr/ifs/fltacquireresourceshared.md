---
title: FltAcquireResourceShared routine
description: The FltAcquireResourceShared routine acquires the given resource for shared access by the calling thread.
ms.assetid: 5232cdba-1050-46b6-8c21-177d4cd1721d
keywords: ["FltAcquireResourceShared routine Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FltAcquireResourceShared
api_location:
- FltMgr.lib
- FltMgr.dll
api_type:
- LibDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FltAcquireResourceShared routine


The **FltAcquireResourceShared** routine acquires the given resource for shared access by the calling thread.

Syntax
------

```ManagedCPlusPlus
VOID FltAcquireResourceShared(
  _Inout_ PERESOURCE Resource
);
```

Parameters
----------

*Resource* \[in, out\]  
Pointer to an opaque ERESOURCE structure. This structure must be allocated by the caller from nonpaged pool and initialized by calling [**ExInitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545317) or [**ExReinitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545542).

Return value
------------

None

Remarks
-------

This routine is available on Microsoft Windows XP SP2, Microsoft Windows Server 2003 SP1, and later.

The **FltAcquireResourceShared** routine acquires the given resource for shared access by the calling thread.

Whether or when the caller is given shared access to the given resource depends on the following:

-   If the resource is currently unowned, shared access is granted immediately to the current thread.

-   If the caller already has acquired the resource (for shared or exclusive access), the current thread is granted the same type of access recursively. Note that making this call does not convert a caller's exclusive ownership of a given resource to shared.

-   If the resource is currently owned as shared by another thread and no thread is waiting for exclusive access to the resource, shared access is granted to the caller immediately. The caller is put into a wait state if there is an exclusive waiter.

-   If the resource is currently owned as exclusive by another thread or if there is another thread waiting for exclusive access and the caller does not already have shared access to the resource, the current thread is put into a wait state until the resource can be acquired.

**FltAcquireResourceShared** is a wrapper for [**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363) that disables normal kernel APC delivery.

Because **FltAcquireResourceShared** disables normal kernel APC delivery, it is not necessary to call [**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021) or [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md) before calling **FltAcquireResourceShared**.

To release the resource after it is acquired, call [**FltReleaseResource**](fltreleaseresource.md). Every successful call to **FltAcquireResourceShared** must be matched by a subsequent call to **FltReleaseResource**.

To acquire a resource for exclusive access, call [**FltAcquireResourceExclusive**](fltacquireresourceexclusive.md).

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
<td align="left"><p>Header</p></td>
<td align="left">Fltkernel.h (include Fltkernel.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>Library</p></td>
<td align="left">FltMgr.lib</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>&lt;= APC_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363)

[**ExDeleteResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff544578)

[**ExInitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545317)

[**ExReinitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545542)

[**FltAcquireResourceExclusive**](fltacquireresourceexclusive.md)

[**FltReleaseResource**](fltreleaseresource.md)

[**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md)

[**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021)

 

 






