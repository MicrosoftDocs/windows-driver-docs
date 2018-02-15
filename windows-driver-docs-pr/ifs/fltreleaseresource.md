---
title: FltReleaseResource routine
description: The FltReleaseResource routine releases a specified resource owned by the current thread.
ms.assetid: 2884c596-77ec-4cba-b6cb-000d96cc6342
keywords: ["FltReleaseResource routine Installable File System Drivers"]
topic_type:
- apiref
api_name:
- FltReleaseResource
api_location:
- fltmgr.sys
api_type:
- DllExport
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# FltReleaseResource routine


The **FltReleaseResource** routine releases a specified resource owned by the current thread.

Syntax
------

```ManagedCPlusPlus
VOID FltReleaseResource(
  _Inout_ PERESOURCE Resource
);
```

Parameters
----------

*Resource* \[in, out\]  
Pointer to the opaque ERESOURCE structure for the resource to be released.

Return value
------------

None

Remarks
-------

**FltReleaseResource** releases a resource that was previously acquired by calling [**FltAcquireResourceExclusive**](fltacquireresourceexclusive.md) or [**FltAcquireResourceShared**](fltacquireresourceshared.md).

**FltReleaseResource** is a wrapper for [**ExReleaseResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545597) that reenables normal kernel APC delivery.

Because **FltReleaseResource** reenables normal kernel APC delivery, it is not necessary to call [**KeLeaveCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552964) or [**FsRtlExitFileSystem**](fsrtlexitfilesystem.md) after calling **FltReleaseResource**.

To acquire a resource for exclusive access, call [**FltAcquireResourceExclusive**](fltacquireresourceexclusive.md).

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
<td align="left">[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
</tr>
<tr class="even">
<td align="left"><p>Version</p></td>
<td align="left"><p>This routine is available on Microsoft Windows XP SP2, Microsoft Windows Server 2003 SP1, and later.</p></td>
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
<td align="left"><p>DLL</p></td>
<td align="left">Fltmgr.sys</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>&lt;= DISPATCH_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**ExDeleteResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff544578)

[**ExInitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545317)

[**ExReinitializeResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545542)

[**ExReleaseResourceLite**](https://msdn.microsoft.com/library/windows/hardware/ff545597)

[**FltAcquireResourceExclusive**](fltacquireresourceexclusive.md)

[**FltAcquireResourceShared**](fltacquireresourceshared.md)

[**FsRtlExitFileSystem**](fsrtlexitfilesystem.md)

[**KeLeaveCriticalRegion**](https://msdn.microsoft.com/library/windows/hardware/ff552964)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20FltReleaseResource%20routine%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





