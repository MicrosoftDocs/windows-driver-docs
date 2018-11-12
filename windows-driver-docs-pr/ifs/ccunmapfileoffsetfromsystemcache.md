---
title: CcUnmapFileOffsetFromSystemCache routine
description: The CcUnmapFileOffsetFromSystemCache routine removes a portion of a cached file from the system cache.
ms.assetid: 37C4ACB9-343D-4F5F-A8B8-FB99A7EA274A
keywords: ["CcUnmapFileOffsetFromSystemCache routine Installable File System Drivers"]
topic_type:
- apiref
api_name:
- CcUnmapFileOffsetFromSystemCache
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# CcUnmapFileOffsetFromSystemCache routine


The [**CcUnmapFileOffsetFromSystemCache**](ccsetreadaheadgranularityex.md) routine removes a portion of a cached file from the system cache.

Syntax
------

```ManagedCPlusPlus
VOID CcUnmapFileOffsetFromSystemCache(
  _In_ PFILE_OBJECT   FileObject,
  _In_ PLARGE_INTEGER FileOffset,
  _In_ ULONG          Length,
  _In_ ULONG          Flags
);
```

Parameters
----------

*FileObject* \[in\]  
Pointer to a file object for the cached file whose cache memory will be unmapped.

*FileOffset* \[in\]  
Pointer to the file location to begin unmapping from the system cache.

*Length* \[in\]  
The length of the portion of the file to unmap from the cache. If *Length* is 0, then the remaining portion of the memory section for the file, beginning at *FileOffset*, is unmapped.

*Flags* \[in\]  
Not used. Set *Flags* to 0.

Return value
------------

None

Remarks
-------

Setting both *FileOffset* and *Length* to 0 will cause [**CcUnmapFileOffsetFromSystemCache**](ccsetreadaheadgranularityex.md) to unmap the entire memory section for a cached file.

[**CcUnmapFileOffsetFromSystemCache**](ccsetreadaheadgranularityex.md) allows file system drivers to reduce cache utilization when a large number of file portions are held in the system cache.

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

 

 





