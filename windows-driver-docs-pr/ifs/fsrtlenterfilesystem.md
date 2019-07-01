---
title: FsRtlEnterFileSystem function
description: The FsRtlEnterFileSystem macro temporarily disables the delivery of normal kernel-mode asynchronous procedure calls (APC). Special kernel-mode APCs are still delivered.
date: 06/25/2019
ms.assetid: 6aa6315d-e430-4189-8eb5-9427a2e5ba46
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

File system filter drivers can disable delivery of normal kernel APCs by calling **FsRtlEnterFileSystem** or [**KeEnterCriticalRegion**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-keentercriticalregion) prior to [**IoCallDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocalldriver) only if [**FsRtlExitFileSystem**](https://docs.microsoft.com/windows-hardware/drivers/ifs/fsrtlexitfilesystem) or [**KeLeaveCriticalRegion**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-keleavecriticalregion) is in the same dispatch routine. They should not call **FsRtlEnterFileSystem** or **KeEnterCriticalRegion** prior to **IoCallDriver** and then call **FsRtlExitFileSystem** or **KeLeaveCriticalRegion** in the *completion routine* of the IRP. Driver Verifier has a rule to help catch this condition.

File system filter drivers should disable normal kernel APCs before acquiring any resource. File system filter drivers acquire resources with the following routines:

* [**ExAcquireResourceExclusive**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mmcreatemdl)
* [**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351)
* [**ExAcquireResourceShared**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mmcreatemdl)
* [**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363)
* [**ExAcquireSharedStarveExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544367)
* [**ExAcquireSharedWaitForExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544370)

As an alternative to **FsRtlEnterFileSystem**, minifilter drivers can use the [**FltAcquireResourceExclusive**](fltacquireresourceexclusive.md), [**FltAcquireResourceShared**](fltacquireresourceshared.md), and [**FltReleaseResource**](fltreleaseresource.md) routines which properly handles APCs when acquiring and releasing a resource.

## Requirements

|   |   |
| - | - |
| Target platform | Desktop |
| Header | Ntifs.h (include Ntifs.h) |
| IRQL | <= APC_LEVEL |

## See also

[**ExAcquireResourceExclusive**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mmcreatemdl)

[**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351)

[**ExAcquireResourceShared**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mmcreatemdl)

[**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363)

[**ExAcquireSharedWaitForExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544370)

[**ExAcquireSharedStarveExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544367)

[**ExReleaseResource**](https://docs.microsoft.com/windows-hardware/drivers/kernel/mmcreatemdl)

[**ExReleaseResourceLite**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-exreleaseresourcelite)

[**ExTryToAcquireFastMutex**](https://docs.microsoft.com/previous-versions/windows/hardware/drivers/ff545647(v=vs.85))

[**FltAcquireResourceExclusive**](fltacquireresourceexclusive.md)

[**FltAcquireResourceShared**](fltacquireresourceshared.md)

[**FltReleaseResource**](fltreleaseresource.md)

[**FsRtlExitFileSystem**](fsrtlexitfilesystem.md)

[**IoCallDriver**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-iocalldriver)

[**KeEnterCriticalRegion**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/ntddk/nf-ntddk-keentercriticalregion)

[**KeRaiseIrqlToDpcLevel**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wdm/nf-wdm-keraiseirqltodpclevel)
