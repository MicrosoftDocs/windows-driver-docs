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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# CcSetReadAheadGranularityEx routine


The **CcSetReadAheadGranularityEx** routine sets the read-ahead granularity and enables pipelined read-ahead for a cached file.

Syntax
------

```ManagedCPlusPlus
VOID CcSetReadAheadGranularityEx(
  _In_ PFILE_OBJECT FileObject,
  _In_ PREAD_AHEAD_PARAMETERS    ReadAheadParameters
);
```

Parameters
----------

*FileObject* \[in\]  
Pointer to a file object for the cached file whose read-ahead granularity is to be set.

*ReadAheadParameters* \[in\]  
Specifies the read ahead parameters. See [READ_AHEAD_PARAMETERS](read-ahead-parameters.md) for more information.

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

## See also


[**CcInitializeCacheMap**](https://msdn.microsoft.com/library/windows/hardware/ff539135)

[**CcReadAhead**](https://msdn.microsoft.com/library/windows/hardware/ff539191)

[**CcScheduleReadAhead**](https://msdn.microsoft.com/library/windows/hardware/ff539200)

[**CcSetAdditionalCacheAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff539203)

 

 






