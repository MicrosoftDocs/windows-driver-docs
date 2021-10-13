---
title: FsRtlEnterFileSystem function
description: The FsRtlEnterFileSystem macro temporarily disables the delivery of normal kernel-mode asynchronous procedure calls (APC). Special kernel-mode APCs are still delivered.
date: 06/25/2019
keywords: ["FsRtlEnterFileSystem function Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FsRtlEnterFileSystem
api_location:
- Ntifs.h
api_type:
- HeaderDef
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# FsRtlEnterFileSystem function

The **FsRtlEnterFileSystem** macro temporarily disables the delivery of normal kernel-mode asynchronous procedure calls (APC). Special kernel-mode APCs are still delivered.

## Syntax

```ManagedCPlusPlus
VOID FsRtlEnterFileSystem(
   VOID
);
```

## Parameters

None

## Return value

This function does not return a value.

## Remarks

Every file system driver entry point routine must call **FsRtlEnterFileSystem** immediately before acquiring a resource required in performing a file I/O request and call [**FsRtlExitFileSystem**](fsrtlexitfilesystem.md) immediately afterward. This ensures that the routine cannot be suspended while running and thus block other file I/O requests.

Every successful call to **FsRtlEnterFileSystem** must be matched by a subsequent call to [**FsRtlExitFileSystem**](fsrtlexitfilesystem.md).

File system filter drivers can disable delivery of normal kernel APCs by calling **FsRtlEnterFileSystem** or [**KeEnterCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keentercriticalregion) prior to [**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver) only if [**FsRtlExitFileSystem**](./fsrtlexitfilesystem.md) or [**KeLeaveCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keleavecriticalregion) is in the same dispatch routine. They should not call **FsRtlEnterFileSystem** or **KeEnterCriticalRegion** prior to **IoCallDriver** and then call **FsRtlExitFileSystem** or **KeLeaveCriticalRegion** in the *completion routine* of the IRP. Driver Verifier has a rule to help catch this condition.

File system filter drivers should disable normal kernel APCs before acquiring any resource. File system filter drivers acquire resources with the following routines:

* [**ExAcquireResourceExclusive**](../kernel/mmcreatemdl.md)
* [**ExAcquireResourceExclusiveLite**](/previous-versions/ff544351(v=vs.85))
* [**ExAcquireResourceShared**](../kernel/mmcreatemdl.md)
* [**ExAcquireResourceSharedLite**](/previous-versions/ff544363(v=vs.85))
* [**ExAcquireSharedStarveExclusive**](/previous-versions/ff544367(v=vs.85))
* [**ExAcquireSharedWaitForExclusive**](/previous-versions/ff544370(v=vs.85))

As an alternative to **FsRtlEnterFileSystem**, minifilter drivers can use the [**FltAcquireResourceExclusive**](fltacquireresourceexclusive.md), [**FltAcquireResourceShared**](fltacquireresourceshared.md), and [**FltReleaseResource**](fltreleaseresource.md) routines which properly handles APCs when acquiring and releasing a resource.

## Requirements

**Target platform**: Desktop

**Header**: Ntifs.h (include Ntifs.h)

**IRQL**: <= APC_LEVEL


## See also

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

[**FsRtlExitFileSystem**](fsrtlexitfilesystem.md)

[**IoCallDriver**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iocalldriver)

[**KeEnterCriticalRegion**](/windows-hardware/drivers/ddi/ntddk/nf-ntddk-keentercriticalregion)

[**KeRaiseIrqlToDpcLevel**](/windows-hardware/drivers/ddi/wdm/nf-wdm-keraiseirqltodpclevel)
