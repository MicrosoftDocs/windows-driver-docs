---
title: FsRtlEnterFileSystem function
description: The FsRtlEnterFileSystem macro temporarily disables the delivery of normal kernel-mode asynchronous procedure calls (APC). Special kernel-mode APCs are still delivered.
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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FsRtlEnterFileSystem function


The **FsRtlEnterFileSystem** macro temporarily disables the delivery of normal kernel-mode asynchronous procedure calls (APC). Special kernel-mode APCs are still delivered.

Syntax
------

```ManagedCPlusPlus
VOID FsRtlEnterFileSystem(
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

Every file system driver entry point routine must call **FsRtlEnterFileSystem** immediately before acquiring a resource required in performing a file I/O request and call [**FsRtlExitFileSystem**](fsrtlexitfilesystem.md) immediately afterward. This ensures that the routine cannot be suspended while running and thus block other file I/O requests.

Every successful call to **FsRtlEnterFileSystem** must be matched by a subsequent call to [**FsRtlExitFileSystem**](fsrtlexitfilesystem.md).

Note that, unlike local file systems and network redirectors, file system filter drivers should never disable delivery of normal kernel APCs (by calling **FsRtlEnterFileSystem** or [**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021) or by raising to IRQL APC\_LEVEL) across a call to [**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336).

File system filter drivers should disable normal kernel APCs before acquiring any resource. File system filter drivers acquire resources with the following routines:

-   [**ExAcquireResourceExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544345)

-   [**ExAcquireResourceExclusiveLite**](https://msdn.microsoft.com/library/windows/hardware/ff544351)

-   [**ExAcquireResourceShared**](https://msdn.microsoft.com/library/windows/hardware/ff544359)

-   [**ExAcquireResourceSharedLite**](https://msdn.microsoft.com/library/windows/hardware/ff544363)

-   [**ExAcquireSharedStarveExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544367)

-   [**ExAcquireSharedWaitForExclusive**](https://msdn.microsoft.com/library/windows/hardware/ff544370)

As an alternative to **FsRtlEnterFileSystem**, minifilter drivers can use the [**FltAcquireResourceExclusive**](fltacquireresourceexclusive.md), [**FltAcquireResourceShared**](fltacquireresourceshared.md), and [**FltReleaseResource**](fltreleaseresource.md) routines which properly handles APCs when acquiring and releasing a resource.

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

[**FsRtlExitFileSystem**](fsrtlexitfilesystem.md)

[**IoCallDriver**](https://msdn.microsoft.com/library/windows/hardware/ff548336)

[**KeEnterCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552021)

[**KeRaiseIrqlToDpcLevel**](https://msdn.microsoft.com/library/windows/hardware/ff553084)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FsRtlEnterFileSystem%20function%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





