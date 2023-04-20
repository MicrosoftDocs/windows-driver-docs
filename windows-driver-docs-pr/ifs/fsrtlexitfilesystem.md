---
title: FsRtlExitFileSystem function
description: Learn more about the FsRtlExitFileSystem macro.
keywords: ["FsRtlExitFileSystem function Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FsRtlExitFileSystem
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 03/13/2023
ms.topic: reference
---

# FsRtlExitFileSystem function

The **FsRtlExitFileSystem** macro re-enables the delivery of normal kernel-mode APCs that a preceding call to [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md) disabled.

## Syntax

```ManagedCPlusPlus
VOID FsRtlExitFileSystem(
   VOID 
);
```

## Parameters

None

## Return value

This function doesn't return a value.

## Remarks

Every file system driver entry point routine must call [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md) immediately before acquiring a resource required in performing a file I/O request and call **FsRtlExitFileSystem** immediately afterward. This ensures that the routine can't be suspended while running and thus block other file I/O requests.

Every successful call to [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md) must be matched by a subsequent call to **FsRtlExitFileSystem**.

Unlike local file systems and network redirectors, file system filter drivers should never disable delivery of normal kernel APCs (by calling [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md) or [**KeEnterCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keentercriticalregion) or by raising to IRQL APC_LEVEL) across a call to [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver).

The only time when a file system filter driver should disable normal kernel APCs is immediately before calling [**ExAcquireResourceExclusive**](../kernel/mmcreatemdl.md), [**ExAcquireResourceExclusiveLite**](/previous-versions/ff544351(v=vs.85)), [**ExAcquireResourceShared**](../kernel/mmcreatemdl.md), [**ExAcquireResourceSharedLite**](/previous-versions/ff544363(v=vs.85)), or [**ExAcquireSharedStarveExclusive**](/previous-versions/ff544367(v=vs.85)). After the filter driver calls [**ExReleaseResource**](../kernel/mmcreatemdl.md) or [**ExReleaseResourceLite**](/windows-hardware/drivers/ddi/wdm/nf-wdm-exreleaseresourcelite), it should immediately re-enable delivery of normal kernel APCs. As an alternative to [**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md), minifilter drivers can use the [**FltAcquireResourceExclusive**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltacquireresourceexclusive), [**FltAcquireResourceShared**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltacquireresourceshared), and [**FltReleaseResource**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleaseresource) routines, which properly handle APCs when acquiring and releasing a resource.

It isn't necessary to disable normal kernel APCs before calling [**ExAcquireSharedWaitForExclusive**](/previous-versions/ff544370(v=vs.85)) because this routine calls [**KeRaiseIrqlToDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirqltodpclevel), which disables both normal and special kernel APCs. It's also not necessary to do so before calling [**ExAcquireFastMutex**](/previous-versions/windows/hardware/drivers/ff544337(v=vs.85)) or [**ExAcquireResourceExclusive**](../kernel/mmcreatemdl.md), because these routines disable normal kernel APCs.

## Requirements

| Requirement type | Requirement |
| ---------------- | ----------- |
| Header | *Ntifs.h* (include *Ntifs.h*) |
| IRQL   | <= APC_LEVEL |

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

[**FltAcquireResourceExclusive**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltacquireresourceexclusive)

[**FltAcquireResourceShared**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltacquireresourceshared)

[**FltReleaseResource**](/windows-hardware/drivers/ddi/fltkernel/nf-fltkernel-fltreleaseresource)

[**FsRtlEnterFileSystem**](fsrtlenterfilesystem.md)

[**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)

[**KeLeaveCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keleavecriticalregion)

[**KeRaiseIrqlToDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirqltodpclevel)
