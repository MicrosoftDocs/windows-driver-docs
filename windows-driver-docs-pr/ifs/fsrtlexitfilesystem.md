---
title: FsRtlExitFileSystem function
description: The FsRtlExitFileSystem macro re-enables the delivery of normal kernel-mode APCs that were disabled by a preceding call to FsRtlEnterFileSystem.
ms.assetid: 763ceb1c-f614-4268-a7fe-73de0c354c71
keywords: ["FsRtlExitFileSystem function Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FsRtlExitFileSystem
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FsRtlExitFileSystem function


The **FsRtlExitFileSystem** macro re-enables the delivery of normal kernel-mode APCs that were disabled by a preceding call to [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md).

Syntax
------

```ManagedCPlusPlus
VOID FsRtlExitFileSystem(
   VOID 
);
```

Parameters
----------

**   
None

Return value
------------

This function does not return a value.

Remarks
-------

Every file system driver entry point routine must call [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md) immediately before acquiring a resource required in performing a file I/O request and call **FsRtlExitFileSystem** immediately afterward. This ensures that the routine cannot be suspended while running and thus block other file I/O requests.

Every successful call to [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md) must be matched by a subsequent call to **FsRtlExitFileSystem**.

Note that, unlike local file systems and network redirectors, file system filter drivers should never disable delivery of normal kernel APCs (by calling [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md) or [**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021) or by raising to IRQL APC\_LEVEL) across a call to [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

The only time when a file system filter driver should disable normal kernel APCs is immediately before calling [**ExAcquireResourceExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544345), [**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351), [**ExAcquireResourceShared**](https://msdn.microsoft.com/library/windows/hardware/ff544359), [**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363), or [**ExAcquireSharedStarveExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544367). After calling [**ExReleaseResource**](https://msdn.microsoft.com/library/windows/hardware/ff545571) or [**ExReleaseResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545597), the filter driver should immediately re-enable delivery of normal kernel APCs. As an alternative to [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md), minifilter drivers can use the [**FltAcquireResourceExclusive**](fltacquireresourceexclusive.md), [**FltAcquireResourceShared**](fltacquireresourceshared.md), and [**FltReleaseResource**](fltreleaseresource.md) routines which properly handles APCs when acquiring and releasing a resource.

It is not necessary to disable normal kernel APCs before calling [**ExAcquireSharedWaitForExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544370) because this routine calls [**KeRaiseIrqlToDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553084), which disables both normal and special kernel APCs. It is also not necessary to do so before calling [**ExAcquireFastMutex**](https://msdn.microsoft.com/library/windows/hardware/ff544337) or [**ExAcquireResourceExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544345), because these routines disable normal kernel APCs.

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
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h)</td>
</tr>
<tr class="odd">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>&lt;= APC_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**ExAcquireFastMutex**](https://msdn.microsoft.com/library/windows/hardware/ff544337)

[**ExAcquireResourceExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544345)

[**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351)

[**ExAcquireResourceShared**](https://msdn.microsoft.com/library/windows/hardware/ff544359)

[**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363)

[**ExAcquireSharedWaitForExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544370)

[**ExAcquireSharedStarveExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544367)

[**ExReleaseResource**](https://msdn.microsoft.com/library/windows/hardware/ff545571)

[**ExReleaseResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545597)

[**ExTryToAcquireFastMutex**](https://msdn.microsoft.com/library/windows/hardware/ff545647)

[**FltAcquireResourceExclusive**](fltacquireresourceexclusive.md)

[**FltAcquireResourceShared**](fltacquireresourceshared.md)

[**FltReleaseResource**](fltreleaseresource.md)

[**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md)

[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)

[**KeLeaveCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552964)

[**KeRaiseIrqlToDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553084)

 

 






