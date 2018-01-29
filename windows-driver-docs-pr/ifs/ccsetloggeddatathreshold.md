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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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


[**CcSetLogHandleForFileEx**](ccsetloghandleforfileex.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20CcSetLoggedDataThreshold%20routine%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





