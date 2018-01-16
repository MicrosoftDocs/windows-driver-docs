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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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

```
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

```
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
<td align="left">[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</td>
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bifsk\ifsk%5D:%20CcSetLogHandleForFileEx%20routine%20%20RELEASE:%20%281/9/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





