---
title: CcSetLogHandleForFileEx routine
description: The CcSetLogHandleForFileEx routine sets a log handle for a file and tracking callback functions for the file log.
ms.assetid: D56BEAC9-6AB8-44BA-ADFC-D2435A1458DB
keywords: ["CcSetLogHandleForFileEx routine Installable File System Drivers"]
topic_type:
- apiref
api_name:
- CcSetLogHandleForFileEx
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# CcSetLogHandleForFileEx routine


The **CcSetLogHandleForFileEx** routine sets a log handle for a file and tracking callback functions for the file log.

Syntax
------

```ManagedCPlusPlus
VOID CcSetLogHandleForFileEx(
  _In_ PFILE_OBJECT     FileObject,
  _In_ PVOID            LogHandle,
  _In_ PFLUSH_TO_LSN    FlushToLsnRoutine,
  _In_ PQUERY_LOG_USAGE QueryLogUsageRoutine
);
```

Parameters
----------

*FileObject* \[in\]
Pointer to the file object for the file for which the log handle is to be stored.

*LogHandle* \[in\]
Pointer to the log handle that is to be stored.

*FlushToLsnRoutine* \[in\]
Pointer to a log file flush callback routine to call before flushing buffers for this file. This routine is called to ensure that a log file is flushed to the most recent logical sequence number (LSN) for any buffer control block (BCB) being flushed. This routine is declared as follows:

```cpp
typedef
VOID (*PFLUSH_TO_LSN) (
            IN PVOID LogHandle,
            IN LARGE_INTEGER Lsn
            );
```

<a href="" id="loghandle"></a>
***LogHandle***

Pointer to an opaque structure that is used to identify this client.

<a href="" id="lsn"></a>
***Lsn***

This is the LSN that must be on the disk on return from this callback routine.

*QueryLogUsageRoutine* \[in\]
Pointer to a client callback routine to call to retrieve the percentage of log usage for this file. This routine is called to check if thresholds are met to initiate a write of dirty pages. This routine is declared as follows:

```cpp
typedef  
VOID (*PQUERY_LOG_USAGE) (  
            IN PVOID LogHandle,  
            OUT PUSHORT PercentageFull  
            );  
```

<a href="" id="loghandle"></a>
***LogHandle***

Pointer to an opaque structure that is used to identify this client.

<a href="" id="percentagefull"></a>
***PercentageFull***

A value between 0 and 100 indicating percentage of log usage.

Return value
------------

None

Remarks
-------

**CcSetLogHandleForFileEx** sets a log handle for a file, for use in subsequent calls to [**CcGetDirtyPages**](https://msdn.microsoft.com/library/windows/hardware/ff539088).

Callbacks for *FlushToLsnRoutine* and *QueryLogUsageRoutine* are required. These values must not be NULL.

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
<td align="left"><p>Available on Windows 8 and later.</p></td>
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
<tr class="even">
<td align="left"><p>IRQL</p></td>
<td align="left"><p>Any level</p></td>
</tr>
</tbody>
</table>

## See also


[**CcGetDirtyPages**](https://msdn.microsoft.com/library/windows/hardware/ff539088)

[**CcSetDirtyPinnedData**](https://msdn.microsoft.com/library/windows/hardware/ff539211)

 

 






