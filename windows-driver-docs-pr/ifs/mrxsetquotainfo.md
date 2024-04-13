---
title: MRxSetQuotaInfo Routine
description: TheMRxSetQuotaInfo routine is called by RDBSS to request that a network mini-redirector set quota information on a file system object.
keywords: ["MRxSetQuotaInfo routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxSetQuotaInfo
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 03/13/2023
ms.topic: reference
---

# MRxSetQuotaInfo routine


The*MRxSetQuotaInfo* routine is called by [RDBSS](./the-rdbss-driver-and-library.md) to request that a network mini-redirector set quota information on a file system object.

## Syntax

```ManagedCPlusPlus
PMRX_CALLDOWN MRxSetQuotaInfo;

NTSTATUS MRxSetQuotaInfo(
  _Inout_ PRX_CONTEXT RxContext
)
{ ... }
```

## Parameters

*RxContext* \[in, out\]  
A pointer to the RX\_CONTEXT structure. This parameter contains the IRP that is requesting the operation.

## Return value

*MRxSetQuotaInfo* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as one of the following:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Return code</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><strong>STATUS_ACCESS_DENIED</strong></td>
<td align="left"><p>The caller lacked the proper security for this operation.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_CONNECTION_DISCONNECTED</strong></td>
<td align="left"><p>The connection was disconnected.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_INSUFFICIENT_RESOURCES</strong></td>
<td align="left"><p>There were insufficient resources to complete the query.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_INVALID_PARAMETER</strong></td>
<td align="left"><p>An invalid parameter was specified.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_NOT_SUPPORTED</strong></td>
<td align="left"><p>Quotas are not supported.</p></td>
</tr>
</tbody>
</table>

 

## Remarks

RDBSS issues a call to *MRxSetQuotaInfo* in response to receiving an [**IRP\_MJ\_SET\_QUOTA**](irp-mj-set-quota.md) request.

Before calling *MRxSetQuotaInfo*, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The *Info.Buffer* member is set to the user buffer from I/O request packet. This buffer has already been locked by RDBSS if needed.

The **Info.LengthRemaining** member is set to **IrpSp-&gt;Parameters.SetQuota.Length**.

## Requirements

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


[**MRxIsValidDirectory**](/windows-hardware/drivers/ddi/mrx/nc-mrx-pmrx_chkdir_calldown)

[**MRxQueryDirectory**](mrxquerydirectory.md)

[**MRxQueryEaInfo**](mrxqueryeainfo.md)

[**MRxQueryFileInfo**](mrxqueryfileinfo.md)

[**MRxQueryQuotaInfo**](mrxqueryquotainfo.md)

[**MRxQuerySdInfo**](mrxquerysdinfo.md)

[**MRxQueryVolumeInfo**](mrxqueryvolumeinfo.md)

[**MRxSetEaInfo**](mrxseteainfo.md)

[**MRxSetFileInfo**](mrxsetfileinfo.md)

[**MRxSetFileInfoAtCleanup**](mrxsetfileinfoatcleanup.md)

[**MRxSetSdInfo**](mrxsetsdinfo.md)

[**MRxSetVolumeInfo**](mrxsetvolumeinfo.md)

 

