---
title: FsRtlExitFileSystem function
description: The FsRtlExitFileSystem macro re-enables the delivery of normal kernel-mode APCs that were disabled by a preceding call to FsRtlEnterFileSystem.
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

## Syntax

```ManagedCPlusPlus
VOID FsRtlExitFileSystem(
   VOID 
);
```

## Parameters

**   
None

## Return value

This function does not return a value.

## Remarks

Every file system driver entry point routine must call [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md) immediately before acquiring a resource required in performing a file I/O request and call **FsRtlExitFileSystem** immediately afterward. This ensures that the routine cannot be suspended while running and thus block other file I/O requests.

Every successful call to [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md) must be matched by a subsequent call to **FsRtlExitFileSystem**.

Note that, unlike local file systems and network redirectors, file system filter drivers should never disable delivery of normal kernel APCs (by calling [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md) or [**KeEnterCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keentercriticalregion) or by raising to IRQL APC\_LEVEL) across a call to [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver).

The only time when a file system filter driver should disable normal kernel APCs is immediately before calling [**ExAcquireResourceExclusive**](../kernel/mmcreatemdl.md), [**ExAcquireResourceExclusiveLite**](/previous-versions/ff544351(v=vs.85)), [**ExAcquireResourceShared**](../kernel/mmcreatemdl.md), [**ExAcquireResourceSharedLite**](/previous-versions/ff544363(v=vs.85)), or [**ExAcquireSharedStarveExclusive**](/previous-versions/ff544367(v=vs.85)). After calling [**ExReleaseResource**](../kernel/mmcreatemdl.md) or [**ExReleaseResourceLite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleaseresourcelite), the filter driver should immediately re-enable delivery of normal kernel APCs. As an alternative to [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md), minifilter drivers can use the [**FltAcquireResourceExclusive**](fltacquireresourceexclusive.md), [**FltAcquireResourceShared**](fltacquireresourceshared.md), and [**FltReleaseResource**](fltreleaseresource.md) routines which properly handles APCs when acquiring and releasing a resource.

It is not necessary to disable normal kernel APCs before calling [**ExAcquireSharedWaitForExclusive**](/previous-versions/ff544370(v=vs.85)) because this routine calls [**KeRaiseIrqlToDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirqltodpclevel), which disables both normal and special kernel APCs. It is also not necessary to do so before calling [**ExAcquireFastMutex**](/previous-versions/windows/hardware/drivers/ff544337(v=vs.85)) or [**ExAcquireResourceExclusive**](../kernel/mmcreatemdl.md), because these routines disable normal kernel APCs.

## Requirements

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


[**ExAcquireFastMutex**](/previous-versions/windows/hardware/drivers/ff544337(v=vs.85))

[**ExAcquireResourceExclusive**](../kernel/mmcreatemdl.md)

[**ExAcquireResourceExclusiveLite**](/previous-versions/ff544351(v=vs.85))

[**ExAcquireResourceShared**](../kernel/mmcreatemdl.md)

[**ExAcquireResourceSharedLite**](/previous-versions/ff544363(v=vs.85))

[**ExAcquireSharedWaitForExclusive**](/previous-versions/ff544370(v=vs.85))

[**ExAcquireSharedStarveExclusive**](/previous-versions/ff544367(v=vs.85))

[**ExReleaseResource**](../kernel/mmcreatemdl.md)

[**ExReleaseResourceLite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleaseresourcelite)

[**ExTryToAcquireFastMutex**](/previous-versions/windows/hardware/drivers/ff545647(v=vs.85))

[**FltAcquireResourceExclusive**](fltacquireresourceexclusive.md)

[**FltAcquireResourceShared**](fltacquireresourceshared.md)

[**FltReleaseResource**](fltreleaseresource.md)

[**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md)

[**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)

[**KeLeaveCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keleavecriticalregion)

[**KeRaiseIrqlToDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirqltodpclevel)

 

