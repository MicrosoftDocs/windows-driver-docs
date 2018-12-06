---
title: Read ahead parameters
description: read-ahead parameters for  read-ahead granularity and pipelined read-ahead.
ms.assetid:
keywords: ["read-ahead parameters"]
topic_type:
- apiref
api_name:
- read_ahead_parame3ters
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.author: eliotgra
ms.date: 09/14/2017
ms.localizationpriority: medium
---

# READ_AHEAD_PARAMETERS structure

The **READ_AHEAD_PARAMETERS** structure contains publicly exposed read ahead parameters.

Syntax
------

```ManagedCPlusPlus
typedef struct _READ_AHEAD_PARAMETERS {

    CSHORT NodeByteSize;
    ULONG Granularity;
    ULONG PipelinedRequestSize;
    ULONG ReadAheadGrowthPercentage;

} READ_AHEAD_PARAMETERS, *PREAD_AHEAD_PARAMETERS;
```

Members
----------

*NodeByteSize* \[in\]  
Size of the node in bytes.

*Granularity* \[in\]  
Granularity of read aheads. This value must be an even power of 2 and greater than, or equal to PAGE_SIZE

*PipelinedRequestSize* \[in\]  
The request size in bytes, to be used when performing pipelined read-aheads. Each read ahead request that is pipelined is broken into smaller **PipelinedRequestSize** sized requests. This is typically used to increase the throughput by parallelizing multiple requets instead of one single big one.

> [!NOTE]
> Due to backward compatibility, If this value is zero, every read-ahead request will be broken into two.

*ReadAheadGrowthPercentage* \[in\]  
The growth of read ahead as a percentage of the data that has already been ready by the application so far. 


Remarks
-------

None 

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


[**CcSetReadAheadGranularityEx**](CcSetReadAheadGranularityEx.md)

[**CcReadAhead**](https://msdn.microsoft.com/library/windows/hardware/ff539191)

[**CcScheduleReadAhead**](https://msdn.microsoft.com/library/windows/hardware/ff539200)
