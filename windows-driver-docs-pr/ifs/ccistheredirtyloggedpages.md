---
title: CcIsThereDirtyLoggedPages routine
description: The CcIsThereDirtyLoggedPages routine determines whether a volume contains any files that have dirty log data in the system cache.
ms.assetid: B8FDD817-87E6-4D82-B668-7F1078041281
keywords: ["CcIsThereDirtyLoggedPages routine Installable File System Drivers"]
topic_type:
- apiref
api_name:
- CcIsThereDirtyLoggedPages
api_location:
- NtosKrnl.exe
api_type:
- DllExport
---

# CcIsThereDirtyLoggedPages routine


The **CcIsThereDirtyLoggedPages** routine determines whether a volume contains any files that have dirty log data in the system cache.

Syntax
------

```ManagedCPlusPlus
BOOLEAN CcIsThereDirtyLoggedPages(
  _In_     PDEVICE_OBJECT DeviceObject,
  _In_opt_ PULONG         NumberOfDirtyPages
);
```

Parameters
----------

*DeviceObject* \[in\]  
A pointer to a device object associated with the volume to check.

*NumberOfDirtyPages* \[in, optional\]  
An optional pointer to an **ULONG** buffer that receives the number of dirty log pages on the volume associated with *DeviceObject*.

Return value
------------

The **CcIsThereDirtyLoggedPages** routine returns **TRUE** if the volume contains one or more cached files whose log data has been modified in the cache, but not yet flushed to disk. Otherwise, this routine returns **FALSE**.

Remarks
-------

This routine will return **TRUE** if any dirty log pages exist. It will also return **TRUE** if there are any log pages currently queued to the volume.

Unlike [**CcIsThereDirtyDataEx**](https://msdn.microsoft.com/library/windows/hardware/ff539152), the **CcIsThereDirtyLoggedPages** routine uses a file system device object to locate the volume cache information to check for dirty log pages.

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
<td align="left"><p>Available in Windows 8 and later versions of Windows.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Header</p></td>
<td align="left">Ntifs.h (include Ntifs.h or FltKernel.h)</td>
</tr>
<tr class="even">
<td align="left"><p>Library</p></td>
<td align="left">NtosKrnl.lib</td>
</tr>
<tr class="odd">
<td align="left"><p>DLL</p></td>
<td align="left">NtosKrnl.exe</td>
</tr>
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>PASSIVE_LEVEL</p></td>
</tr>
</tbody>
</table>

## See also


[**CcFlushCache**](https://msdn.microsoft.com/library/windows/hardware/ff539082)

[**CcPurgeCacheSection**](https://msdn.microsoft.com/library/windows/hardware/ff539188)

[**CcIsThereDirtyDataEx**](https://msdn.microsoft.com/library/windows/hardware/ff539152)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20CcIsThereDirtyLoggedPages%20routine%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





