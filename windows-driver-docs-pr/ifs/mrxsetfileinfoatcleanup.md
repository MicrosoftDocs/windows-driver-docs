---
title: MRxSetFileInfoAtCleanup routine
description: The MRxSetFileInfoAtCleanup routine is called by RDBSS to request that a network mini-redirector set file information on a file system object at cleanup.
ms.assetid: 099244ee-cc66-4500-9fee-a10238aaa66c
keywords: ["MRxSetFileInfoAtCleanup routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxSetFileInfoAtCleanup
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MRxSetFileInfoAtCleanup routine


The *MRxSetFileInfoAtCleanup* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to request that a network mini-redirector set file information on a file system object at cleanup.

Syntax
------

```ManagedCPlusPlus
PMRX_CALLDOWN MRxSetFileInfoAtCleanup;

NTSTATUS MRxSetFileInfoAtCleanup(
  _Inout_ PRX_CONTEXT RxContext
)
{ ... }
```

Parameters
----------

*RxContext* \[in, out\]  
A pointer to the RX\_CONTEXT structure. This parameter contains the IRP that is requesting the operation.

Return value
------------

*MRxSetFileInfoAtCleanup* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value.

Remarks
-------

RDBSS issues a call to *MRxSetFileInfoAtCleanup* during cleanup, when the last handle to a file object is closed. This is different than the close operation which is invoked when the last reference to a file object is deleted.

*MRxSetFileInfoAtCleanup* is called by RDBSS if the timestamps on a file or the size of a file have changed. The calls to *MRxSetFileInfoAtCleanup* by RDBSS are made separately for each of these changes. If both the file size and the timestamps have changed, then RDBSS makes two calls to *MRxSetFileInfoAtCleanup*.

Before calling *MRxSetFileInfoAtCleanup*, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter if the timestamps on a file have changed:

The **Info.FileInformationClass** member is set to a FILE\_INFORMATION\_CLASS value of FileBasicInformation.

The **Info.Buffer** member is set to a FILE\_BASIC\_INFORMATION structure allocated on the stack.

The **Info.Length** member is set to the sizeof a FILE\_BASIC\_INFORMATION structure.

Before calling *MRxSetFileInfoAtCleanup*, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter if the size of a file has changed:

The **Info.FileInformationClass** member is set to a FILE\_INFORMATION\_CLASS value of FileEndOfFileInformation.

The **Info.Buffer** member is set to a FILE\_END\_OF\_FILE\_INFORMATION structure allocated on the stack.

The **Info.Length** member is set to <strong>sizeof(</strong>FILE\_END\_OF\_FILE\_INFORMATION<strong>)</strong>.

RDBSS ignores the return value from *MRxSetFileInfoAtCleanup*.

A network mini-redirector can choose to do nothing in this routine and return STATUS\_SUCCESS. Any changes to the file size or timestamps will be handled during the cleanup operation.

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
<td align="left">Desktop</td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Mrx.h (include Mrx.h)</td>
</tr>
</tbody>
</table>

## See also


[**MRxIsValidDirectory**](https://msdn.microsoft.com/library/windows/hardware/ff550696)

[**MRxQueryDirectory**](mrxquerydirectory.md)

[**MRxQueryEaInfo**](mrxqueryeainfo.md)

[**MRxQueryFileInfo**](mrxqueryfileinfo.md)

[**MRxQueryQuotaInfo**](mrxqueryquotainfo.md)

[**MRxQuerySdInfo**](mrxquerysdinfo.md)

[**MRxQueryVolumeInfo**](mrxqueryvolumeinfo.md)

[**MRxSetEaInfo**](mrxseteainfo.md)

[**MRxSetFileInfo**](mrxsetfileinfo.md)

[**MRxSetQuotaInfo**](mrxsetquotainfo.md)

[**MRxSetSdInfo**](mrxsetsdinfo.md)

[**MRxSetVolumeInfo**](mrxsetvolumeinfo.md)

 

 






