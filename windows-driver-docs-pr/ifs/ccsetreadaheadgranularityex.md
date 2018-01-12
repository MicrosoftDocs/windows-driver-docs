---
title: CcSetReadAheadGranularityEx routine
description: The CcSetReadAheadGranularityEx routine sets the read-ahead granularity and enables pipelined read-ahead for a cached file.
ms.assetid: D70C3397-CF37-46E5-BA84-819BC984665A
keywords: ["CcSetReadAheadGranularityEx routine Installable File System Drivers"]
topic_type:
- apiref
api_name:
- CcSetReadAheadGranularityEx
api_location:
- NtosKrnl.exe
api_type:
- DllExport
---

# CcSetReadAheadGranularityEx routine


The **CcSetReadAheadGranularityEx** routine sets the read-ahead granularity and enables pipelined read-ahead for a cached file.

Syntax
------

```ManagedCPlusPlus
VOID CcSetReadAheadGranularityEx(
  _In_ PFILE_OBJECT FileObject,
  _In_ ULONG        Granularity,
  _In_ ULONG        PipelinedRequestSize
);
```

Parameters
----------

*FileObject* \[in\]  
Pointer to a file object for the cached file whose read-ahead granularity is to be set.

*Granularity* \[in\]  
Specifies the desired read-ahead granularity, which must be an even power of two and must be greater than or equal to PAGE\_SIZE.

*PipelinedRequestSize* \[in\]  
Specifies a desired read-ahead request size to override the system computed request size. If *PipelinedRequestSize* is 0, the current read-ahead request size is set to itself divided by 2.

Return value
------------

None

Remarks
-------

Calling **CcSetReadAheadGranularityEx** will enable pipelined read-ahead requests for the file object in *FileObject*. Selecting an appropriate value for *PipelinedRequestSize* will divide read-ahead requests into smaller multiple parallel requests. Callers of **CcSetReadAheadGranularityEx** can tune read-ahead performance by adjusting *PipelinedRequestSize*.

After [**CcInitializeCacheMap**](https://msdn.microsoft.com/library/windows/hardware/ff539135) is called to cache a file, but before **CcSetReadAheadGranularityEx** is called for the cached file, the default read-ahead granularity for the cached file is equal to PAGE\_SIZE.

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
<td align="left">Ntifs.h (include Ntifs.h)</td>
</tr>
<tr class="even">
<td align="left"><p>Library</p></td>
<td align="left">NtosKrnl.lib</td>
</tr>
<tr class="odd">
<td align="left"><p>DLL</p></td>
<td align="left">NtosKrnl.exe</td>
</tr>
</tbody>
</table>

## See also


[**CcInitializeCacheMap**](https://msdn.microsoft.com/library/windows/hardware/ff539135)

[**CcReadAhead**](https://msdn.microsoft.com/library/windows/hardware/ff539191)

[**CcScheduleReadAhead**](https://msdn.microsoft.com/library/windows/hardware/ff539200)

[**CcSetAdditionalCacheAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff539203)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20CcSetReadAheadGranularityEx%20routine%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





