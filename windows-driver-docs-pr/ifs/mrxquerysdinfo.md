---
title: MRxQuerySdInfo routine
description: TheMRxQuerySdInfo routine is called by RDBSS to request that a network mini-redirector query security descriptor information on a file system object.
ms.assetid: 5bab05f1-2a79-42c0-ba70-e1124f7b1528
keywords: ["MRxQuerySdInfo routine Installable File System Drivers", "PMRX_CALLDOWN"]
topic_type:
- apiref
api_name:
- MRxQuerySdInfo
api_location:
- mrx.h
api_type:
- UserDefined
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MRxQuerySdInfo routine


The*MRxQuerySdInfo* routine is called by [RDBSS](https://msdn.microsoft.com/library/windows/hardware/ff556810) to request that a network mini-redirector query security descriptor information on a file system object.

Syntax
------

```ManagedCPlusPlus
PMRX_CALLDOWN MRxQuerySdInfo;

NTSTATUS MRxQuerySdInfo(
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

*MRxQuerySdInfo* returns STATUS\_SUCCESS on success or an appropriate NTSTATUS value, such as one of the following:

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
<td align="left"><strong>STATUS_BUFFER_OVERFLOW</strong></td>
<td align="left"><p>The buffer to receive the security descriptor information was too small.</p>
<p>This return value should be considered success and as much valid data as possible should be returned in the <strong>Info.Buffer</strong> member of the RX_CONTEXT structure pointed to by the <em>RxContext</em> parameter.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_BUFFER_TOO_SMALL</strong></td>
<td align="left"><p>The buffer is too small to receive the requested data.</p>
<p>If this value is returned, the <strong>InformationToReturn</strong> member of the RX_CONTEXT structure pointed to by the <em>RxContext</em> parameter should be set to the minimum size of the expected buffer for the call to succeed.</p></td>
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
<td align="left"><strong>STATUS_NETWORK_ACCESS_DENIED</strong></td>
<td align="left"><p>Network access was denied.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_NOT_IMPLEMENTED</strong></td>
<td align="left"><p>A feature that is requested, such as information on a remote page file, is not implemented.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_NOT_SUPPORTED</strong></td>
<td align="left"><p>Security descriptor information is not supported on the remote share.</p></td>
</tr>
<tr class="even">
<td align="left"><strong>STATUS_OBJECT_PATH_NOT_FOUND</strong></td>
<td align="left"><p>The object path was not found. This error can be returned if information on an NTFS stream object was requested and the remote file system does not support streams.</p></td>
</tr>
<tr class="odd">
<td align="left"><strong>STATUS_REPARSE</strong></td>
<td align="left"><p>A reparse is required to handle a symbolic link.</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

RDBSS issues a call to *MRxQuerySdInfo* in response to receiving an [**IRP\_MJ\_QUERY\_SECURITY**](irp-mj-query-security.md) request.

Before calling *MRxQuerySdInfo*, RDBSS modifies the following members in the RX\_CONTEXT structure pointed to by the *RxContext* parameter:

The **QuerySecurity.SecurityInformation** member is set to **IrpSp-&gt;Parameters.QuerySecurity.SecurityInformation**.

The **Info.Buffer** member is set to user buffer from I/O request packet. This buffer has already been locked by RDBSS if needed.

The **Info.LengthRemaining** member is set to **IrpSp-&gt;Parameters.QuerySecurity.Length**.

On success, the network mini-redirector should set the **InformationToReturn** member of the RX\_CONTEXT structure to the length of the security information returned. If the call to *MRxQuerySdInfo* was successful, RDBSS sets the **IoStatus.Information** member of the IRP to the **InformationToReturn** member of RX\_CONTEXT.

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

[**MRxQueryVolumeInfo**](mrxqueryvolumeinfo.md)

[**MRxSetEaInfo**](mrxseteainfo.md)

[**MRxSetFileInfo**](mrxsetfileinfo.md)

[**MRxSetFileInfoAtCleanup**](mrxsetfileinfoatcleanup.md)

[**MRxSetQuotaInfo**](mrxsetquotainfo.md)

[**MRxSetSdInfo**](mrxsetsdinfo.md)

[**MRxSetVolumeInfo**](mrxsetvolumeinfo.md)

 

 






