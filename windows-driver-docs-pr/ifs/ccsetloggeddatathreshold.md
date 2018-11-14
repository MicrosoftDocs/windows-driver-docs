---
title: CcSetLoggedDataThreshold routine
description: The CcSetLoggedDataThreshold routine sets a threshold for when a scan of dirty log pages will initiate a lazy write.
ms.assetid: 067121C3-3BD6-48EA-BD8E-B28620F799E1
keywords: ["CcSetLoggedDataThreshold routine Installable File System Drivers"]
topic_type:
- apiref
api_name:
- CcSetLoggedDataThreshold
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# CcSetLoggedDataThreshold routine


The [**CcSetLoggedDataThreshold**](ccistheredirtyloggedpages.md) routine sets a threshold for when a scan of dirty log pages will initiate a lazy write.

Syntax
------

```ManagedCPlusPlus
VOID CcSetLoggedDataThreshold(
  _In_ PVOID LogHandle,
  _In_ ULONG NumberOfPages
);
```

Parameters
----------

*LogHandle* \[in\]  
Log handle for the new threshold.

*NumberOfPages* \[in\]  
The threshold number in dirty log pages for the log specified by *LogHandle*.

Return value
------------

None

Remarks
-------

The threshold value in *NumberOfPages* is used only if the value returned in the *PercentageUsed* parameter of the *QueryLogUsageRoutine* callback routine is 0. The *QueryLogUsageRoutine* callback is set with a call to [**CcSetLogHandleForFileEx**](ccsetloghandleforfileex.md).

The [**CcSetLoggedDataThreshold**](ccistheredirtyloggedpages.md) routine is used to set a fixed value in number of dirty log pages when a log full percentage is not used.

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


[**CcSetLogHandleForFileEx**](ccsetloghandleforfileex.md)

 

 






